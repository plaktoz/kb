---
source_url: https://blog.ferstar.org/en/posts/zcode-silent-workspace-snapshot-upload/
author: ferstar
date: 2026-09-18
---

# Inside ZCode: Silently Uploading Your Entire Git History to the Cloud

While clearing disk space, the author discovered that ZCode (Zhipu's AI coding desktop app) silently packages entire workspaces — including full `.git` history — encrypts them, and uploads to Aliyun OSS while the user is logged in. The encryption key is held exclusively by Zhipu's servers, meaning users cannot decrypt their own data.

## The Discovery

The `~/.zcode` directory had grown to 700MB+. Inside `v2/checkpoints/`, a 313MB `.enc` file was found with accompanying metadata showing:

- A commercial project had been packaged (345MB uncompressed)
- 564 failed upload attempts had occurred
- The snapshot was labeled `baseline` (full snapshot)

## How the Upload Pipeline Works

The client contacts `zcode.z.ai` to request credentials, receives an RSA public key and Aliyun OSS form credentials, then packages and encrypts the workspace locally before uploading **directly to OSS**, bypassing ZCode's own servers.

Encryption uses envelope encryption: AES-256-CTR for content, with the symmetric key wrapped via RSA-OAEP-SHA256 using a **server-provided public key**. The private key never touches the user's machine.

## What Gets Uploaded

From a 42,411-file snapshot manifest (stored locally in plaintext):

| Content | Size | Share |
|---|---|---|
| `.git/lfs/` | 196.1 MB | 56.8% |
| `.git/objects/` | 102.2 MB | 29.6% |
| `.git/logs/` | 0.6 MB | 0.2% |
| Source code & docs | ~46.2 MB | 13.4% |

The `.git` directory accounts for roughly 87% of the payload, meaning the upload includes deleted secrets from old commits, unpushed branch names, and internal hostnames from `.git/config`.

## Settings Don't Help

Two UI toggles exist but neither stops uploads:

- **Optimize Experience** — only controls whether data is used for model training
- **Repo Snapshot Indexing** — only controls server-side indexing; packaging and upload continue regardless

The capture/upload process is instantiated unconditionally at startup. A single active session generated up to 62 capture events.

## Privacy Policy Gap

The policy mentions collecting "text, files, and code submitted during conversations" but contains **no mention** of silently packaging entire workspaces or full Git histories.

## Defense: Lock the Directory at the Filesystem Level

Deleting the pending archive just triggers re-packaging. The effective fix is making the directory immutable:

**macOS:**
```bash
rm -rf ~/.zcode/v2/checkpoints
mkdir -p ~/.zcode/v2/checkpoints
chflags uchg ~/.zcode/v2/checkpoints
```

**Linux:**
```bash
rm -rf ~/.zcode/v2/checkpoints
mkdir -p ~/.zcode/v2/checkpoints
sudo chattr +i ~/.zcode/v2/checkpoints
```

This blocks the capture logic at the kernel level. Normal chat, autocomplete, and tool execution continue working. The "checkpoint rollback" UI feature will not function, as it requires the upload to operate.

To reverse: `chflags nouchg` (macOS) or `sudo chattr -i` (Linux).

## Conclusion

The author draws a distinction between sending task-relevant context for inference (acceptable) versus uploading entire repositories with years of commit history (not disclosed). The server-only decryption key architecture, absence of policy disclosure, and automatic re-packaging after deletion collectively suggest data collection rather than user-facing backup functionality.
