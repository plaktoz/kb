# Human-in-the-Loop AI

source_url: https://cloud.google.com/discover/human-in-the-loop

---

Human-in-the-loop (HITL) is an AI/ML approach where humans are integrated into the training, evaluation, or decision-making process of an AI system — ensuring human judgment guides, corrects, or validates model outputs.

## The Autonomy Spectrum

AI systems exist on a spectrum from full human control to full automation:

| Level | Description |
|-------|-------------|
| Human-in-the-loop | Human actively participates in each decision/cycle |
| Human-on-the-loop | Human monitors; can intervene but system runs autonomously |
| Human-out-of-the-loop | Fully automated, no human intervention |

## Oversight Models

**Active HITL**: Humans label training data, validate predictions before action. Used in: medical diagnosis, legal review, content moderation.

**Passive/Monitoring**: System acts autonomously, humans review outcomes/metrics. Used in: fraud detection alerts, recommendation systems.

**Exception-Based**: System handles routine cases automatically; humans only handle edge cases or low-confidence predictions. Most scalable approach.

## When to Involve Humans vs. Automate

**Involve humans when:**
- High stakes decisions (healthcare, finance, legal)
- Low model confidence scores below threshold
- Novel/edge cases outside training distribution
- Ethical sensitivity — bias risk, fairness concerns
- Regulatory requirements mandate human oversight
- Early model deployment — building ground truth data

**Automate fully when:**
- High-volume, repetitive tasks with clear rules
- Model confidence is consistently high
- Low consequence of errors
- Real-time speed requirements preclude human review
- Well-established model performance with proven accuracy

## Practical Implementation

- **Define confidence thresholds** — Route low-confidence predictions to humans
- **Design feedback loops** — Human corrections should feed back into retraining
- **Avoid alert fatigue** — Too many human reviews reduces quality of oversight
- **Track reviewer performance** — Human reviewers can also introduce bias
- **Use active learning** — Intelligently select which cases need human review
