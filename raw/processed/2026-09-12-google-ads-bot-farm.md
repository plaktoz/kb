---
title: "I spent $220 on Google app ads. 60% of the installs were robots."
source_url: "https://dayzlegame.com/blog/google-ads-bot-farm/"
date: "2026-09-11"
author: "Nick Abe"
---

# I Spent $220 on Google App Ads. 60% of the Installs Were Robots.

**Author:** Nick Abe
**Date:** September 11, 2026

## Summary

Nick Abe, developer of a small puzzle app called Dayzle, ran a Google Ads campaign for Android at CA$40/day targeting installs. After removing the target CPA, Google spent CA$80 in one day and claimed 21 installs — but the admin panel showed only 1.

## What Happened

Digging into raw analytics revealed 21 new Android devices that day. Twenty of them ran an app version the Play Store had stopped serving, meaning they sideloaded it from elsewhere — yet each reported Google Play as the installer. Every device opened the app once, spent zero seconds on any screen, and never returned.

Over the full two-week campaign:
- **56 installs billed**
- **33** showed bot-like behavior
- **7** came from countries outside the campaign's targeting
- **13** were real people, who collectively finished 92 games

## How the Bot Farm Worked

The suspected farm would watch the shortest ad video without clicking, then install from a saved APK rather than the store — faster, and less likely to trigger Play Store detection. Because Google counted a view + install as a conversion, the farm's activity *improved* the campaign's apparent performance, causing Google's algorithm to send more ads to the farm. A self-reinforcing loop.

## What Changed

Abe submitted an invalid-traffic refund request to Google and changed the campaign goal from "opened the app" to **"won a puzzle"** — reasoning that scripting a Sudoku solve is meaningfully harder than scripting an app open, making Dayzle a more expensive target than comparable apps.

## Takeaway

> "if you're relying on Google's install count for your ads, it's a real number, but it's definitely worth digging into."
