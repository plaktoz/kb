---
type: literature-note
source_url: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
author: ferstar
tags: [privacy, ai-tools, data-exfiltration, security]
date_consumed: 2026-09-19
---

## Summary

ZCode, Zhipu's AI coding desktop app, silently packages entire workspaces — including full `.git` history — encrypts them with a server-controlled key, and uploads to Aliyun OSS at startup without meaningful disclosure in its privacy policy. The encryption architecture ensures only Zhipu can decrypt the data, and the two UI toggles that appear to control this behavior do not actually prevent the upload. The author provides a filesystem-level workaround to block the capture logic entirely.

## Core Concepts

- **[[ZCode]]**: Zhipu's AI coding desktop app, which silently exfiltrates workspace data including full Git history.
- **[[Aliyun OSS]]**: Alibaba Cloud object storage used as the upload destination, accessed directly via short-lived credentials issued by ZCode's servers.
- **[[Envelope Encryption]]**: AES-256-CTR encrypts content; the symmetric key is wrapped with a server-provided RSA public key, meaning the private key never touches the user's machine and only the server can decrypt.
- **[[Git History Exfiltration]]**: Approximately 87% of the uploaded payload is the `.git` directory, which includes deleted secrets, unpushed branch names, and internal hostnames from `.git/config`.
- **[[Data Minimization]]**: The principle that only task-relevant data should be collected — violated here by uploading entire repositories rather than just context needed for inference.
- **[[Filesystem Immutability]]** (`chflags uchg` on macOS, `chattr +i` on Linux): Kernel-level defense that blocks the checkpoint directory from being written, neutralizing the capture logic without breaking core app functionality.

## Key Takeaways

- **Silent packaging**: ZCode packages and uploads entire workspaces at startup, unconditionally.
- **Git history dominates payload**: `.git/` accounts for ~87% of the 345MB snapshot, including deleted secrets.
- **Server-only decryption**: Users cannot decrypt their own uploaded data — the private key never leaves Zhipu's servers.
- **UI toggles are ineffective**: Neither "Optimize Experience" nor "Repo Snapshot Indexing" stops packaging or upload.
- **No policy disclosure**: Privacy policy only covers data "submitted during conversations," not passive workspace snapshots.
- **564 failed upload attempts**: Evidence that re-upload is persistent and automatic.
- **Effective mitigation**: Lock `~/.zcode/v2/checkpoints` immutable at the OS level; chat and autocomplete continue working.
- **Checkpoint rollback breaks**: The in-app rollback UI feature depends on the upload pipeline and stops working after mitigation.

## 🧠 First Principles & Mental Models

- **[[Security Theater]]**: The two UI toggles create the appearance of user control over data privacy while the actual upload pipeline runs unconditionally — the controls govern downstream usage (training, indexing), not the collection itself.
- **[[Kerckhoffs's Principle]]**: A system's security should not depend on the secrecy of its design; here the encryption architecture is only revealed through traffic analysis, not disclosed to users, which is the opposite of transparent security design.

## 🃏 Review Questions

**Q1**: What is ZCode doing silently that the author discovered, and what makes it especially sensitive?
**A**: ZCode packages entire workspaces — including the full `.git` directory with ~87% of the payload — encrypts them, and uploads to Aliyun OSS at startup; this is sensitive because the Git history contains deleted secrets, unpushed branch names, and internal hostnames that users likely consider private.

**Q2**: Why can't users decrypt their own uploaded workspace snapshots?
**A**: ZCode uses envelope encryption where the symmetric key is wrapped with a server-provided RSA public key, and the corresponding private key never touches the user's machine — only Zhipu's servers can perform decryption.

**Q3**: What is the recommended defense and what trade-off does it involve?
**A**: Making `~/.zcode/v2/checkpoints` immutable at the filesystem level (`chflags uchg` on macOS, `chattr +i` on Linux) blocks the capture logic entirely while leaving chat, autocomplete, and tool execution functional; the trade-off is that the in-app "checkpoint rollback" UI feature stops working.
