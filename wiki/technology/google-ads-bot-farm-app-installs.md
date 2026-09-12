---
type: literature-note
source_url: https://dayzlegame.com/blog/google-ads-bot-farm/
author: Nick Abe
tags: [google-ads, ad-fraud, bot-farm, mobile-marketing]
date_consumed: 2026-09-12
---

## Summary

Nick Abe, indie developer of a puzzle app, ran a CA$40/day Google Ads campaign for Android installs and found that 60% of billed conversions were bot-driven — devices that installed from a saved APK rather than the Play Store, opened the app once with zero engagement, and never returned. The fraud loop was self-reinforcing: bot activity improved apparent campaign performance, causing Google's algorithm to serve more ads to the farm.

## Core Concepts

- **[[Google App Ads]]** — install-campaign product where billing is triggered by a conversion event (e.g. app open, in-app action)
- **[[Bot Farm]]** — coordinated network of devices that simulate user behavior to generate fraudulent ad conversions
- **[[Invalid Traffic (IVT)]]** — industry term for non-human ad interactions; Google offers a refund process for verified IVT
- **[[APK Sideloading]]** — installing Android apps from outside the Play Store; used here to avoid Play Store detection while still reporting the store as the installer
- **[[Conversion Goal Hardening]]** — raising the bar for what counts as a conversion to make fraud economically unviable (e.g. switching from "app open" to "completed puzzle")
- **[[Feedback Loop]]** — bots improve campaign metrics → algorithm rewards them with more impressions → bots receive more budget

## Key Takeaways

- **Campaign spend**: CA$220 over two weeks; 56 installs billed, only 13 real users.
- **Bot signature**: one app open, zero seconds on any screen, old app version not on Play Store.
- **Self-reinforcing fraud**: bots boosted apparent CTR/CVR, directing more spend toward them.
- **Detection method**: cross-referencing raw device analytics against admin panel install count.
- **Mitigation**: changed conversion goal to "won a puzzle" — harder to script than an app open.
- **Refund path**: Google's invalid-traffic refund request form is available after the fact.
- **Targeting anomaly**: 7 installs came from countries explicitly excluded from the campaign.

## 🧠 First Principles & Mental Models

- **[[Goodhart's Law]]**: Once "install count" becomes the optimized metric, actors game it via fake installs — the number rises while the underlying signal (genuine user interest) collapses.
- **[[Perverse Incentive]]**: Google's algorithm optimizes for conversions regardless of quality, so fraud that inflates conversion numbers is inadvertently rewarded with more ad spend — the platform's incentive structure works against the advertiser.

## 🃏 Review Questions

**Q1**: What was the core finding of Nick Abe's Google Ads experiment?
**A**: 60% of billed installs (33 of 56) showed bot-like behavior — one open, zero engagement, sideloaded from a saved APK — meaning only 13 installs were real users.

**Q2**: How did the bot farm avoid Play Store detection while still registering as a valid conversion?
**A**: Bots installed from a pre-saved APK rather than the live Play Store listing, bypassing store-side checks, but reported Google Play as the installer so Google counted it as a valid install conversion.

**Q3**: What practical step can indie developers take to harden their campaigns against this type of fraud?
**A**: Switch the conversion goal from a trivial action (app open) to a meaningful in-app event (e.g., completing a puzzle), raising the scripting cost high enough that the farm targets cheaper apps instead.
