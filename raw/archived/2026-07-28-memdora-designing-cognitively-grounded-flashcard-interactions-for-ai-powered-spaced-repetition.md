# Memdora: Designing Cognitively-Grounded Flashcard Interactions for AI-Powered Spaced Repetition

source_url: https://arxiv.org/html/2607.25096v1

---

arXiv preprint, July 2026.

## Abstract

Spaced repetition systems (SRS) have demonstrated robust effects on long-term retention, yet existing tools reduce the flashcard interaction to a single binary gesture: flip and self-rate. This impoverished interaction model fails to leverage decades of cognitive science evidence on retrieval practice, and requires learners to context-switch out of their reading flow to create cards manually. The paper presents Memdora, a cross-platform AI spaced repetition system built around four contributions: (1) a taxonomy of 17 cognitively-grounded interaction types across three learning categories — Language (6 types), By Heart (1 type with 3 retrieval modes), and Exam (10 types) — each mapped to peer-reviewed cognitive science evidence displayed on every card; (2) a unified AI generation pipeline that collapses card creation to a single gesture at the point of reading across web, mobile, and three browser extensions; (3) a collaborative classroom layer for teachers to publish decks, assign them to students, and track outcomes at the individual card level; and (4) an effort-based behavioral reward system that incentivizes actual cognitive engagement rather than mere app presence. Memdora integrates FSRS-6, the current state-of-the-art spaced repetition algorithm.

## Background

The forgetting curve, described by Ebbinghaus in 1885, remains one of the most replicated findings in cognitive psychology: without review, humans forget roughly 70% of newly learned material within 24 hours. Despite decades of evidence supporting spaced repetition, mainstream tools — most notably Anki, with over 10 million downloads — have changed little since SuperMemo's SM-2 algorithm in 1987. These tools reduce the flashcard interaction to a single gesture: flip, reveal, self-rate.

This binary model has two limitations. First, it ignores evidence that different retrieval formats (multiple choice, free recall, fill-in-the-blank, error detection, sequential reconstruction) activate different cognitive processes and produce differential retention. Flipping a card to see a translation is recognition-based recall — among the weakest forms of retrieval — while generating an answer before revealing it, completing a cloze deletion, or reconstructing a passage produces superior retention through the testing effect. Second, existing tools impose significant creation friction: a prior study of AI flashcard systems found students reported spending more energy preparing cards than actually studying them.

## The taxonomy of 17 interaction types

**Language category (6 types):** Vocabulary, Cloze, Phrase, Concept, Reverse, Sentence — supporting vocabulary and phrase acquisition with retention grounded in retrieval-practice, cloze-deletion, chunking, and elaborative-interrogation research.

**By Heart category (1 type, 3 modes):** For verbatim memorization of passages, speeches, and quotations. Users self-select difficulty via Strip Peek (highest effort — all lines hidden, tap to reveal for 2 seconds), Step Through (partial cueing from preceding lines), or First Word (lightest cue — only the opening word shown). This operationalizes Bjork's "desirable difficulties" framework, letting learners calibrate challenge to their current competence.

**Exam category (10 types):** Multiple Choice, Q&A, True/False, Matching, Sequence, Formula, Scenario, Error Spot, Comparison, Fill the Blank — each mapped to a specific cognitive-science citation, from recognition-based retrieval to transfer-appropriate processing.

## Behavioral design

Memdora rewards cognitive effort rather than app presence: users earn AI generation credits for 5 continuous minutes of active review or 100 cards reviewed in a day, rather than simply for opening the app — a deliberate contrast with Duolingo-style streaks, which reward any app interaction. Every card displays its current FSRS-6 retention percentage and a citation to the cognitive-science paper grounding its interaction type, aiming to build learner trust and metacognitive awareness.

## Implementation and limitations

Memdora is a full-stack TypeScript application (React web frontend, React Native mobile apps, WebExtensions-based browser extensions for Chrome, Edge, and Firefox) with FSRS-6 running client-side for offline mobile scheduling. The authors' primary stated limitation is the absence of a controlled user study evaluating whether the 17-type taxonomy actually improves retention outcomes in practice; a longitudinal study comparing card types and reward structures is planned as future work.
