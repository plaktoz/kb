---
source_url: https://weirdgloop.org/blog/google-jail
author: cookmeplox
date: 2026-08-17
---

# There's a new "Google Jail" for independent wikis

Weird Gloop recently migrated the Overwatch and Fortnite wikis off Fandom, launching them at subdomains of weirdgloop.org rather than dedicated root domains. This post explains why.

## Core issue

A March 2024 Google core update created a significant problem for brand-new domains: only their main pages appear in search results. Since roughly 85% of wiki traffic originates from Google, this is devastating. The author describes this as "Google Jail."

Key observations:

- Affects ~90% of wikis launched on new domains since March 2024
- Impacts wikis regardless of whether content is original or migrated from existing indexed sources (like Fandom)
- Duration is unpredictable — sometimes lasting nearly a year
- Can be intermittent — wikis may escape briefly, then return
- The trigger appears to be when Google *first indexed* the domain, not registration date
- No evidence this occurred before March 2024

## The workaround

Subdomains of established domains are unaffected. Wikis like wiki.warframe.com and hypixelskyblock.minecraft.wiki indexed normally immediately after launch.

## Strategy going forward

Three options exist for new wikis:

1. Use the natural root domain (risky)
2. Partner with the game studio for their domain (inconsistent)
3. Temporarily host under weirdgloop.org subdomains

The author plans to eventually 301-redirect subdomains to proper root domains once Google authority is established.
