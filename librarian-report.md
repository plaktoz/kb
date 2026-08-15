# Librarian Report — 2026-08-15

## Summary
- Candidate pairs inspected: 30 (from 444 slug-similarity + 874 link-overlap pool; filtered to highest-confidence)
- Duplicates found: 6
- Superseded pairs found: 9
- Straggler raw files: 528

---

## Duplicate #1
- **A**: `wiki/technology/siri-ai-icloud-paywall-tiered-access.md` (2026-08-01)
- **B**: `wiki/technology/siri-ai-paywall-icloud-plus-tiered-access.md` (2026-08-01)
- **Why**: Same TechCrunch source URL and date; both cover the Siri AI paywall announcement with near-identical summaries, differing only in minor WikiLink choices.
- **Action**: merge-into-B

## Duplicate #2
- **A**: `wiki/technology/stripe-projects-cli-production-dev-stack.md` (2026-08-01)
- **B**: `wiki/technology/stripe-projects-production-dev-stack-cli.md` (2026-08-01)
- **Why**: Identical source URL, same date; both describe the Stripe Projects CLI tool with the same summary — filenames are the same tokens in different order.
- **Action**: merge-into-B

## Duplicate #3
- **A**: `wiki/finance/novo-nordisk-ziltivekimab-trial-failure-dip.md` (2026-08-01)
- **B**: `wiki/finance/novo-nordisk-ziltivekimab-trial-failure.md` (2026-08-01)
- **Why**: Same Motley Fool source URL and date; both cover Novo Nordisk's Ziltivekimab Phase 3 failure with nearly identical content.
- **Action**: merge-into-B

## Duplicate #4
- **A**: `wiki/finance/dwindling-cash-soaring-memory-costs-ai-buildout.md` (2026-08-01)
- **B**: `wiki/technology/tech-ai-buildout-memory-crisis-cash-flow-squeeze.md` (2026-08-01)
- **Why**: Same CNBC source URL and date; both cover the same AI buildout cash/memory cost story — filed in different categories.
- **Action**: merge-into-B

## Duplicate #5
- **A**: `wiki/technology/ai-native-company-brain-garry-tan.md` (2026-07-28)
- **B**: `wiki/technology/every-company-should-have-a-brain-garry-tan.md` (2026-08-01)
- **Why**: Same YouTube source; both 40 lines; both cover Garry Tan's "company brain" framework with similar depth — A has richer WikiLinks, B has slightly more narrative.
- **Action**: merge-into-A

## Duplicate #6
- **A**: `wiki/learning/ryan-holiday-wisdom-takes-work-3-ways.md` (2026-08-01)
- **B**: `wiki/strategy/3-ways-to-get-wiser-wisdom-takes-work.md` (2026-07-29)
- **Why**: Same YouTube source; 37 vs 36 lines; both cover Ryan Holiday's three wisdom practices from the same video — filed in different categories.
- **Action**: merge-into-B

## Superseded #7
- **Keep**: `wiki/technology/monday-com-ai-layoffs-20-major-tech-companies.md` (2026-08-01)
- **Old**: `wiki/technology/monday-com-ai-layoffs-20-major-tech-companies-2026.md` (2026-07-26)
- **Why**: Same TechCrunch source; Keep is newer (2026-08-01) with better-structured concepts and additional insight on the Nasdaq underperformance signal.
- **Action**: merge-into-Keep

## Superseded #8
- **Keep**: `wiki/technology/synopsys-nvidia-agentic-ai-chip-design.md` (2026-08-01)
- **Old**: `wiki/technology/synopsys-nvidia-agentic-ai-chip-design-2026.md` (2026-07-27)
- **Why**: Same TipRanks source; Keep is newer and more comprehensive with richer concept definitions and a second-order supply chain insight.
- **Action**: merge-into-Keep

## Superseded #9
- **Keep**: `wiki/technology/every-level-of-claude-explained.md` (2026-07-29)
- **Old**: `wiki/technology/claude-levels-1-to-5-architect-progression.md` (2026-08-02)
- **Why**: Same YouTube source; despite being older, Keep covers all 5 levels in full depth with Boris Cherny context, while Old is truncated after Level 4.
- **Action**: merge-into-Keep

## Superseded #10
- **Keep**: `wiki/strategy/how-organizations-can-capture-value-from-digital-colleagues.md` (2026-08-01)
- **Old**: `wiki/technology/how-organizations-capture-value-digital-colleagues.md` (2026-07-28)
- **Why**: Same MIT Sloan source; Keep is newer (34 lines vs 25) and correctly filed under strategy; Old is smaller and in the wrong category.
- **Action**: merge-into-Keep

## Superseded #11
- **Keep**: `wiki/finance/hsbc-spacex-coverage-115-price-target-2026.md` (2026-08-01)
- **Old**: `wiki/finance/hsbc-spacex-initiation-115-price-target-2026.md` (2026-07-27)
- **Why**: Same Motley Fool source; Keep is newer (35 lines vs 27) and more comprehensive on the bull case and price target rationale.
- **Action**: merge-into-Keep

## Superseded #12
- **Keep**: `wiki/health/time-restricted-eating-brain-health-older-adults.md` (2026-08-01)
- **Old**: `wiki/health/time-restricted-eating-brain-health.md` (2026-07-29)
- **Why**: Same source; Keep is newer (38 lines vs 31) with more detail on the older-adult cohort findings.
- **Action**: merge-into-Keep

## Superseded #13
- **Keep**: `wiki/finance/brace-for-volatility-fed-big-tech-earnings-markets.md` (2026-08-01)
- **Old**: `wiki/finance/brace-for-volatility-fed-big-tech-earnings-week.md` (2026-07-28)
- **Why**: Same Business Insider source; Keep is newer and filed with the updated framing post-earnings week; Old is the pre-week preview version.
- **Action**: merge-into-Keep

## Superseded #14
- **Keep**: `wiki/technology/doordash-instacart-uber-eats-llm-search-architectures.md` (2026-08-01)
- **Old**: `wiki/technology/llm-search-integration-doordash-instacart-uber-eats.md` (2026-07-29)
- **Why**: Same ByteByteGo source; Keep is newer (41 lines vs 34) with clearer architectural framing and more specific technical details.
- **Action**: merge-into-Keep

## Superseded #15
- **Keep**: `wiki/finance/ibm-quantum-foundry-trump-grant.md` (2026-07-27)
- **Old**: `wiki/finance/ibm-quantum-foundry-trump-1b-grant.md` (2026-08-01)
- **Why**: Same Stocktwits source; despite being older, Keep has richer WikiLinks ([[Anderon]], [[Wedbush]], [[Department of Commerce]]) and more complete concept coverage; Old is a sparser re-ingest.
- **Action**: merge-into-Keep

---

## Phase 6: Unmatched Raw Files

- **Straggler files found**: 528
- **Action**: archive

> Note: The large straggler count reflects articles processed before the current wiki naming convention or during an earlier pipeline version that did not create matching wiki notes. Many are older evergreen articles (2000–2024) that may be worth re-ingesting or simply archiving.

### Files to archive

- `raw/processed/2000-10-02-painless-functional-specifications-part-1-why-bother.md`
- `raw/processed/2004-05-01-is-design-dead.md`
- `raw/processed/2005-06-14-up-front-requirements.md`
- `raw/processed/2005-12-13-new-methodology.md`
- `raw/processed/2008-02-15-fixed-schedule-productivity-time-management-roundup.md`
- `raw/processed/2008-07-14-stop-procrastinating-making-it-easier-to-procrastinate.md`
- `raw/processed/2011-01-11-video-the-best-way-to-play-office-politics.md`
- `raw/processed/2011-07-08-introduction-to-mental-model-of-redundancy.md`
- `raw/processed/2013-06-20-learn-physics-like-newton-beginner-expert-strategies.md`
- `raw/processed/2016-01-12-should-you-use-deliberate-practice-or-just-practice.md`
- `raw/processed/2016-12-14-immigration-extinction-and-island-equilibrium.md`
- `raw/processed/2017-06-28-activation-energy-why-getting-started-is-the-hardest-part.md`
- `raw/processed/2019-10-30-video-telling-stories-with-data-in-3-steps-quick-study.md`
- `raw/processed/2021-07-07-video-8-email-etiquette-tips-how-to-write-better-emails-at-work.md`
- `raw/processed/2021-09-02-gentle-introduction-to-graph-neural-networks.md`
- `raw/processed/2021-10-05-video-6-tips-for-productive-1-1-meetings-with-your-manager.md`
- `raw/processed/2022-02-23-video-what-is-strategy-its-a-lot-simpler-than-you-think.md`
- `raw/processed/2022-06-29-video-a-plan-is-not-a-strategy.md`
- `raw/processed/2022-10-30-the-mindset-of-a-successful-practitioner.md`
- `raw/processed/2023-01-11-expertise-expert-8-tips-learning-new-skill.md`
- `raw/processed/2023-01-11-expertise-expert-offers-8-tips-for-learning-a-new-skill.md`
- `raw/processed/2023-04-11-ten-favorite-papers-science-of-learning-thinking.md`
- `raw/processed/2023-06-23-llm-powered-autonomous-agents.md`
- `raw/processed/2023-08-23-video-what-is-retrieval-augmented-generation-rag.md`
- `raw/processed/2023-09-10-implementing-learning-principles-with-a-personal-ai-tutor.md`
- `raw/processed/2023-11-29-how-to-build-an-adaptive-ai-tutor-using-kg-rag.md`
- `raw/processed/2024-02-21-reflection-agents.md`
- `raw/processed/2024-03-01-when-time-management-was-easy.md`
- `raw/processed/2024-03-15-enhancing-rag-applications-accuracy-with-knowledge-graphs.md`
- `raw/processed/2024-03-20-agentic-design-patterns-part-1.md`

> Full list of 528 straggler files omitted for readability. Run the following to regenerate: `python3 -c "import os,re; wiki={f for r,d,fs in os.walk('wiki') for f in fs if not 'archived' in r and f.endswith('.md')}; [print(f) for f in sorted(os.listdir('raw/processed')) if f.endswith('.md') and re.sub(r'^\d{4}-\d{2}-\d{2}-','',f) not in wiki]"`
