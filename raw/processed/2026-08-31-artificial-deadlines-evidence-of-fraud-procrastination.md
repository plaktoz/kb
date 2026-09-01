---
title: "Artificial Deadlines (Part 1): Evidence of Fraud in an Influential Study About Procrastination"
source_url: "https://datacolada.org/138"
date: "2026-08-31"
author: "Uri, Joe, & Leif (Data Colada)"
---

# Artificial Deadlines (Part 1): Evidence of Fraud in an Influential Study About Procrastination

**Authors:** Uri, Joe, & Leif (Data Colada)
**Published:** August 31, 2026

## Overview

A new *Psychological Science* paper reports a failure to replicate Study 2 of Ariely and Wertenbroch's 2002 article, "Procrastination, Deadlines, and Performance: Self-Control by Precommitment." The original study found that evenly spaced external deadlines improved task performance compared to self-set or single end-date deadlines. With 2,100+ Google Scholar citations, the paper has been widely assigned in economics and psychology courses.

After receiving the original data files (emailed from Ariely's MIT account in 2006, forwarded to Data Colada in 2023), the authors conducted a full analysis and concluded the data were tampered with.

---

## Background

Co-author Klaus Wertenbroch, who reportedly never had access to the data, forwarded Hyndman's 2006 data request to Ariely. When the replication team asked Ariely in 2024 to comment on anomalies in those files, he denied the request, stating the files "may not be the actual data" and provided no alternative data.

---

## Study 2 Design

- **Task:** Proofreading three 10-page documents, each containing 100 errors
- **N:** 60 participants, 20 per condition
- **Conditions:**
  - Evenly Spaced Deadlines (days 7, 14, 21)
  - Set Your Own Deadlines (within 21 days)
  - Last Day Deadline (all due day 21)

Published results showed a strong advantage for evenly spaced deadlines across all three dependent variables.

---

## Four Red Flags

### Red Flag #1: Implausibly Large Effect Sizes

The evenly spaced group averaged 136.1 corrections vs. 71.1 for the last-day group — a Cohen's *d* = 2.5. For context:

- Gender difference in height: *d* ≈ 1.8
- Gender difference in shoes owned: *d* ≈ 1.2
- Perceived argument count (9 vs. 3 arguments): *d* = 1.49

An effect where deadlines influence proofreading more than the literal number of arguments affects perceived argument count is not credible. The condition distributions barely overlap — 90% of the evenly-spaced group exceeded the maximum of the last-day group.

### Red Flag #2: Duplicate Observations

In the Last Day condition, 18 of 20 participants had an exact "corrections twin" — another participant with identical correction counts across all three tasks individually. These twins had ID numbers exactly 10 apart (S1/S11, S7/S17, etc.). No duplicates appeared in the other two conditions. This pattern is inconsistent with genuine data.

### Red Flag #3: Missing Correlations Where Strong Ones Are Expected

Three categories of variables that should correlate strongly within conditions did not in the original data:

| Variable Pair | Original Data (range) | Replication (range) |
|---|---|---|
| Subjective ratings (5 measures) | −.29 to +.18 | +.63 to +.92 |
| Performance across 3 tasks | +.03 to +.27 | +.74 to +.90 |
| Time spent across 3 tasks | +.05 to +.17 | +.79 to +.95 |

All replication correlations were highly significant (ps < 0.0000024). None of the original correlations were both positive and significant.

### Red Flag #4: No Rounding in Self-Reported Time

When asked to estimate minutes spent per task:

- **Replication participants:** 85% gave round numbers (e.g., 20, 30 minutes) — typical human behavior
- **Original data:** Only 11.7% gave round numbers — consistent with chance (~10%), not human estimation

---

## Conclusion

The authors state they cannot generate a benign explanation for all four anomalies simultaneously. They conclude the Study 2 data were "severely tampered with or fabricated."

A follow-up post (Part 2) will analyze the Study 1 data with different methods but similar conclusions.

---

## Author Responses

- **Klaus Wertenbroch:** Confirmed he never had data access; distinguished between demand for precommitment (replicated) and effectiveness in these specific studies (not replicated); requested retraction.
- **Dan Ariely:** Did not reply to Data Colada. Posted publicly that the data contained "serious anomalies" and that his documentary record and memory are "insufficient to answer the questions raised." Committed to cooperating with retraction processes.
- **Hyndman & Bisin:** Noted their replication "stands on its own methodological findings" and distanced themselves from analysis of the historical files.
- **Simine Vazire (Editor, *Psychological Science*):** Said the journal is considering "best next steps... in accordance with COPE guidelines."

---

*Data and code available at [ResearchBox 7135](https://researchbox.org/7135?PEER_REVIEW_passcode=GXBLRW).*
