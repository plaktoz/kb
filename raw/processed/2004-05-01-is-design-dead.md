---
source_url: https://martinfowler.com/articles/designDead.html
author: Martin Fowler
date: 2004-05-01
---

# Is Design Dead?

## Summary

Fowler argues that XP doesn't kill design — it transforms it. Rather than "Big Up Front Design," XP enables **evolutionary design** through enabling practices.

## Core Argument

Two design philosophies exist:

- **Planned Design** — think ahead, hand off blueprints to builders
- **Evolutionary Design** — design emerges during implementation

Evolutionary design traditionally fails due to entropy and ad-hoc decisions. XP changes this by flattening the cost-of-change curve through:

- **Testing**
- **Continuous Integration**
- **Refactoring**

## Key Principles

**Simplicity (YAGNI):** Don't build flexibility you don't yet need. Complexity added prematurely makes future changes harder in all directions *except* the one anticipated.

Kent's four criteria for a simple system (most important first):
1. Runs all the Tests
2. No duplication
3. Reveals intention
4. Fewest classes/methods

**Patterns:** Still vital. XP changes *when* you apply them — evolve into patterns gradually rather than front-loading them.

**Architecture:** A "broad starting point" is reasonable, but treat early decisions as revisable. "When in doubt err on the side of simplicity."

**UML:** Useful for communication, not comprehensiveness. Diagrams are most valuable as temporary thinking tools, not permanent artifacts.

**Reversibility:** Reduce irreversible decisions. Defer or structure choices so they can be undone cheaply.

**The Will to Design:** Someone on the team must actively maintain design quality. Without this human commitment, evolutionary design collapses.

## Skills XP Design Demands

- Desire to keep code simple
- Confident refactoring
- Pattern knowledge (when *and* how to apply them)
- Anticipating future change
- Communicating design through code, diagrams, and conversation

## Conclusion

Design is not dead — its nature has changed. XP makes evolutionary design a viable strategy again, demanding *more* skill from designers, not less.
