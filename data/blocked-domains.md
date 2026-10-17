# Blocked domains

The news agent skips these domains. `manual` rows are hand-edited and never touched by code.
`auto` rows are regenerated from `kbm.log.md` by `scrape_queue.py` on every `finalize` or
`blocklist` run. A domain is listed while its last 2 or more scrapes all failed (dead links
excluded) and drops off after its next success. A domain also covers its subdomains.

| Domain | Source | Reason | Since |
|--------|--------|--------|-------|
| investors.com | auto | 3 consecutive failed scrapes, last 2026-10-12 | 2026-08-15 |
| reuters.com | manual | blocks scraping | - |
| usatoday.com | auto | 2 consecutive failed scrapes, last 2026-10-05 | 2026-10-05 |
