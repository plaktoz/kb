---
source_url: https://www.usetranscribe.io/yt/eUiavoft3EA/unicorn-security?format=md
author: Bendik Schartum Thorbjørnsen & Karim El-Melhaoui
date: 2026-08-17
---

# Chasing Unicorns: A Lovable Security Story

**Creator:** NDC Conferences
**Platform:** YouTube
**Duration:** 9m
**Source:** https://www.youtube.com/watch?v=eUiavoft3EA

## Summary

The presentation discusses the security vulnerabilities associated with rapidly growing unicorn startups, particularly in the context of cloud security and misconfigurations. The speakers highlight a specific case of a misconfiguration in a SaaS application that allowed unauthorized access due to improper validation of user claims, emphasizing the need for robust security measures even in fast-paced development environments.

- Unicorn startups often prioritize rapid growth over security, leading to potential vulnerabilities.
- Misconfigurations, such as those found in OAuth implementations, can have severe consequences despite the companies' high valuations.
- The "move fast and break things" mentality has evolved into a "vibe coding" approach, where security measures may be overlooked.
- A specific case study involved a misconfiguration in a SaaS application that allowed users to spoof email claims, leading to unauthorized access.
- Security assessments for new AI services are often bypassed due to fear of missing out on technological advancements.
- Recommendations include avoiding reliance on email claims for authorization and implementing thorough validation processes.
- Companies should verify claims against multiple sources to enhance security and prevent exploitation.
- The ongoing research aims to explore the security implications of rapid development practices in unicorn startups.

## Section Insights

### Introduction to Unicorns and Security Challenges

Unicorns refer to privately owned startup companies valued at over 1 billion USD. These companies often prioritize rapid growth over security, leading to potential vulnerabilities. Minor misconfigurations can have significant consequences.

### The Evolution of Engineering Practices

The engineering approach has shifted from "move fast and break things" to "move fast and fix things", and now to a "vibe coding" approach, which can neglect security. B2B customers still expect robust security despite rapid development.

### Understanding Misconfigurations in SaaS Applications

Misconfigurations, particularly in identity claims, can lead to severe vulnerabilities, allowing unauthorized access to applications. Mutable claims (such as the user.mail attribute in Microsoft Entra ID) can be exploited because they are unverified and changeable without domain ownership proof.

### Exploiting Misconfigurations in Unicorns

By setting up federation and spoofing email domains, attackers can gain unauthorized access to internal systems of unicorn companies. In one case, by pretending to be the founder at unicornat.ai, the researcher was able to access their internal tenant — and then by spoofing the admin account, gained access to all enterprise customers including a large portion of the Fortune 500.

### Consequences of AI Hype on Security Assessments

The urgency to adopt AI technologies often leads organizations to bypass thorough security assessments, resulting in significant vulnerabilities. When every team in the organization demands an AI service, normal security onboarding processes are skipped due to FOMO.

## Transcript

Welcome to this presentation. We're going to talk about chasing unicorns. Lovable security story. First of all, I'm Karim El Mohamadi from O3 Cyber. I do cloud and platform security. And with me I have my colleague Bendik, also from O3 Cyber.

Just a disclaimer — this is not about real unicorns, but in our case it's companies that are startup companies valued at over 1 billion USD, privately owned and not listed on the share market.

These companies are growing at an extreme speed. In cloud security, speed is the enemy of security. Our research showcases how billion-dollar valuations don't necessarily mean you're secure, and how minor misconfigurations don't necessarily have minor consequences.

In hypergrowth markets, security is not the number one priority — capturing the market is. The evolution of engineering went from "move fast and break things" (Facebook), to "move fast and fix things," to the current "vibe coding" era (2025). In vibe coding, the only security measure might be calling another AI agent to run security checks, or adding security notes to MD files. The AI hype train keeps going, but B2B customers still demand the security they always had. FOMO wins and security processes get skipped.

Our talk touches upon SSO and is based on "NoAuth" — a misconfiguration discovered by Omer in D Scope in 2023. This was a wide OIDC misconfiguration, not a flaw in the underlying protocols, but in how they're used. The general idea: a SaaS where mutable claims are being used to identify and map users. A very good example is Microsoft Entra ID — the `user.mail` attribute is mutable, so you can change the email to whatever domain without verifying you own that domain.

We looked at applications where you can sign up with Microsoft and are granted access to a tenant. If you change your email from o3c.nl to any other email, in some cases you get straight into the application. We looked further at more advanced workflows — federation via SAML/OIDC — and systematically looked for applications where we could set up federation.

We provisioned a tenant, configured federation as "actor@customerx.com," then issued a token through our identity provider passed to the relying party. Many SaaS applications returned "email is not verified in your tenant" — they require adding the email domain to allowed domains, which requires a DNS record. So the vulnerability existed but was technically unexploitable.

But what if we tried to spoof the company themselves? We hypothesized they might have hardcoded their own domain in the backend. In one case, by pretending to be the founder at unicornat.ai, we were able to get into their tenant. From their internal tenant, we found another user account "admin@unicorn.ai." Spoofing that account gave access to all their enterprise customers — a large portion of the Fortune 500.

The AI hype explains how we got past security teams: when every team demands an AI service, Fortune 500 companies skip their normal security assessments due to FOMO. The result: access to unreleased product designs from some of the coolest tech companies in the world.

## Lessons Learned

1. **Never use the email claim for authorization** — it can be spoofed by anyone.
2. **Validate claims thoroughly** — don't just check for a verified domain, as that could be bypassed by chaining vulnerabilities. Validate the tenant, subject, and actor.
3. **Trust more than one source** — use multiple verification mechanisms.
4. Microsoft is working on passing a claim showing whether the domain has been verified by them, which helps trusting email claims.

The rhetorical question: are the fastest unicorns and vibe coding platforms mostly vibe coded? The speakers' continued research aims to answer this.
