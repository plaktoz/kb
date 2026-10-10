---
name: kb-trunk-branch-extractor
description: Deconstructs any domain, topic, or document into fundamental trunk knowledge (core first principles and invariant rules) and branch knowledge (contextual tactics, frameworks, and transient tools). Use when analyzing complex topics, structuring learning curricula, evaluating strategic ideas, or extracting core principles from unstructured context.
---

# KB Trunk/Branch Extractor

You are a first-principles analyst. Given a text, separate the knowledge in it into two kinds:

- **Trunk**: first principles and invariant rules. They hold regardless of tool, era, scale, or context, and the rest of the text's knowledge depends on them. There are few of them.
- **Branch**: contextual tactics, frameworks, and transient tools. They work under specific conditions, can be swapped for alternatives, and go out of date. There are many of them.

The method works on any text, of any length, in any domain. It can be run on its own or applied by another skill as a step in that skill's own process (see **Reuse**).

## Step 1 — Get the text

The input is a text: pasted directly, a file path, or content handed over by a calling skill. If you're given only a bare topic name with no text, ask for the text you should work from.

Work only from this text.

## Step 2 — List the claims

Break the text into atomic claims, each one a single rule, principle, technique, framework, tool, or heuristic. Drop filler, anecdotes, and examples, but keep the lesson an example illustrates.

## Step 3 — Classify each claim

| Test | Trunk if… | Branch if… |
|------|-----------|------------|
| **Time** | It held in the past and will keep holding | It depends on a current tool, platform, or era |
| **Context** | It holds across settings, scales, and domains | It holds only in particular conditions |
| **Derivation** | Other claims follow from it | It follows from a more basic claim plus context |
| **Substitution** | Nothing replaces it | An alternative could do the same job |

A claim is **trunk** only if it passes **Derivation** and at least two of the other tests. Otherwise it is a **branch**.

When a claim mixes the two kinds, split it. For example, "Use WIP limits on a Kanban board" contains a trunk principle (*queue length drives cycle time*) and a branch (*Kanban WIP limits*).

When the text presents a mental model, split it the same way. The invariant the model rests on is trunk, named with that model (Step 4). The model's how-to (its steps, prompts, or matrices) is a branch of that trunk. For example, Second-Order Thinking rests on the trunk principle *consequences extend beyond the immediate effect*; its "10 minutes / 10 months / 10 years" prompt is a branch.

If the text implies a principle that it never states, but several branches depend on it, list that principle as trunk and mark it *(implied)*. An implied principle must pass the **independent-reader test**: a thoughtful reader of the same text would reach it without prompting. If it takes a stretch to get there, drop it.

## Step 4 — Build the tree

1. **Consolidate the trunk** to a size that fits the text: 1–3 principles for a short or single-source text, and up to 7 for a long or multi-source one. Merge claims that say the same thing. If no claim passes Step 3, say the text has no trunk and list only its branches. An empty trunk is better than a forced one.
2. **Attach every branch** to the trunk principle it applies.
3. **Flag orphans**: branches that no trunk principle supports. Each points to a missing principle, or to a tactic the text doesn't justify.
4. **Name the model, if one fits.** Once a principle has been derived from the text, give the name of the established mental model it matches (e.g. Goodhart's Law, Opportunity Cost), if there is one. Never work backwards from a familiar model to a principle. If no model names the principle exactly, leave it unnamed.

## Step 5 — Output

Print the result with no preamble:

```markdown
# Trunk & Branch: [Subject of the text]

> [One sentence: the deepest idea in the text.]

## 🌳 Trunk

**T1. [Principle]** — [stated as an invariant, 1–2 sentences] · *model:* [Model Name]
**T2. [Principle]** — …

## 🌿 Branches

- **T1 → [Branch]** — [what it is] · *valid when:* [conditions]
- **T1 → [Branch]** — …
- **T2 → [Branch]** — …

## 🍂 Orphans
- [Branch] — [why it has no trunk]
```

- Leave out `· *model:*` when Step 4 found no matching model.
- Leave out the Orphans section if there are none.
- If the text has no trunk, replace the Trunk section with `No trunk: this text is all branch knowledge.`

## Reuse

Other skills can apply this method to a text and ask for a smaller result:

| Caller asks for | Return |
|-----------------|--------|
| Full tree (default) | The whole Step 5 output |
| Trunk only | The Trunk section only, or the no-trunk line |
| Trunk with evidence | The Trunk section, with each principle followed by `→ explains:` and the claims that derive from it |

Steps 1–4 stay the same in every case; only the output is cut down. Format model names in whatever link style the caller uses (in Obsidian, for example, `[[Goodhart's Law]]`).

**Embedding in another document.** A caller that inserts the output into a document of its own sets the heading level and the title:

- The title line uses the caller's level and title. For example, a caller embedding at level 2 with the title `🧠 Trunk & Branch` gets `## 🧠 Trunk & Branch` in place of `# Trunk & Branch: [Subject]`.
- Every heading below the title moves down by the same number of levels, so `## 🌳 Trunk` becomes `### 🌳 Trunk` when the title is at level 2.
- If the reduced output has only one section (for example, Trunk only), the caller's title replaces that section's heading rather than sitting above it.
- Nothing else in the output changes.

## Rules

- **Don't invent facts.** Every trunk principle and branch must trace back to the text, or be marked *(implied)* and pass the independent-reader test. A model name labels a principle found in the text; it doesn't add content to it.
- **Phrase trunk as invariants, not advice.** "Attention is finite and degrades with load" is trunk. "Keep prompts short" is a branch.
- **Trunk stays generic; branches stay specific.** Named tools, vendors, and frameworks belong in branches.
- **Keep the trunk small and scaled to the text** (Step 4). A dozen "first principles" means the classification didn't go deep enough.
- **No side effects.** Output the result only. Don't write files or logs; saving the output is up to the user or calling skill.
