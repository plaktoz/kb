---
type: literature-note
source_url: https://mcpherrin.ca/2026/09/07/rsa.html
author: Matthew McPherrin
tags: [cryptography, rsa, pki, web-security]
date_consumed: 2026-09-08
---

## Summary

Matthew McPherrin investigated early [[Web PKI]] security by hunting for dangerously small [[RSA]] keys in archived 1990s browser installers. He discovered two 512-bit RSA root certificates from a defunct Canadian [[Certificate Authority]] called **E-Certify**, shipped with Netscape 4.51 in 1999, and fully factored both private keys using the open-source [[CADO-NFS]] number field sieve on commodity hardware. He then demonstrated the recovered keys by issuing valid certificates trusted by Netscape 4.51, proving real-world exploitability of legacy PKI roots.

## Core Concepts

- **[[RSA Key Factoring]]**: Breaking RSA by factoring the public modulus into its prime components, yielding the private key. Feasible for small key sizes (512-bit and below).
- **[[Web PKI]] / Root Certificates**: Browser trust stores ship pre-loaded CA certificates; any key recoverable from those roots could sign fraudulent certificates trusted by that browser.
- **[[CADO-NFS]]**: Open-source C implementation of the Number Field Sieve algorithm used to factor large integers; ran on a Ryzen 9 5950X.
- **[[E-Certify]]**: Defunct Canadian CA whose 512-bit SSL and S/MIME root certificates were shipped in Netscape 4.51 (March 1999).
- **[[Number Field Sieve (NFS)]]**: The most efficient known algorithm for factoring integers above a certain size; sub-exponential time complexity.
- **[[Certificate Authority (CA)]]**: Entity whose root key is embedded in browsers; compromise of the root key breaks the entire trust chain for that CA.

## Key Takeaways

- **512-bit RSA roots existed in 1999**: Netscape 4.51 shipped with E-Certify's 512-bit roots, far below modern minimums.
- **Factor time on commodity hardware**: SSL root factored in ~32 hours, S/MIME root in ~29 hours on a single Ryzen 9 CPU.
- **GPU acceleration helps**: A 512-bit VeriSign test code-signing CA from IE 3.02 was factored in ~1 hour using a GPU cluster (Steve Weis).
- **Private keys fully recovered**: Both E-Certify roots had their private keys reconstructed and published.
- **Live demo built**: A Go-based TLS server at `e-certify.fly.dev` issues certs valid under Netscape 4.51, proving the exploit end-to-end.
- **Archive.org as a research tool**: Old browser installers preserved on archive.org enabled retroactive security archaeology.
- **Modern browsers unaffected**: No contemporary browser trusts these ancient roots — risk is historical/educational.

## 🧠 First Principles & Mental Models

- **[[Security Debt]]**: Weak cryptographic parameters chosen under 1990s computational constraints became exploitable liabilities decades later — legacy trust anchors never cleaned from browser distributions accumulate compounding risk.
- **[[Threat Modeling Over Time]]**: What is computationally infeasible today may become trivially feasible as hardware improves; security assumptions must be re-evaluated against future adversaries, not just present ones.

## 🃏 Review Questions

**Q1**: What was McPherrin's core finding about early Web PKI security?
**A**: He discovered that Netscape 4.51 (1999) shipped with two 512-bit RSA root certificates from the defunct Canadian CA E-Certify, which he fully factored on a modern consumer CPU — recovering the private keys and proving the roots were exploitable.

**Q2**: How long did it take to factor the 512-bit RSA keys, and what tool was used?
**A**: The SSL root was factored in approximately 32 hours and the S/MIME root in ~29 hours using CADO-NFS on a Ryzen 9 5950X; a VeriSign 512-bit test CA from IE 3.02 was factored in ~1 hour on a GPU cluster.

**Q3**: What is the practical implication of recovering a CA's private key?
**A**: An attacker holding the CA private key can issue arbitrary certificates that any browser trusting that root will accept as valid — enabling man-in-the-middle attacks or silent code signing against clients still using the affected software.
