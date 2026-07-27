---
type: literature-note
source_url: https://cheatsheetseries.owasp.org/cheatsheets/Java_Security_Cheat_Sheet.html
author: OWASP
tags: [java, security, owasp, injection-prevention]
date_consumed: 2026-07-27
---

## Summary

The OWASP Java Security Cheat Sheet provides concrete, code-level guidance for preventing the most critical Java application vulnerabilities: injection attacks (SQL, JPA, OS, XPath, HTML/XSS, NoSQL, Log), and weak cryptography. Each section identifies the vulnerability symptom, prescribes the prevention mechanism, and provides working Java code examples. The preferred cryptography library is Google Tink; JCA/JCE is a fallback requiring expert review.

## Core Concepts

- **[[SQL Injection]]**: Never build SQL from user input strings; use `PreparedStatement` with `?` placeholders and `setString()`/`setInt()` binding.
- **[[JPA Injection]]**: Use JPQL named parameters (`:colorName`) via `setParameter()` — never string-concatenate JPQL queries.
- **[[OS Command Injection]]**: Use Java API methods (e.g., `InetAddress.isReachable()`) instead of building shell command strings from user input.
- **[[XPath Injection]]**: Use `XPathVariableResolver` to parameterize XPath expressions.
- **[[XSS Prevention]]**: Combine strict allowlist input validation with OWASP Java HTML Sanitizer (output sanitizing) + OWASP Java Encoder (HTML escaping).
- **[[Log Injection]]**: Use parameterized logging (`logger.warn("User {}", username)`) — never string-concatenate user data into log messages.
- **[[Google Tink]]**: Google's high-level cryptography library; recommended over raw JCA/JCE; provides safe AES-GCM and ECDH hybrid encryption APIs.
- **[[AES-GCM]]**: Recommended symmetric encryption algorithm; requires 256-bit key, unique 96-bit nonce per operation, 128-bit authentication tag.
- **[[ECDH]]** (Elliptic Curve Diffie-Hellman): Key agreement protocol for hybrid encryption between parties; use `secp256r1` curve; regenerate key pairs periodically.
- **[[OWASP Top 10]]**: The standard awareness document for web application security risks; injection is consistently a top-ranked vulnerability.

## Key Takeaways

- Use `PreparedStatement` for all SQL — no exceptions.
- Use JPQL named parameters for JPA queries — never `createQuery("... = '" + input + "'"`)`.
- Never build OS commands as strings — call the Java API equivalent.
- Validate input with allowlist regex first; sanitize + escape output with OWASP libraries.
- Structured JSON logging (Log4j `JsonTemplateLayout`, Logback `JsonEncoder`) prevents log injection by default.
- Never use JCA/JCE directly for encryption without cryptography expert review — use Google Tink.
- AES-GCM: 256-bit key + unique 96-bit nonce per operation — nonce reuse breaks confidentiality.
- ECDH key pairs should be regenerated periodically to limit exposure from a compromised shared secret.
- Log injection is underrated — structured logging at the infrastructure level is the cleanest mitigation.

## 🧠 First Principles & Mental Models

- **[[Defense in Depth]]**: The cheat sheet implicitly demonstrates defense in depth — input validation + output encoding + parameterized queries all address the same root cause (untrusted data in structured contexts) from multiple angles, so that a failure in one layer doesn't lead to a vulnerability.
- **[[Principle of Least Privilege]]**: Restricting access to internal JDK APIs (JEP 403) and using library-level encryption abstractions (Tink over JCA/JCE) both express the principle — expose the minimum API surface needed, reduce the attack surface by narrowing what can go wrong.
