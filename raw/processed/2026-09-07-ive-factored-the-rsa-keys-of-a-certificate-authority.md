---
source_url: https://mcpherrin.ca/2026/09/07/rsa.html
author: Matthew McPherrin
date: 2026-09-07
---

# I've factored the RSA keys of a Certificate Authority…

McPherrin investigated early Web PKI security by hunting for factorably small RSA keys in archived Netscape and Internet Explorer installers. He notes that RSA-260 (862-bit) was recently factored — "the largest factorization I'm aware of" — and wondered whether even smaller keys existed in 1990s browser roots.

Using archive.org collections of old browser installers, he catalogued ancient root certificates and found two 512-bit RSA roots from a defunct Canadian CA called **E-Certify**, shipped with Netscape 4.51 in March 1999. He ran **CADO-NFS** on a Ryzen 9 5950X, factoring the SSL root in ~32 hours and the S/MIME root in ~29 hours, then reconstructed both private keys.

He also built a custom Go-based TLS server (using Claude Code) to demonstrate issuing valid certs trusted by Netscape 4.51, hosted at `e-certify.fly.dev` — though no modern browser will connect.

As a bonus, a 512-bit VeriSign test code-signing CA from IE 3.02 was factored in roughly an hour using a GPU cluster by Steve Weis. McPherrin published all recovered private keys and tools in his GitHub repo.
