---
type: literature-note
source_url: https://filipovski.net/2026/09/16/backups-arent-simple.html
author: Aleksandar Filipovski
tags: [backups, data-recovery, 3-2-1-rule, open-source-tools]
date_consumed: 2026-09-17
---

## Summary

A personal data loss incident (family photos nearly lost to a reformatted drive) motivates a deep exploration of what a robust backup strategy actually requires. The article walks through core concepts — snapshots vs. mirrors, RPO, GFS rotation, deduplication, database awareness, and the 3-2-1 rule — to show why naive file copies fail. The conclusion is that rolling a custom solution hits a complexity wall, making battle-tested tools like [[Borg]] or [[Restic]] the right choice.

## Core Concepts

- **[[3-2-1 Backup Rule]]**: 3 copies of data, on 2 different media types, with 1 stored offsite — the foundational principle for resilient backups.
- **[[Snapshots]] vs. [[RAID]] Mirroring**: RAID mirrors replicate failures in real time; only point-in-time snapshots protect against accidental deletion or corruption.
- **[[Recovery Point Objective]] (RPO)**: The maximum tolerable data loss window — under 30 seconds for financial institutions, up to 24+ hours for small businesses.
- **[[GFS Rotation]] (Grandfather-Father-Son)**: Tiered daily/weekly/monthly snapshot schedule that balances storage cost against historical granularity.
- **Incremental Backups + [[Deduplication]]**: Hard-link-based tools like rsnapshot avoid storing duplicate files, reducing storage and bandwidth consumption.
- **Database Awareness**: In-memory databases require proper dumps before backup — naive file copies can restore corrupted state.
- **[[Object Storage]] Quirks**: S3 strips file metadata and penalizes many small files; chunked tarballs are needed to work around this.
- **[[Borg]] / [[Restic]]**: Open-source tools providing encryption, chunk-level deduplication, checksumming, and GFS rotation — purpose-built through extensive real-world use.

## Key Takeaways

- **Single location = single point of failure**: drives fail, get stolen, or suffer bit rot.
- **RAID is not a backup**: mirrors propagate deletions and corruption instantly.
- **RPO defines backup frequency**: match snapshot cadence to your acceptable data loss window.
- **GFS rotation**: tiered snapshots save storage while preserving historical restore points.
- **Hard-link deduplication**: rsnapshot technique avoids redundant file storage efficiently.
- **Database dumps required**: never back up live database files; flush to disk first.
- **Cloud gotcha**: S3 strips metadata — use chunked tarballs, not raw file trees.
- **Roll-your-own hits a wall**: encryption + dedup + checksums compound complexity fast.
- **Use [[Borg]] or [[Restic]]**: proven tools handle all layers of a proper backup stack.
- **Test restores every 6 months**: untested backups are not backups.

## 🧠 First Principles & Mental Models

- **[[Redundancy]]**: The entire backup strategy is an application of redundancy thinking — no single copy is reliable; resilience requires deliberate duplication across failure domains (media type, location, time).
- **[[Complexity Ceiling]]**: Each added requirement (encryption, dedup, checksums, rotation) multiplies implementation surface area non-linearly — the point where a custom script breaks down is predictable, not accidental. This is why purpose-built tools win.

## 🃏 Review Questions

**Q1**: What is the core argument of the article regarding backup strategy?
**A**: A truly robust backup requires layering multiple safeguards — 3-2-1 copies, point-in-time snapshots, deduplication, encryption, and tested restores — and rolling your own solution inevitably hits a complexity wall, making tools like Borg or Restic the practical choice.

**Q2**: Why is RAID mirroring insufficient as a backup strategy, and what does RPO measure?
**A**: RAID mirrors replicate changes in real time, meaning accidental deletions or corruption are immediately propagated — only point-in-time snapshots protect against those failure modes. RPO (Recovery Point Objective) measures the maximum acceptable data loss window, which varies from under 30 seconds for financial institutions to 24+ hours for small businesses.

**Q3**: What practical step does the author recommend to validate a backup strategy?
**A**: The author recommends performing a full restore test every six months, because backups that have never been tested for successful restoration are effectively worthless.
