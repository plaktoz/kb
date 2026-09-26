---
type: literature-note
source_url: https://docs.typesafe.ai/confidence
author: Unknown
tags: [jev, confidence-scores, decision-making, ai-reliability]
date_consumed: 2026-09-26
---

## Summary

Every [[Jev]] Choice and Score answer includes a `confidence` score (0–1) derived from the shape of the probability distribution across options — concentrated distributions signal certainty, flat distributions signal uncertainty. TypeSafe recommends splitting confidence into three behavioral tiers (high → act automatically, medium → proceed cautiously, low → route to human) with thresholds scaled to the risk level of the action. The raw `probabilities` array is always available for developers who need custom confidence measures.

## Core Concepts

- **[[Confidence Score]]** — a 0–1 value computed automatically on every Choice and Score answer; derived from probability distribution shape using approximately `(n × largest_probability − 1) / (n − 1)`
- **Distribution shape** — concentrated distribution → high confidence (one option dominates); flat distribution → low confidence (no clear winner)
- **[[Confidence-Gated Routing]]** — three behavioral tiers: high confidence → act automatically; medium → flag or confirm; low → route to human
- **Risk-scaled thresholds** — no single correct threshold; destructive operations require higher confidence than read-only ones (e.g. `> 0.9` for approving a transfer vs `> 0.5` for checking a balance)
- **Raw probabilities** — `response.answers["key"].probabilities` always available for custom confidence measures beyond TypeSafe's built-in definition
- **[[Epistemic Honesty]]** — a system that cannot express uncertainty cannot be trusted; confidence is the model's mechanism for honest uncertainty signaling

## Key Takeaways

- **Formula**: `(n × max_prob − 1) / (n − 1)` — where `n` = number of options
- **Noul answers don't include confidence**: only Choice and Score provide it
- **Three tiers**: high → auto-act; medium → cautious; low → human review
- **Start conservative**: begin with strict thresholds and loosen based on observed accuracy
- **Risk scales thresholds**: destructive/irreversible actions need higher confidence cutoffs
- **Custom measures**: use raw `probabilities` array when the built-in confidence doesn't fit

```python
if confidence < 0.5:
    route_to_human(msg)
elif action == "check_balance":
    show_balance(account_id)          # read-only: 0.5 threshold ok
elif action == "approve_transfer":
    if confidence > 0.9:              # destructive: stricter threshold
        confirm_then_execute(account_id)
    else:
        ask_user_to_confirm(account_id)
```

## 🧠 First Principles & Mental Models

- **[[Risk-Reward Calibration]]**: The insight that thresholds should scale with consequence severity is a direct application of expected-value thinking — higher stakes require more certainty before acting, encoding risk tolerance in code rather than in the model.

## 🃏 Review Questions

**Q1**: What does a confidence score near 0 vs near 1 indicate about a Jev answer?
**A**: Near 1 means one option has a dominant probability (model is certain); near 0 means probabilities are evenly spread across options (model has no clear read and is essentially guessing).

**Q2**: Why should the confidence threshold for approving a bank transfer be higher than for checking a balance?
**A**: The threshold encodes risk tolerance — a wrong auto-route on a destructive, irreversible action (transfer) has a much higher cost than on a read-only action (balance check), so stricter certainty is required before acting automatically.

**Q3**: When should a developer use raw `probabilities` instead of the built-in `confidence` value?
**A**: When the use case requires a custom certainty measure — e.g. treating a close second-place option as a signal, or computing entropy across the full distribution rather than just the top probability.
