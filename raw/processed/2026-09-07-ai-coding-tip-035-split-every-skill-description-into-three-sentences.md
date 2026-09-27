---
source_url: https://hackernoon.com/ai-coding-tip-035-split-every-skill-description-into-three-sentences
author: Maxi Contieri (@mcsee)
date: 2026-09-07
---

# AI Coding Tip 035 - Split Every Skill Description Into Three Sentences

## Core Idea

Skill descriptions should answer exactly three questions: when to read it, when to use it, and what it does. Cramming everything into one paragraph forces agents to open files just to determine relevance — burning context unnecessarily.

## Key Points

**The Problem:** Long, feature-dumping descriptions make agents unable to quickly decide whether a skill applies. They either skip it or open the whole file to check.

**The Format:**
- Sentence 1: Repeat the trigger moment (when to read)
- Sentence 2: Name the exact situation (when to use)
- Sentence 3: State what it does — nothing more

**Why three?** One sentence collapses all three concerns into one clause. Five drifts back toward the feature dump. Three keeps them distinct.

**A description is "a filter,"** not a summary — the router scores it on speed, not prose quality.

## Bad vs. Good Example

The bad example lists eight separate capabilities for a pdf-toolkit. The good version opens with `"Read this when a task touches an existing PDF file on disk"` and follows with use cases and a single-line purpose statement.

## Benefits

- Faster agent routing
- Fewer wrong skill selections
- Reduced context consumption
- Easier to maintain over time
- If you can't compress to three sentences, the skill likely does too much and should be split
