import json
import subprocess
import sys
import tempfile
import threading
import time
import unittest
from datetime import timedelta
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import scrape_queue as sq

SCRIPT = Path(__file__).parent / "scrape_queue.py"
PARA = "<p>" + "The quarterly numbers beat every estimate on the street. " * 8 + "</p>"
ARTICLE = f"""<html><head><title>Fallback title</title>
<meta property="og:title" content="Chipmaker beats estimates">
<meta name="author" content="Jane Doe">
<meta property="article:published_time" content="2026-09-28T07:43:00Z">
</head><body><nav><p>Home | Markets | Tech</p></nav>
<article>{PARA * 4}</article><footer><p>Copyright</p></footer></body></html>"""
CHALLENGE = """<html><head><title>Just a moment...</title></head>
<body><script src="/cdn-cgi/challenge-platform/h/b/orchestrate/chl_page"></script></body></html>"""
PAYWALL = f"""<html><head><script type="application/ld+json">
{{"@context":"https://schema.org","@type":"NewsArticle","headline":"Bond yields",
"isAccessibleForFree":"False","author":{{"@type":"Person","name":"A. Writer"}}}}
</script></head><body>{PARA}<p>Subscribe to continue reading.</p></body></html>"""
TABLE_LAYOUT = ("<html><head><title>How to Prepare</title></head><body><table><tr><td><font face=verdana>"
                + "Universities already have what founders need. " * 60 + "<br><br>"
                + "The hard part is the product. " * 10 + "<p>" + "An epigraph in the only p tag. " * 24
                + "</p></font></td></tr></table></body></html>")
JS_SHELL = '<html><body><div id="root"></div><script>render()</script></body></html>'

ROUTES = {
    "/article": (200, ARTICLE),
    "/challenge": (403, CHALLENGE),
    "/forbidden": (403, "<html><body>Forbidden</body></html>"),
    "/challenge-200": (200, CHALLENGE),
    "/paywall": (200, PAYWALL),
    "/js": (200, JS_SHELL),
    "/table": (200, TABLE_LAYOUT),
    "/gone": (404, "<html>Not found</html>"),
    "/down": (502, "<html>Bad gateway</html>"),
    "/long": (200, "<html><body>" + PARA * 200 + "</body></html>"),
    "/news/live-updates/markets": (200, ARTICLE),
}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/drip":
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            for _ in range(60):
                self.wfile.write(b"<p>")
                self.wfile.flush()
                time.sleep(1)
            return
        status, body = ROUTES.get(self.path, (404, ""))
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, *a):
        pass


class ProbeTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.server.daemon_threads = True
        threading.Thread(target=cls.server.serve_forever, daemon=True).start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()

    def probe(self, path):
        return sq.probe_all([self.base + path])[0]

    def test_verdict_per_page_kind(self):
        expected = {
            "/article": "ok",
            "/challenge": "blocked",
            "/forbidden": "blocked",
            "/challenge-200": "blocked",
            "/paywall": "paywall",
            "/js": "thin",
            "/table": "ok",
            "/gone": "dead",
            "/down": "unreachable",
            "/news/live-updates/markets": "thin",
        }
        got = {path: p.verdict for path, p in zip(expected, sq.probe_all([self.base + p for p in expected]))}
        self.assertEqual(got, expected)

    def test_ok_page_carries_metadata_and_body_without_nav(self):
        p = self.probe("/article")
        self.assertEqual((p.title, p.author, p.published), ("Chipmaker beats estimates", "Jane Doe", "2026-09-28"))
        text = Path(p.text_path).read_text()
        self.assertIn("beat every estimate", text)
        self.assertNotIn("Home | Markets", text)
        self.assertNotIn("Copyright", text)

    def test_table_layout_keeps_paragraph_breaks(self):
        text = Path(self.probe("/table").text_path).read_text()
        self.assertIn("founders need.\n\nThe hard part", text)

    def test_long_article_is_capped_and_says_so(self):
        p = self.probe("/long")
        self.assertEqual(p.verdict, "ok")
        self.assertIn(f"first {sq.MAX_TEXT_CHARS} kept", p.reason)
        self.assertLess(len(Path(p.text_path).read_text()), sq.MAX_TEXT_CHARS + 500)

    def test_paywall_reads_json_ld_author(self):
        p = self.probe("/paywall")
        self.assertEqual((p.verdict, p.author, p.text_path), ("paywall", "A. Writer", None))

    def test_refused_connection_is_unreachable_not_dead(self):
        self.assertEqual(sq.probe_all(["http://127.0.0.1:9/nothing"])[0].verdict, "unreachable")

    def test_slow_drip_server_cannot_hang_the_cli(self):
        start = time.monotonic()
        out = subprocess.run([sys.executable, str(SCRIPT), "probe", self.base + "/drip", self.base + "/article"],
                             capture_output=True, text=True, timeout=sq.DEADLINE_S + 10)
        elapsed = time.monotonic() - start
        verdicts = [p["verdict"] for p in json.loads(out.stdout)]
        self.assertEqual(verdicts, ["unreachable", "ok"])
        self.assertLess(elapsed, sq.DEADLINE_S + 3)


class VaultTest(unittest.TestCase):
    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "raw" / "url").mkdir(parents=True)
        (self.root / "raw" / "processed").mkdir()
        (self.root / "wiki" / "finance").mkdir(parents=True)
        (self.root / "kbm.log.md").write_text("# KBM Activity Log\n\n| Date | File | Activity |\n")
        (self.root / "raw" / "processed" / "2026-09-01-old.md").write_text(
            "---\nsource_url: https://example.com/old\n---\n# Old\n")
        (self.root / "raw" / "url" / "2026-10-01-news-aggregation.md").write_text(
            "## Finance\n- **Old**: seen\n  URL: https://example.com/old\n"
            "- **New**: fresh\n  URL: https://example.com/new).\n"
            "- **Dup**: again\n  URL: https://example.com/new\n")
        (self.root / "raw" / "url" / "done.processed.md").write_text("https://example.com/ignored\n")

    def test_pending_urls_skip_processed_files_and_dedupe(self):
        files, urls = sq.pending_urls(self.root)
        self.assertEqual(files, ["raw/url/2026-10-01-news-aggregation.md"])
        self.assertEqual(urls, ["https://example.com/old", "https://example.com/new"])
        self.assertEqual(sq.scraped_urls(self.root), {"https://example.com/old"})

    def test_seen_splits_vault_failed_and_fresh(self):
        with (self.root / "kbm.log.md").open("a") as log:
            log.write("| 2026-09-30 | https://example.com/paywalled (blocked: http 403) | scrape-failed |\n")
        out = subprocess.run([sys.executable, str(SCRIPT), "seen", "https://example.com/old",
                              "https://example.com/paywalled", "https://example.com/brand-new)."],
                             capture_output=True, text=True, cwd=self.root, check=True)
        self.assertEqual(json.loads(out.stdout), {
            "inVault": ["https://example.com/old"],
            "failedBefore": ["https://example.com/paywalled"],
            "blockedDomain": [],
            "fresh": ["https://example.com/brand-new"],
        })

    def test_finalize_is_idempotent(self):
        queue = {"sourceFiles": ["raw/url/2026-10-01-news-aggregation.md"]}
        rows = [{"filename": "2026-10-01-new.md", "activity": "scrape"},
                {"filename": "https://example.com/x (blocked | http 403)", "activity": "scrape-failed"}]
        first = sq.finalize(self.root, queue, rows)
        second = sq.finalize(self.root, queue, rows)
        log = (self.root / "kbm.log.md").read_text().splitlines()
        self.assertEqual((first["appended"], second["appended"]), (3, 0))
        self.assertEqual(log[-3:], [
            f"| {sq.date.today()} | 2026-10-01-new.md | scrape |",
            f"| {sq.date.today()} | https://example.com/x (blocked / http 403) | scrape-failed |",
            f"| {sq.date.today()} | 2026-10-01-news-aggregation.processed.md | archive |",
        ])
        self.assertTrue((self.root / "raw" / "url" / "2026-10-01-news-aggregation.processed.md").exists())
        self.assertFalse((self.root / "raw" / "url" / "2026-10-01-news-aggregation.md").exists())


class BlocklistTest(unittest.TestCase):
    MANUAL = "| Reuters.com | manual | blocks scraping, by hand |  -  |"
    TODAY = sq.date(2026, 10, 17)

    def setUp(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "raw" / "processed").mkdir(parents=True)
        (self.root / "wiki").mkdir()
        (self.root / "data").mkdir()
        (self.root / "kbm.log.md").write_text("# KBM Activity Log\n\n| Date | File | Activity |\n")
        (self.root / "data" / "blocked-domains.md").write_text(sq.BLOCKLIST_HEADER + self.MANUAL + "\n")

    def log(self, *rows):
        with (self.root / "kbm.log.md").open("a") as f:
            for day, file, activity in rows:
                f.write(f"| {day} | {file} | {activity} |\n")

    def failed(self, day, url, reason="blocked: http 403"):
        return day, f"{url} ({reason})", "scrape-failed"

    def ok(self, day, url, sub="raw/processed"):
        name = f"{day}-{abs(hash(url))}.md"
        (self.root / sub / name).write_text(f"---\nsource_url: {url}\n---\n# Body\n")
        return day, name, "scrape"

    def auto(self):
        return {r["domain"]: (r["reason"], r["since"])
                for r in sq.regenerate_blocklist(self.root, self.TODAY)[0] if r["source"] == "auto"}

    def test_two_trailing_failures_block_the_domain_and_one_does_not(self):
        self.log(self.failed("2026-10-01", "https://www.paywalled.com/a"),
                 self.failed("2026-10-03", "https://paywalled.com/b"),
                 self.failed("2026-10-03", "https://once.com/a"))
        self.assertEqual(self.auto(), {
            "paywalled.com": ("2 consecutive failed scrapes, last 2026-10-03", "2026-10-01")})

    def test_success_after_failures_clears_the_block(self):
        self.log(self.failed("2026-10-01", "https://site.com/a"), self.failed("2026-10-02", "https://site.com/b"))
        self.assertIn("site.com", self.auto())
        self.log(self.ok("2026-10-04", "https://www.site.com/c", sub="raw"))
        self.assertEqual(self.auto(), {})

    def test_interleaved_failures_do_not_block(self):
        self.log(self.failed("2026-10-01", "https://medicalxpress.com/a"),
                 self.ok("2026-10-02", "https://medicalxpress.com/b"),
                 self.failed("2026-10-03", "https://medicalxpress.com/c"))
        self.assertEqual(self.auto(), {})

    def test_block_expires_block_days_after_the_last_failure(self):
        def streak_ending(days_ago):
            last = self.TODAY - timedelta(days=days_ago)
            self.log(self.failed(str(last - timedelta(days=1)), f"https://stale{days_ago}.com/a"),
                     self.failed(str(last), f"https://stale{days_ago}.com/b"))
        streak_ending(61)
        streak_ending(59)
        self.assertEqual(list(self.auto()), ["stale59.com"])

    def test_dead_links_and_unmapped_successes_are_ignored(self):
        self.log(self.failed("2026-10-01", "https://site.com/a", "dead: http 404"),
                 self.failed("2026-10-02", "https://site.com/b", "page not found"),
                 self.failed("2026-10-03", "https://site.com/c"),
                 ("2026-10-04", "2026-10-04-no-such-file.md", "scrape"),
                 self.failed("2026-10-05", "https://site.com/d", "http 410"))
        self.assertEqual(self.auto(), {})
        self.log(self.failed("2026-10-06", "https://site.com/e"))
        self.assertEqual(self.auto(), {"site.com": ("2 consecutive failed scrapes, last 2026-10-06", "2026-10-03")})

    def test_regeneration_keeps_manual_rows_verbatim_and_is_idempotent(self):
        self.log(self.failed("2026-10-01", "https://zeta.com/a"), self.failed("2026-10-02", "https://zeta.com/b"),
                 self.failed("2026-10-01", "https://alpha.com/a"), self.failed("2026-10-02", "https://alpha.com/b"),
                 self.failed("2026-10-01", "https://reuters.com/a"), self.failed("2026-10-02", "https://reuters.com/b"))
        path = self.root / "data" / "blocked-domains.md"
        _, added = sq.regenerate_blocklist(self.root, self.TODAY)
        first = path.read_text()
        _, added_again = sq.regenerate_blocklist(self.root, self.TODAY)
        self.assertEqual(path.read_text(), first)
        self.assertEqual((added, added_again), (["alpha.com", "zeta.com"], []))
        self.assertEqual(first.splitlines()[-3:], [
            "| alpha.com | auto | 2 consecutive failed scrapes, last 2026-10-02 | 2026-10-01 |",
            self.MANUAL,
            "| zeta.com | auto | 2 consecutive failed scrapes, last 2026-10-02 | 2026-10-01 |",
        ])

    def test_seen_routes_blocked_domains_and_subdomains(self):
        out = subprocess.run([sys.executable, str(SCRIPT), "seen", "https://www.reuters.com/x",
                              "https://uk.reuters.com/y", "https://notreuters.com/z"],
                             capture_output=True, text=True, cwd=self.root, check=True)
        self.assertEqual(json.loads(out.stdout), {
            "inVault": [], "failedBefore": [],
            "blockedDomain": ["https://www.reuters.com/x", "https://uk.reuters.com/y"],
            "fresh": ["https://notreuters.com/z"],
        })

    def test_finalize_reports_newly_blocked_domains_once(self):
        (self.root / "raw" / "url").mkdir()
        queue = {"sourceFiles": []}
        rows = [{"filename": "https://bad.com/a (paywall)", "activity": "scrape-failed"},
                {"filename": "https://bad.com/b (paywall)", "activity": "scrape-failed"}]
        self.assertEqual(sq.finalize(self.root, queue, rows)["blockedDomains"], ["bad.com"])
        self.assertEqual(sq.finalize(self.root, queue, rows)["blockedDomains"], [])
        self.assertIn("| bad.com | auto |", (self.root / "data" / "blocked-domains.md").read_text())


if __name__ == "__main__":
    unittest.main()
