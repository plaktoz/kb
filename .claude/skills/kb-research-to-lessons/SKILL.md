---
name: kb-research-to-lessons
description: Convert a research report (research/<slug>/report.md) into a self-contained interactive HTML lesson course. Two phases: plan (MISSION.md + lessons.md curriculum), pause for confirmation, then generate all lesson HTML files in parallel. Use when the user wants to turn a research report into a structured course.
---

# KB Research to Lessons

Convert a research report into a self-contained interactive HTML lesson course co-located with the report.

## Invocation

```
/kb-research-to-lessons <path-to-report>
```

Example: `/kb-research-to-lessons research/effective-learning-with-ai/report.md`

Pass `--force` to overwrite an existing MISSION.md or LESSONS.md.

---

## Phase 1 — Plan

### Step 1 — Parse args and validate

Extract the report path from args. Derive the research directory (parent of the report file).

Check for existing files:
```bash
ls <research-dir>/MISSION.md <research-dir>/lessons.md 2>/dev/null
```

If either exists AND `--force` was not passed, stop and tell the user:
> `MISSION.md` (or `lessons.md`) already exists at `<research-dir>/`. Run with `--force` to overwrite, or delete the files manually.

If `--force` was passed, proceed and overwrite.

Read the full report file.

### Step 2 — Generate MISSION.md

Write `<research-dir>/MISSION.md` using this format:

```markdown
# Mission: {Topic from report title}

## Why
{1-3 sentences. The concrete real-world goal behind studying this topic. What changes when the learner has this knowledge? Avoid "to understand X" — push for the underlying outcome.}

## Success looks like
- {A specific, observable thing the learner will be able to do}
- {Another specific thing — aim for 3-5 bullets}

## Constraints
- Learning from research papers — no access to proprietary systems
- Self-paced, one lesson at a time

## Out of scope
- {Adjacent topics not covered by the report}
```

Derive all content from the report — do not invent.

### Step 3 — Generate lessons.md curriculum plan

Analyse the report and design a lesson curriculum. Rules:
- Target **8–15 lessons** total. Justify in a comment if outside this range.
- Group lessons into **3–4 modules** that follow a logical learning arc (foundations → architecture → advanced → evaluation is a common pattern, but adapt to the report's structure).
- Each lesson must map to **one source paper or concept cluster** from the report — no lesson without a citation anchor.
- Each lesson must have a **skill exercise** (something the learner actively does, not just reads).

Write `<research-dir>/lessons.md` using this structure:

```markdown
# Lesson Plan: {Topic}

*Source: `<path-to-report>`*
*Each lesson → one HTML file in `lessons/`, one reference doc in `reference/`*

---

## Module N — {Module Title}
*One sentence on why this module comes here in the sequence.*

### Lesson N: {Title}
**File:** `lessons/NNNN-slug.html`
**Key concepts:** concept · concept · concept
**Source paper:** arxiv link or citation — brief result summary
**Skill:** What the learner will actively do to demonstrate understanding
**Reference doc:** `reference/slug.html` (or *(extend existing-ref.html)*)

[repeat for each lesson]

---

## Suggested Teaching Order

[brief note on sequencing logic]

---

## Reference Documents to Build

| File | Contents |
|------|----------|
| `reference/slug.html` | What it contains |
```

### Step 4 — Show plan and pause

Display the contents of `lessons.md` to the user.

Then ask:
> **Plan ready.** Review `lessons.md` above — does this look right? Reply "go" to generate all lessons, or tell me what to change.

**Wait for the user's response. Do not proceed to Phase 2 until they confirm.**

---

## Phase 2 — Generate

Only proceed after explicit user confirmation (e.g. "go", "looks good", "yes").

### Step 5 — Create directory structure

```bash
mkdir -p <research-dir>/lessons
mkdir -p <research-dir>/reference
mkdir -p <research-dir>/assets
```

### Step 6 — Write shared assets

Write `<research-dir>/assets/style.css` — a Tufte-inspired stylesheet with:
- Serif body font (Lora or Georgia fallback)
- Clean, readable typography at 18px base
- CSS classes: `.container`, `.lesson-header`, `.breadcrumb`, `.lesson-meta`, `.callout`, `.callout.key`, `.callout.warning`, `.source-card`, `.quiz`, `.quiz-options`, `.quiz-feedback`, `.exercise`, `.lesson-nav`, `.tutor-prompt`, `table`
- Print-ready media query
- Light/dark-neutral color palette using CSS custom properties

Write `<research-dir>/assets/quiz.js` — a shared quiz widget:
```js
function initQuiz(containerId, correctIndex, explanation) {
  const container = document.getElementById(containerId);
  if (!container) return;
  const buttons = container.querySelectorAll('.quiz-options button');
  const feedback = container.querySelector('.quiz-feedback');
  buttons.forEach((btn, i) => {
    btn.addEventListener('click', () => {
      buttons.forEach(b => b.disabled = true);
      const isCorrect = i === correctIndex;
      btn.classList.add(isCorrect ? 'correct' : 'incorrect');
      if (!isCorrect) buttons[correctIndex].classList.add('correct');
      feedback.textContent = explanation;
      feedback.className = 'quiz-feedback show ' + (isCorrect ? 'correct' : 'incorrect');
    });
  });
}
```

### Step 7 — Generate all lessons in parallel

Spawn one agent per lesson, all in parallel. Each agent receives:
- The full lesson spec from `lessons.md` (key concepts, source paper, skill exercise)
- The relevant section of the research report
- The target file path
- Instructions to use `../assets/style.css` and `../assets/quiz.js`

**Each lesson HTML file must include:**

1. **Header block** with `.breadcrumb` (linking back to `lessons.md`), `h1` title, `.lesson-meta` (estimated time, module label)
2. **`.source-card`** citing the primary paper with arxiv link and key result
3. **Content sections** (`h2` headers) covering the key concepts — derived strictly from the source paper, no invented claims
4. **`.callout.key`** for the single most important insight
5. **`.callout.warning`** for common misconceptions or caveats (when applicable)
6. **`.quiz`** with `id="quiz-N"`:
   - One question, three options
   - **All three options must be exactly the same number of words** — count and equalize before writing
   - `initQuiz('quiz-N', correctIndex, 'Explanation text')` wired at the bottom
7. **`.exercise`** with a textarea — a hands-on skill task the learner actively performs (not multiple choice)
8. **`.lesson-nav`** with prev/next links; first lesson has no prev; last lesson has no next, only "Back to Curriculum"
9. **`.tutor-prompt`** banner: "Questions about this lesson? Ask your tutor — copy any sentence you want to explore deeper."
10. Scripts at the bottom: `<script src="../assets/quiz.js"></script>` then `initQuiz(...)` call

**HTML template skeleton:**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Lesson N — {Title}</title>
  <link rel="stylesheet" href="../assets/style.css">
</head>
<body>
<div class="container">
  <header class="lesson-header">
    <div class="breadcrumb">
      <a href="../lessons.md">{Topic}</a> › {Module} › Lesson N of Total
    </div>
    <h1>{Title}</h1>
    <div class="lesson-meta">
      <span>~N min</span>
      <span>{Module label}</span>
    </div>
  </header>
  <!-- content -->
  <div class="tutor-prompt">Questions about this lesson? Ask your tutor — copy any sentence you want to explore deeper.</div>
  <nav class="lesson-nav">
    <a href="prev.html">← Previous</a>
    <a href="next.html" class="primary">Next →</a>
  </nav>
  <script src="../assets/quiz.js"></script>
  <script>initQuiz('quiz-N', CORRECT_INDEX, 'EXPLANATION');</script>
</div>
</body>
</html>
```

### Step 8 — Housekeeping

After all lesson agents complete:

**Log to `kbm.log.md`:**
```
| YYYY-MM-DD | <research-dir>/lessons/ | lessons |
```

**Update CLAUDE.md skills table** — append a row to the main skills table:
```
| `/kb-research-to-lessons` | Converts a research report into an interactive HTML lesson course with curriculum plan, shared assets, and parallel-generated lessons |
```

---

## Notes

- Never invent facts. Every claim in every lesson must trace back to the source report.
- The planning agent should prefer breadth in the lesson plan — if a concept is too small for a lesson, merge it with a related concept rather than creating a thin lesson.
- If the report has fewer than 5 source papers, it may be too thin to generate 8 lessons. In this case, generate fewer lessons and note the constraint in `lessons.md`.
- Reference documents (`reference/`) are planned in `lessons.md` but not generated by this skill. See TODO.md for that future enhancement.
