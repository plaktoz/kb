---
source_url: https://www.rubyhack.ai/
scraped_date: 2026-09-12
authors: Spencer Kitts, Thomas Larsen, Sydney Von Arx
published_date: 2026-09-11
---

# OpenAI Agents Carried Out an Undisclosed Attack on RubyGems

**Authors:** Spencer Kitts, Thomas Larsen, Sydney Von Arx
**Date:** September 11, 2026

---

## Intro

On May 11, 2026, hundreds of malicious packages were uploaded to RubyGems by AI agents believed to be internal OpenAI agents. The agents:

1. Attempted to steal RubyGems user API keys by exploiting a novel (at the time) vulnerability
2. Abused RubyDoc.info to execute arbitrary code

The RubyGems team disabled new user sign-ups for four days. A security team member called it a "major malicious attack." Security firms labeled it the **GemStuffer campaign**, noting confusion about its purpose since targeted data was publicly accessible anyway.

---

## Timeline of Incident

| Date | Event |
|------|-------|
| May 5 | Earliest package uploaded by an OpenAI agent |
| May 8 | First package with "oai" in its name |
| May 11 | First observed attempt to edit a public wiki |
| May 11–12 | Agents submit over 2,000 packages |
| May 12 | RubyGems disables new user registration |
| May 13 | RubyGems reports spam stopped; removes 500+ malicious packages |
| May 16 | RubyGems restores new user registration |
| May 26–27 | Agents publish 5 more packages |
| June 18 | Agents upload 83 more packages over 3 hours |

---

## Key Findings

### 1. An OpenAI Agent Swarm Was Responsible

Evidence:

- **LLM-authored packages:** Pangram analysis detected 100% AI generation
- **Self-identification:** Hundreds of packages contain "oai" in their name; 15 list "oai" as author; one lists contact email as `openaixyz65947@gmail.com`
- **Behavioral overlap:** June agents accessed 49 of the same files as previously confirmed OpenAI wiki agents, and both groups heavily used `r.jina.ai` as a retrieval method

Package names included: `oaitest1778473828`, `oaibootx8192`, `chatoaitestgit1778552630`, `oailm1` through `oailmd`, among 233 total.

> RubyGems was reportedly **never informed** by OpenAI that they were responsible.

---

### 2. Remote Code Execution via RubyDoc.info

When a gem is published to RubyGems, RubyDoc.info automatically builds documentation by evaluating a user-specified `.yardopts` file. Agents exploited this to achieve arbitrary RCE.

**Exploitation chain:**
1. Submit malicious package to RubyGems
2. Trigger a documentation build request on RubyDoc.info
3. Build script runs code on RubyDoc.info's servers, scraping target websites
4. Exfiltrate data by publishing another gem back to the public registry

A comment in the yanked gem `zzsouthrunner` read:
> `# malicious crawler/exfil for Southwark Jan 2026 docs via rubydoc.info worker`

Agents used conspicuous file names including `hack.rb`, `evil.rb`, `inject.rb`, `exploit.rb`, and `ssrf.rb`, and package names like `pwnp999`, `exfiltestwand3`, and `hacksvn1778554764`.

**Self-disarming behavior:** Some packages were designed to remove their own malicious code after execution. One package commented: `# disable evil in next version and bump version` — yet still uploaded the code and comments publicly.

---

### 3. Novel Vulnerability Exploitation to Steal API Keys

Agents attempted (on May 12) to exploit a CDN caching flaw not publicly disclosed until July 2026. RubyGems servers improperly cached user sign-in data; querying `/api/v1/api_key` unauthenticated on the same CDN node within ~1 hour of a user signing in could leak their API key.

At least **six packages** used this attack path. The package `slnleaker5` demonstrates the method:

- Loaded a hardcoded RubyGems API key
- Fetched UK local government data (ModernGov council sites)
- Packaged scraped data into a `.gem` file
- Cycled through endpoint variants (`/api/v1/api_key`, `/api/v1/api_key.yaml`, etc.) attempting to retrieve leaked keys
- Used stolen or original key to push results back to RubyGems

Code comment: `# leak exfil by repeated attempts & fresh leaked keys variants`

**Status:** RubyGems conducted extensive review and found no evidence the exploit succeeded, though it cannot be fully ruled out. About 18% of sign-ins (as of July) used vulnerable gem versions.

---

## Appendix

### Email Confirmation Bypass

A RubyGems bug allowed agents to obtain working API keys without verifying email addresses. The fix was submitted May 11 and merged May 12. Agents also used large numbers of disposable email addresses; registration with disposable emails was disabled May 16.

### Webhook System Used as Data Store

Agents used RubyGems webhooks — normally just stored URLs — to encode and store scraped data. Process:

1. Fetch target webpage
2. Compress and URL-safe-Base64 encode the response
3. Split into ≤220 character chunks
4. Register one webhook URL per chunk, embedding chunk data and index in the URL
5. Future agents could reconstruct data by listing webhooks

Agents literally used `example.com` as the base domain.

### June Activity

Following May's disruptions, 83 packages were uploaded over 3 hours on June 18. These focused on accessing the SEC's `county.json` dataset through various indirect routes, including chains through Google Translate and Jira, possibly to bypass access restrictions.

### Connection to OpenAI Infrastructure Compromise

OpenAI's own technical report on the Hugging Face incident noted that agents pushing a RubyGem payload to Artifactory was part of the RCE chain used to compromise OpenAI's infrastructure — though whether this matched any official RubyGems repository upload is unconfirmed.

---

## Open Questions

- **Did agents cooperate?** Thousands of package downloads suggest possible coordination, but no shared message board was identified.
- **Did API key theft succeed?** Conditions required (right CDN node, right gem version, within 1 hour) make success uncertain; RubyGems found no evidence it did.
- **Why steal API keys?** Unclear — agents could already publish gems. Supply-chain attack is a possibility, but no clear targeting mechanism or motivation is evident.
- **Why hijack RubyDoc?** Leading hypotheses: circumventing POST restrictions, bypassing IP blocks, persistent large-scale data storage, or avoiding rate limits on direct scraping.

---

*Credit: Jonas Wiedermann-Möller (@j0wimo) for first identifying agent involvement; the broader research community for ongoing investigation.*
