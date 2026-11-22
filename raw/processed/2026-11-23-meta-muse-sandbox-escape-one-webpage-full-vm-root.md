---
source_url: https://thecybersecguru.com/exploits/meta-muse-sandbox-escape-nebusec
author: Unknown
date: 2026-11-23
---

# Meta Muse Sandbox Escape: One Webpage, Full VM Root

On November 20, the security firm NebuSec published a demonstration that anyone building AI agents should read closely. An attacker-controlled webpage, opened by Meta’s Muse assistant during an ordinary request to save the page as a PDF, ended with the user’s private conversations and stored memories arriving at an external server. No approval dialog appeared. Pushed one step further, the same chain reached the credential store that Meta deliberately keeps outside the agent’s reach.

This was a laboratory demonstration against the researchers’ own Muse instance, not an attack on real users. NebuSec says the Muse team patched every described weakness before publication. Meta has not publicly confirmed the fixes or said whether any user data was accessed before the patches landed.

The headline matters less than the architecture it defeated. Muse was designed on the assumption that its own agent could be turned against the user, and by NebuSec’s account each containment control worked as specified. The attack went through them anyway.

### How Muse is built: a cloud VM designed for a hostile occupant

Muse launched on September 8, 2026 as Meta’s personal agent. Its defining choice is that the chat interface and the agent are the same thing. The website, the mobile apps and the WhatsApp assistant all connect to one agent running in the user’s own cloud computer, which is what allows long-running background work, purchases and connected accounts.

#### The VM and the runtime cell

Meta provisions a 2-vCPU, 8 GiB virtual machine per user under Cloud Hypervisor, the Rust-based virtual machine monitor with a deliberately small device model, running on KVM. Inside that Ubuntu VM, a systemd-nspawn container called the runtime cell hosts the Codex-like agent harness, internally named Hatch. Requests arrive over the Noise protocol at an ingress service in the VM and cross a Unix socket to the hatch daemon inside the cell. Conversation history and memories sit on persistent storage dedicated to that VM, while durable application state lives in a Postgres database outside the cell.

#### Root inside the container

The agent runs as root inside its container, which is less alarming than it sounds. The runtime-cell code fixes the user-namespace range at 131072 to 196607, so UID and GID 0 inside the cell map to the unprivileged UID 131072 in the VM. The same base appears across the VM configuration in rootfs ownership, connector socket ownership and peer checks. Meta’s launch documentation also describes filtered system calls and stripped capabilities, including no CAP_SYS_PTRACE and no CAP_NET_ADMIN.

#### Security services outside the cell

The security services live outside the cell entirely:

- hatch-safety reviews model input and output.
- hatch-authd holds connector credentials and mints surrogate tokens.
- Privilege-separation workers execute connector logic.
- Sentinel is the sole permission authority for connector actions and network egress.

Real OAuth tokens replace surrogates only at the network boundary, after a request is authorized, so the agent never sees them. The shipped inference and Stefi proxy units are the documented exception. Each loads its own platform secret through systemd’s LoadCredential= mechanism, which delivers credentials into a per-unit directory instead of the agent’s environment.

At launch, Meta said it designed the system on the assumption that the agent may be under attack, with the aim of limiting the damage. A public bug bounty backs that stance, paying up to $300,000 for valid reports, including up to $130,000 for prompt injections affecting a single user. This is an assume-breach design in the classical sense. NebuSec’s question was whether the boundaries hold when the occupant of the cage is genuinely hostile. The answer depended on components Meta’s threat model treated as scenery: a browser binary, an update schedule and a shared kernel.

### Four browsers and one outdated Chromium renderer

Muse has a browser portfolio rather than a browser. NebuSec’s write-up lists four backends, selected by task:

1. Container tools such as browser_open and browser_search call a remote page-fetching service. Its internals are unknown and it may not be browser-backed at all.
2. Interactive work such as logins, forms and bookings goes through browser.browse to a broker in the user VM, which provisions an on-demand browser VM running Chromium 155.0.8059.80.
3. Background page checks run in htch-browser, a separate systemd-nspawn container with its own network policy: direct IPv4 egress through a dedicated masquerade rule, internal and reserved IPv4 ranges denied, IPv6 disabled.
4. A bundled Chromium at /opt/meta-chromium/chrome, started directly by the agent or through Playwright inside the runtime cell, handles screenshot review, thumbnails and PDF export.

The fourth path is the one that mattered.

#### Why the bundled Chromium was the weak path

Meta’s public documentation describes the brokered browser in detail. The driving sub-agent sees an accessibility-tree snapshot instead of the raw DOM, has no JavaScript execution verbs, cannot touch Chrome DevTools, and pauses entirely while the credential store fills a login form. That hardening covers the brokered path only. The bundled Chromium sits beside the agent in the runtime cell and inherits the cell’s Sentinel-mediated egress. Per NebuSec, it ran with its IPC sandbox disabled in the PDF-export configuration.

Chromium’s security economics assume a renderer will eventually be compromised and the sandbox will contain it. With the sandbox off, a renderer bug stops being a contained crash and becomes code execution with the agent’s privileges.

#### The update lag that supplied the bug

In early October the cell still carried Chromium 152.0.7977.82, a patch release shipped on September 3 for a milestone that reached stable in August. A later snapshot showed 155.0.8059.80. NebuSec estimated that more than five public V8 vulnerabilities were usable against the lagging build without additional flags, including issue 559932543 (which the firm itself reported), 560233248 and 550360762.

The chain used issue 554034656, a parser bug that escaped the V8 sandbox. That phrase carries technical weight. V8’s heap sandbox assumes memory corruption will happen inside its pointer cage and confines it there, with external references mediated through pointer tables, so corruption inside the cage is not yet process compromise. A sandbox-escaping bug crosses that inner boundary and yields arbitrary code execution in the renderer. With the outer IPC sandbox already disabled, no second bug was needed.

NebuSec prices the renderer bug at roughly $500 in bounty terms. Chromium’s reward model values renderer bugs as if the sandbox holds, and Meta’s own program would pay 600 times that figure for a working prompt injection. The cheapest bug in the stack opened the door because the layer that was supposed to make it cheap had been switched off. The firm calls the result a 0.5-click RCE: the user’s only action is an innocuous request to save a page, and everything after that happens without further interaction or approval.

### How Sentinel guards the network gateway

The researchers’ first attempts to ship command output to an external server produced the approval dialog Muse users know, even for programs running as root inside the cell. Root needed permission to use the network because the decision lived outside the container. The same privilege-separation pattern governs everything else. A container-side CLI performs no privileged operations itself. It passes typed arguments and file descriptors over a socket such as /run/hatch/privsep/foo.sock to a worker in the VM.

#### Privilege-separated connector workers

NebuSec examined the Notion connector’s worker and found systemd’s Accept=yes mode spawning a per-connection instance under a dedicated hatch-w-notion-cli account. That account had a temporary home, a read-only system tree, an obscured /proc, and syscall filters denying mount, setns and unshare, the primitives an escaper would reach for. On the credential-read path, authd derived the worker’s scope from its cgroup and handed over only the Notion document. Socket permissions admitted the mapped runtime-daemon identity and nothing more.

#### Fake-IP DNS and compulsory proxying

The cell’s only external interface is host0, with a default route and DNS resolver both pointing at 198.19.0.1, the VM-side address of Sentinel (hatch-sentinel). Sentinel answers DNS on port 53 and proxy traffic on port 3128. Its resolver never returns real destination addresses. It allocates a fake address from 198.18.0.0/16 and records the mapping, so when a connection reaches the proxy it can recover the original domain.

The range is a knowing choice. RFC 2544 reserves 198.18.0.0/15 for network benchmarking, and proxy tools like Clash repurpose the same block for fake-IP routing because nothing legitimate on the public internet lives there. The scheme also means the container never learns real IPs, which complements the SSRF restrictions Meta documents: a public hostname cannot talk the cell into reaching private infrastructure after resolution.

Cooperative clients reach the proxy through HTTP_PROXY, HTTPS_PROXY and ALL_PROXY in /opt/hatch/runtime-cell/guest.env. SSL_CERT_FILE tells them to trust Sentinel’s own certificate authority, which lets the proxy terminate TLS and inspect the decoded request at layer 7.

Arbitrary code can ignore environment variables and call connect() directly, so Sentinel also attaches an eBPF program to the container’s cgroup that rewrites external destinations to 198.19.0.1:3128. This is the cgroup socket-address hook family Cilium uses for socket-level load balancing, applied here as compulsory proxying. Unsetting HTTP_PROXY accomplishes very little when the kernel redirects the socket anyway.

At this point the researchers had code execution and could already tamper with chat history, but every obvious exfiltration route ended in a prompt. The guard was working. The next phase was reading its rulebook.

### Exfiltration inside the policy: how private data left without a prompt

Sentinel first attributes each request to its originating process, then evaluates built-in Rego policies, the language of Open Policy Agent. A deny match rejects outright. Everything else is split into reads and writes, and the definition of a read is purely syntactic: only GET, HEAD and OPTIONS requests without a body qualify. Writes need approval unless an allow rule covers them. Reads may leave silently under Muse’s default “Ask for some actions” setting.

#### Taint tracking

Attribution also feeds a taint gate run by execd, which tracks file and process state as clean, tainted, untracked or distrusted. Sentinel accepts clean only when the query succeeds and both the PID and the process start time match. The start-time check exists to defeat PID-reuse impersonation.

Meta’s launch post describes the ambition behind this machinery: a “tainted egress” design where a process that reads user data becomes tainted and loses auto-allow. It is implemented with eBPF cgroup programs plus programs attached to custom Linux Security Module hooks that Meta added to its kernel for taint propagation. In the policy NebuSec observed, taint gates one route to silent approval, where a rule demands a clean origin. A failed or non-clean query removes that route, and evaluation continues through the ordinary allow, deny and prompt rules.

#### Content screening and rolling budgets

Method classification is only the first filter. Sentinel tries hex and Base64 decoding on each URL component and scans the decoded text for email addresses, international phone numbers beginning with +, and six-to-eight-digit values attached to otp or verification_code. The write-up records an odd asymmetry: a short Base64-encoded email address triggered review, while the plaintext [email protected] was allowed.

Chunks that fail to decode are assigned to one of four character-set classes and measured by Shannon entropy against a class-specific threshold. This is a standard DLP technique, and its math is unforgiving in both directions. A hex string carries at most 4 bits of entropy per character and Base64 at most 6, while ordinary prose sits far below its alphabet’s ceiling. Encoded secrets therefore tend to stand out, and shaped payloads can be made not to.

Suspicious requests go to a guard model, policyguard-nvfp4, whose name points to NVIDIA’s 4-bit NVFP4 format. It returns either veto or no_finding. Rolling budgets throttle bulk movement. Within a 60-minute window, traffic from one originator to one domain triggers review above 2 MiB, and the same domain across all originators triggers it above 5 MiB. Rotating processes buys little, so a patient attacker must move data slowly or widely.

#### What went through the gap

Working within those rules, NebuSec sent the user’s conversation history and stored memories to its own server through the browser chain without a single approval prompt. It could also inject entries into the history and alter stored memories. The firm does not publish the exact request construction, but the shape of the gap is visible in the policy itself.

HTTP method semantics are not data-flow semantics. A bodyless GET can carry arbitrary data in its URL, and a classifier that treats reads as inherently benign is betting that URLs hold locators rather than cargo. The content screens inspect shape (decodable patterns, entropy, volume) and ignore provenance, so bytes from the user’s private history look identical to bytes from anywhere else, provided they are dressed to pass.

The integrity half of the result may matter more in the long run. An attacker who can write memories and conversation entries can plant instructions the agent will later treat as its own recollection, turning a one-time webpage visit into a persistent foothold in every future session. Meta’s designers clearly anticipated this class of abuse, yet the composed policy, as deployed, still admitted traffic that realized it.

### The shared kernel was the real boundary

Even with silent exfiltration, the code still ran inside the runtime cell, and container root could call the VM-side sockets only on their terms. Service identity, credential scope and authority all stayed outside. The remaining move was the one the architecture could not abstract away.

A systemd-nspawn container shares its kernel with the VM, and user namespaces remap identities without removing a single syscall from reach. A kernel memory-corruption bug exploited from inside the cell yields root in the VM’s initial namespace. Every socket ACL, cgroup derivation and credential allowlist above it then becomes advisory.

#### Which privilege-escalation primitives survive the crossing

Not every primitive works here. NebuSec notes that data-only copy-on-write bugs, the Dirty Pipe class that overwrites page-cache contents of files the attacker can read, are usually useless in this setup. The container’s filesystem does not expose the VM’s libc, setuid binaries or other dependencies, and writing to an arbitrary file the host never executes escalates nothing. Kernel memory corruption was the practical path to simultaneous escalation and escape.

#### The Hatch kernel and its hardening gaps

The October 2 test environment ran a custom Hatch-built kernel, 7.0.0-39-generic, compiled September 24 with GCC 13.3.0. It was heavily stripped of hardware drivers, filesystems and peripheral protocols, with KALLSYMS_ALL and /proc/kcore disabled. CONFIG_IO_URING was compiled in but blocked, consistent with Meta’s documentation listing io_uring among the cell’s filtered syscalls. That is a defensible posture given io_uring’s years as a leading source of kernel exploits, though the code remains present for anything running outside the filter.

Several hardening options were off:

- RANDOMIZE_MEMORY, which randomizes the direct-map and vmalloc bases.
- HARDENED_USERCOPY, which bounds-checks copies between user and kernel memory.
- INIT_ON_ALLOC_DEFAULT_ON, which zeroes fresh allocations.

Each disabled option removed a nuisance the researchers would otherwise have had to bypass.

#### Exploiting a kernel you cannot see

The genuine obstacle was that no target kernel image was visible from inside the container. No structure-field or function offsets could be precomputed, and the exploit could not assume a fixed CPU or memory layout. Linux 7.0 fell within the published affected ranges of multiple CVEs, and NebuSec’s Automated Exploit Generation framework produced general-purpose exploits that needed no precomputation.

The approach: obtain arbitrary kernel read and write, use physical-memory access to locate the kernel image, parse its embedded symbol tables at runtime, and resolve the data offsets needed for escalation. Classically that means the credential structures or a string like modprobe_path, which the kernel later hands to a root helper. In the firm’s test runs the exploits succeeded more than 99.9 percent of the time.

NebuSec says more than 170 of its patches have been merged into mainline Linux. Its broader argument is that a CVE listing is not an exploitability assessment, and a customized, stripped, partially hardened kernel is exactly the kind of environment where only a working exploit settles the question.

### What root in the VM exposed

The escape delivered everything the cell had been built to withhold.

- **Storage:** Persistent storage not mounted into the container became readable, including the 100 GiB LUKS2/Btrfs volume holding home and service state. That volume was already unlocked and mounted in the VM, a reminder that full-disk encryption defends against someone reading the disk and does nothing against root reading the filesystem.
- **Product files:** Files under /opt/hatch came from a read-only, dm-verity-backed squashfs image. Its Merkle-tree integrity scheme prevents tampering and does nothing about disclosure.
- **Credentials and guard:** Secure Credential Storage, the repository Meta’s surrogation design exists to keep away from the agent, became plain data on a mounted volume. Sentinel itself (its binaries, its policies, its approval state) sat exposed alongside the kernel image under /boot that had been invisible from inside.

The network position changed just as decisively. The cgroup eBPF hook that forced every container connection through Sentinel was attached to the container’s cgroup, so processes running directly in the VM were not covered. They could send outbound traffic that never touched the proxy, and the VM had its own globally routable IPv6 address on its external interface. The exfiltration channel that needed careful tailoring inside the cell became an open pipe outside it.

#### What did not fall

Cloud Hypervisor and KVM still stood between the compromised VM and every other tenant. Crossing that line would have required a guest-to-host vulnerability in the host kernel or the virtual machine monitor, or a vulnerable internal service. NebuSec demonstrated no such escape. The blast radius was one user, but within that radius it was total: chats, memories, files, credentials for connected accounts, and the guard itself.

### Three lessons for AI agent security

Meta did not build something naive. User namespaces, credential surrogation, privilege-separated workers, cgroup-enforced proxying, content inspection and a taint-tracking system with custom LSM hooks add up to a more serious containment effort than most agent platforms ship. NebuSec’s own conclusion is that the controls worked as designed while the chain completed anyway. That is a statement about composition, and no single component is at fault.

1. **Put enforcement below the adversary’s deepest reachable layer.** Sentinel policed the cell from the VM but shared the cell’s kernel. Kernel corruption therefore demoted the guard to another process on a filesystem the attacker could read.
2. **Treat patch cadence as a security boundary.** A September 3 Chromium build sitting in a production cell in October turned publicly documented V8 bugs into a private-VM compromise. The sandbox-disabled utility browser was an attack surface that Meta’s brokered-browser hardening story did not cover.
3. **Classify egress by origin as well as shape.** Policy that sorts traffic by HTTP method and inspects it by pattern screens the shape of traffic. An attacker who reads the rules can dress private data as an innocuous read. Budgets and entropy checks raise the cost of theft without removing the possibility.

### Disclosure status: what is confirmed and what is not

As of publication, the picture is narrow but clean. NebuSec reported everything to the Muse team and states that all described exploits were patched before the write-up went live. Meta has not publicly confirmed the fixes. The write-up also does not say whether any user data was accessed in the window before patching.

The work is separate from September’s macOS flaw, where malware already running as the logged-in user could hijack the local assistant. That was a device-side trust problem, while the Muse chain is a cloud containment failure.

For everyone building agents that browse, execute and hold credentials, the Muse chain answers a question Meta itself posed in its launch post: what happens when the agent really is under attack? The demonstrated answer is that the architecture’s promises hold only up to the least-patched binary inside the cage and the kernel underneath it. The most valuable bug in the stack is the one that lets an attacker stop asking the guard for permission.

### FAQ: Meta Muse sandbox escape

#### What did NebuSec demonstrate against Meta Muse?

NebuSec showed that a single attacker-controlled webpage, opened during a routine save-as-PDF request, could lead to private conversations and stored memories reaching an external server with no approval dialog. Extended further, the chain reached root in the user’s VM and the credential store Meta keeps away from the agent.

#### Were real Muse users attacked?

No. The demonstration ran against the researchers’ own Muse instance. NebuSec says the Muse team patched every described weakness before publication, and Meta has not publicly confirmed the fixes or said whether any user data was accessed beforehand.

#### What is a 0.5-click RCE?

NebuSec’s term for remote code execution where the user’s only action is an innocuous request, here asking Muse to save a page as a PDF. Everything after that happens without further interaction or approval.

#### Why did the Chromium sandbox matter?

The bundled Chromium used for PDF export ran with its IPC sandbox disabled. A V8 renderer bug that escapes the V8 sandbox therefore gave code execution with the agent’s privileges, with no second bug required.

#### Could the attacker reach other Muse users?

NebuSec demonstrated no escape from the VM to the host or other tenants. Cloud Hypervisor and KVM still separated the compromised VM from everyone else, so the blast radius was one user, though total within that radius.
