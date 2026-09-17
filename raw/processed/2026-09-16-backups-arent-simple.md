---
source_url: https://filipovski.net/2026/09/16/backups-arent-simple.html
author: Aleksandar Filipovski
date: 2026-09-16
---

# Backups Aren't Simple

The article traces the evolution of a robust backup strategy, starting from a personal story about family photos lost when a hard drive was reformatted for a TV set-top box — recoverable only by luck.

## Key Concepts

- **Basic backup principle:** Never keep important data in a single location. Drives fail, get stolen, or suffer bit rot.
- **Snapshots vs. mirrors:** RAID 1 mirroring won't help if you accidentally delete or corrupt files — you need point-in-time snapshots.
- **RPO (Recovery Point Objective):** How much data loss is acceptable? Ranges from under 30 seconds for financial institutions to 24+ hours for small businesses.
- **GFS rotation:** Daily/weekly/monthly snapshot tiers balance storage cost against historical granularity.
- **Incremental + deduplication:** Using hard links (as in rsnapshot) avoids storing duplicate files, saving both storage and bandwidth.
- **Database awareness:** In-memory database flushing means naive file copies can restore corrupted data — dumps are necessary.
- **3-2-1 rule:** 3 copies, on 2 media types, with 1 offsite.
- **Cloud storage quirks:** Object storage like S3 strips file metadata and penalizes many small files, requiring chunked tarballs.
- **The conclusion:** Rolling your own solution hits a complexity wall. Tools like **Borg** or **Restic** handle encryption, chunk-level deduplication, and checksums — built through extensive real-world testing.

## Final Recommendation

The author advocates using proven open-source tools rather than custom scripts, and emphasizes that backups are worthless without regularly tested restores — suggesting a restore test every six months.

> "encrypted, chunk-level deduplicated, GFS-rotated, point-in-time archived, cloud, 3-2-1 backup solution"
