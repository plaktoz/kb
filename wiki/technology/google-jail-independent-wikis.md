---
type: literature-note
source_url: https://weirdgloop.org/blog/google-jail
author: cookmeplox
tags: [seo, google, wiki, search-ranking]
date_consumed: 2026-09-09
---

## Summary

A March 2024 [[Google]] core update introduced what wiki operators call "Google Jail" — a penalty where new domains are limited to only their main page appearing in search results. Since roughly 85% of wiki traffic comes from Google, this is devastating for independent wikis migrating off [[Fandom]]. Weird Gloop found that hosting wikis as subdomains of an established domain bypasses the penalty entirely.

## Core Concepts

- **[[Google Core Update]] (March 2024)**: Triggered a new indexing behavior where brand-new domains are severely restricted in search visibility.
- **Google Jail**: Informal term for the condition where only a domain's main page indexes, effectively making all inner pages invisible in search.
- **[[Fandom]] Migration**: Wikis like Overwatch and Fortnite wikis sought to move off Fandom to gain editorial independence, but faced this SEO barrier.
- **Subdomain Strategy**: Established domains like `weirdgloop.org` act as domain authority sponsors — subdomains inherit the parent's trust and index normally.
- **301 Redirect Plan**: The intended long-term path is to earn authority on subdomains, then redirect to proper root domains once Google trust is established.

## Key Takeaways

- **Scope**: ~90% of wikis launched on new domains since March 2024 are affected.
- **Trigger**: When Google *first indexed* the domain matters, not the registration date.
- **Duration**: Unpredictable — some wikis stay jailed for nearly a year; exits can be intermittent.
- **Content Irrelevance**: Even migrated content from already-indexed sources (Fandom) does not help.
- **Proven Workaround**: Subdomains of established domains (e.g. `wiki.warframe.com`, `hypixelskyblock.minecraft.wiki`) index normally at launch.
- **Three Strategies**: Use root domain (risky), partner with a game studio domain (inconsistent), or use established subdomain (recommended).

## 🧠 First Principles & Mental Models

- **[[Authority Inheritance]]**: Domain authority in SEO is not purely content-based — trust signals propagate from parent to subdomain, meaning structural provenance matters as much as content quality. This explains why a new domain with excellent migrated content still fails while a subdomain of a trusted host succeeds instantly.
- **[[Chilling Effect]]**: Google Jail doesn't just penalize current wikis — the unpredictability and duration create a structural deterrent against any new independent wiki projects, effectively entrenching Fandom's incumbency.

## 🃏 Review Questions

**Q1**: What is "Google Jail" and why is it so harmful for wikis?
**A**: It is a post-March 2024 Google behavior where only a new domain's main page appears in search results. Since ~85% of wiki traffic comes from Google, this effectively starves the rest of the wiki of visitors.

**Q2**: What triggers Google Jail, and does having quality or migrated content help?
**A**: The trigger is when Google first indexes the domain — not the registration date. Content quality or provenance (even content migrated from already-indexed Fandom pages) has no effect on escaping it.

**Q3**: How has Weird Gloop worked around Google Jail for new wiki migrations?
**A**: By hosting new wikis as subdomains of the established `weirdgloop.org` domain, which inherits the parent's trust and indexes normally, with a plan to 301-redirect to root domains once authority is built.
