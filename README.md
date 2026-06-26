<div align="center">

<img src="assets/banner.svg" alt="Michael — software, systems and AI engineer. From the kernel to the cloud, I build all of it." width="100%" />

</div>

# Hi, I'm Michael &nbsp;·&nbsp; [`@convenientlymike`](https://github.com/convenientlymike)

<p align="center">
  <img src="https://img.shields.io/badge/Kernel%20%E2%86%92%20Cloud-8B5CF6?style=for-the-badge&labelColor=09090F" alt="Kernel to Cloud" />
  <img src="https://img.shields.io/badge/End--to--end%20ownership-6366F1?style=for-the-badge&labelColor=09090F" alt="End-to-end ownership" />
  <img src="https://img.shields.io/badge/200%2B%20automations%20in%20prod-22D3EE?style=for-the-badge&labelColor=09090F" alt="200+ automations in production" />
  <img src="https://img.shields.io/badge/Real--estate%20tech-A78BFA?style=for-the-badge&labelColor=09090F" alt="Real-estate tech" />
</p>

**I build and own entire backends end-to-end** — the AI automation, CRMs, and custom internal systems that run a **real estate investment firm**, plus the courses platform that trains the team. On top of that, I ship **full SaaS products**, front to back.

Much of that product work lives in **real-estate tech** — an investment firm's operational backend, a property-tour SaaS, and a wholesaling platform — so I pair real domain fluency with the range to build whatever layer the problem needs.

> **The throughline:** when a system has no API, no docs, or no abstraction left to lean on, I drop to the kernel and reverse-engineer it myself. I build the high-level product *and* the low-level machinery underneath it — so I'm rarely blocked by "that's not exposed." **Kernel to cloud, I build all of it.**

<p>
<a href="https://www.linkedin.com/in/michaelfbirney"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"/></a>
<a href="mailto:convenientlymike@gmail.com"><img src="https://img.shields.io/badge/Email-0B0B0B?style=flat-square&logo=maildotru&logoColor=white" alt="Email"/></a>
</p>

[![Typing SVG](https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=18&pause=1200&color=8B5CF6&width=560&lines=Backend+%26+systems+engineer;AI+automation+%C2%B7+SaaS+%C2%B7+low-level+systems;Real-time+multiplayer+frameworks;Kernel+to+cloud%2C+I+build+all+of+it)](https://github.com/convenientlymike)

<img src="assets/divider.svg" width="100%" height="5" alt="" />

### 🚧 What I'm building right now

- **The operational backend of a real estate investment firm** — AI automation, CRM, custom ops tooling, and a courses platform, owned end to end. **200+ automations in production doing the work of several full-time roles — built in under a year.** *(Proprietary — sanitized write-up below.)*
- **Virtual House Tours** — a full property-tour SaaS: native iOS capture, web viewer + dashboard, Tauri desktop, a Fastify API, and Stripe billing.
- **A real-time multiplayer game-server framework & a defensive, server-authoritative anti-cheat** — ground-up and standalone (no off-the-shelf base): a 37-spec architecture blueprint, a 50-doctrine engineering constitution, and a security core where the server is the only source of truth and the client is treated as hostile input. **The hero is the verification: a 289/289-green mock suite hid eight real bugs** (a money-sign error, hydrate-vs-DB seeding gaps, a fail-*open* create path, a column/NOT-NULL mismatch) — only a real-database gate exposed them. Ledger-as-truth economy on MariaDB, an event-bus hardened choke point, a premium React 19 in-game UI. *(Commercial · private — sanitized write-up below.)*
- **SteelToe** — a verified-reputation network for the skilled trades: a single-player owner hiring tool that turns a worker's reliability into a portable, verified asset, designed to dodge the labor-marketplace trap and built compliance-first (EEOC / FCRA / defamation). *(Private · design + v0 — sanitized write-up below.)*
- **An AI trading control plane** — lets an LLM research and *propose* trades on a brokerage account while **17 deterministic rails the model can't argue past + a human approval step** make the catastrophic outcomes impossible by construction. **Paper-first as a code path** (real orders physically gated until a forward, cost-inclusive edge is proven), contribution-stripped returns vs. a benchmark, a hash-chained decision log, and approve/reject from your phone via Discord. Honest framing: *the edge is unproven — the boring index DCA does the real compounding.* *(Private — sanitized write-up below.)*
- **Deep-systems engineering** — custom Android platform + GKI Linux kernel work, dynamic instrumentation, and a Vulkan↔Metal GPU translation path.

<img src="assets/divider.svg" width="100%" height="5" alt="" />

### 📌 Selected work

> Most of my highest-leverage work is proprietary or client code and lives in private repos. I publish **sanitized architecture write-ups** instead of the source → **[case studies →](https://github.com/convenientlymike/case-studies)**. Happy to walk through any of it in depth on a call.

| Project | What it is | Stack |
|---|---|---|
| ⭐ **Real-estate firm backend** *(flagship · private)* | The complete software backbone of an investment firm — AI automation, CRM, custom internal platforms, courses. **200+ production automations replacing several full-time roles.** | `Python` · `FastAPI` · `TypeScript` · `LLM orchestration` · `Postgres` |
| 🏠 **Virtual House Tours** *(in development)* | Full property-tour SaaS — iOS app, web + dashboard, Tauri desktop, signed-URL delivery, Stripe billing, background workers. | `TypeScript` · `iOS` · `Fastify` · `Postgres` · `Redis` · `S3` |
| 🏘️ **Real-estate wholesaling platform** *(private)* | A wholesaling software stack — Next.js web, a Go service for seller outreach/telephony, a FastAPI AI lead layer, Temporal deal workflows, ClickHouse analytics, Kafka streaming. | `Next.js` · `Go` · `FastAPI` · `Temporal` · `ClickHouse` · `Kafka` |
| 🦺 **SteelToe — verified-reputation network for the trades** *(design · v0 · [case study](https://github.com/convenientlymike/case-studies/blob/main/12-steeltoe-reputation-network.md))* | A reputation layer for trades hiring — turn a worker's reliability into a **portable, verified asset** so an owner can tell the grinders from the flakes *before* hiring. **Owner-tool-first** to dodge the labor-marketplace trap (matching has no moat — even a >$750M incumbent exited the space); the reputation/verification schema is designed around **EEOC / FCRA / defamation**. Honest framing: *v0 proves the tool, not the network.* | `Next.js` · `TypeScript` · `Prisma` · `Postgres` |
| 🎮⚔️ **Real-time multiplayer game-server framework & defensive anti-cheat** *(commercial · private)* | Ground-up, server-authoritative framework — a module loader + phase state-machine spine, an event-bus **7-stage hardened choke point** (malformed → unknown-event → protocol → resolve → rate-limit → validate → dispatch) every inbound message must traverse, identity / permissions / economy domains, a **ledger-as-truth** economy on MariaDB (append-only, partition-ready, fail-closed write-through, crypto-shred GDPR schema). Premium **React 19 + Vite 6** in-game UI — gamepad-first, fully rebindable keybinds, focus-tracking. Verified by a **3-tier ladder**: mock (<1s) → real-DB boot-smoke (the authoritative gate — caught 8 bugs a 289/289 mock suite missed) → synthetic N-player load. | `Lua` · `TypeScript` · `React` · `MariaDB` · `Docker` · `Server-authoritative` |
| 🔬 **Verification ladder & biting quality gates** *(methodology · [case study](https://github.com/convenientlymike/case-studies/blob/main/10-multiplayer-game-framework-verification.md))* | The "the real database is the truth" approach, formalized: mock-native load test (license-free, <1s) → real-DB boot-smoke (the authoritative tier) → synthetic concurrent traffic. Plus an **11-check static gate** (secrets, server-authority, unguarded events, NUI focus-arbiter, perf budget) — each shipped **with a negative-control fixture** + a `--self-test` meta-gate proving every check goes **red** on bad input. A cross-language parity gate pins a `Lua` server impl and a `TypeScript` UI port to one shared **golden vector** (29 rows, `.5`-rounding edges included) so the two can't drift. | `Testing` · `Quality gates` · `Lua` · `TypeScript` · `MariaDB` · `Python` |
| 📈🛡️ **AI trading control plane** *(private · [case study](https://github.com/convenientlymike/case-studies/blob/main/14-ai-trading-control-plane.md))* | Lets an LLM research and *propose* trades on a brokerage account while **17 deterministic rails the model can't edit or argue past** + a human approval step make the catastrophic outcomes (negative-edge ruin, settlement lockouts, runaway double-orders, hallucinated tickers) **impossible by construction**. **Paper-first as a code path** — real orders are physically gated until a forward, cost-inclusive paper run proves a positive net-of-cost edge; returns shown as a contribution-stripped **time-weighted return** vs. benchmark; an append-only **hash-chained decision log**; **every rail backed by a negative-control test that bites**. Approve/reject from a phone via a Discord bot. Honest framing: *the edge is unproven — the agent is a capped, mostly-paper experiment; the boring index DCA does the real compounding.* | `TypeScript` · `React 19` · `Fastify` · `node:sqlite` · `Discord` · `MCP` |
| 🎛️ **`dma-manager` — hardware control plane** | Premium real-time control plane for hardware controllers — 30 Hz telemetry, a clean hardware-abstraction layer (sim → probe → PCIe → serial → remote), hardened API, and a **brick-safe firmware lifecycle** (detect → back up → flash → verify) driven by a guided onboarding wizard. | `TypeScript` · `React` · `FastAPI` · `real-time HAL` |
| 🧱🛡️ **[`bricksafe`](https://github.com/convenientlymike/bricksafe)** *(open source)* | Never brick a device — the safe-by-construction firmware-write core, extracted + made domain-neutral: one write-gate (backup-before-write hard gate, byte-level placeholder guard, read-before-write CAS, confirm-readback, undo + audit). Zero runtime deps, `mypy --strict`. | `Python` · `embedded` · `safety` |
| 🔬 **Low-level systems & RE** | From-scratch systems stack: custom GKI 5.15 Linux kernel, Android platform engineering, dynamic instrumentation, native reverse engineering, GPU translation. | `C` · `Kotlin` · `Instrumentation` · `Vulkan` · `Metal` · `AOSP` |
| 🧬 **[Game-asset CDN reverse engineering](https://github.com/convenientlymike/case-studies/blob/main/11-unity-asset-cdn-re.md)** *(methodology · case study)* | Recovering the exact asset-CDN URL a shipping **Unity / IL2CPP** game resolves at *runtime* (it isn't a literal) — static string-hunt → disassembling the base accessor → a **passive `/proc/mem` pointer-chase** (ELF VA→runtime mapping, with a built-in correctness gate so a wrong offset fails loud, not silent) → **verified by byproduct** against the on-disk catalog hash. Plus the infallible fetcher: per-byte integrity check with a **negative control that bites**, resumable, exact request replication. | `Reverse engineering` · `IL2CPP` · `Unity` · `Python` · `ARM64` |
| ✅ **[Forcing-function engineering](https://github.com/convenientlymike/case-studies/blob/main/07-forcing-function-completeness.md)** *(methodology)* | Making "done" machine-checkable — every quality doctrine encoded as a lint gate or test that fails the moment it's broken (route↔UI coverage, one-audited-write-path, risk-badging, docs-can't-drift), plus a multi-agent completeness audit that drove a 40+ finding sweep to zero. | `Quality gates` · `CI` · `Python` · `TypeScript` |
| 🧪 **[Browser Harness](https://github.com/convenientlymike/browser-harness)** | Autonomous CDP-driven debugging + observability toolkit — drives a real browser, captures runtime/network failures, turns "looks fine" into "proven." | `Python` · `Node` · `Playwright` · `CDP` |
| 🛰️ **[Fleet](https://github.com/convenientlymike/fleet)** | Parallel-agent compatibility for Claude Code — open many windows on one project; an edit to a file a *live* agent has claimed is hard-blocked at the hook (exit 2). Just files + 4 hooks, no daemon. | `Bash` · `Claude Code hooks` · `CLI` |
| 🩺 **[svgsafe](https://github.com/convenientlymike/svgsafe)** | Make SVGs render everywhere — diagnose the iOS/WebKit `<foreignObject>` clipping traps, auto-fix them, or rasterize to a crisp transparent PNG. Zero runtime deps; in-browser playground. | `TypeScript` · `Node` · `CLI` |
| 🖼 **[shotcraft](https://github.com/convenientlymike/shotcraft)** | Turn real terminal output or a before/after into a beautiful, brand-matched PNG for your README — a themeable Carbon + diff framer rendered by your installed Chrome (over CDP). Zero runtime deps; in-browser playground. | `TypeScript` · `Node` · `CLI` |
| 🧊 **[claude-usage-graph](https://github.com/convenientlymike/claude-usage-graph)** | Turn your Claude Code token usage into a 3D isometric calendar — a contribution-graph-style card built from local session transcripts (aggregate counts only). Four themes, optional PNG. Zero required deps; in-browser playground. | `TypeScript` · `Node` · `CLI` |
| 🖥️ **[x86-interactive-on-arm](https://github.com/convenientlymike/x86-interactive-on-arm)** *(open source)* | Run x86-only **interactive-console** server binaries on Apple Silicon — the two-field Colima + Compose recipe (`--cpu-type max` + `stdin_open`) that turns a phantom, every-run **exit-139** "emulation segfault" into a clean boot. The diagnosis: a *deterministic* exit code means a deterministic *cause*, not emulation jitter. | `Colima` · `Docker` · `QEMU` · `macOS` · `shell` |

<img src="assets/divider.svg" width="100%" height="5" alt="" />

### 🧰 Core stack

What I reach for daily — surfaced in-context above; here's the spine:

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Go](https://img.shields.io/badge/Go-00ADD8?style=flat-square&logo=go&logoColor=white)
![C](https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=c&logoColor=black)

![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Next.js](https://img.shields.io/badge/Next.js-0B0B0B?style=flat-square&logo=nextdotjs&logoColor=white)
![React](https://img.shields.io/badge/React-149ECA?style=flat-square&logo=react&logoColor=white)
![Postgres](https://img.shields.io/badge/Postgres-4169E1?style=flat-square&logo=postgresql&logoColor=white)

![LLM orchestration](https://img.shields.io/badge/LLM_orchestration-8B5CF6?style=flat-square&logo=openai&logoColor=white)
![Linux internals](https://img.shields.io/badge/Linux_internals-FCC624?style=flat-square&logo=linux&logoColor=black)
![Reverse engineering](https://img.shields.io/badge/Reverse_engineering-E83E8C?style=flat-square&logo=ghidra&logoColor=white)

<p align="center"><sub>Languages measured from real code across my repos — <em>including private work</em> — with a live contribution calendar:</sub></p>
<p align="center"><img src="assets/metrics.png" alt="Most-used languages and contribution calendar, measured from real code including private repositories" width="100%" /></p>

<p align="center"><sub>And the volume behind it — total Claude Code tokens, with a 3D calendar of daily usage (aggregate counts from local sessions):</sub></p>
<p align="center"><img src="assets/claude-usage.png" alt="Claude Code token usage — 71B+ tokens, with a 3D isometric calendar of daily usage" width="100%" /></p>

<img src="assets/divider.svg" width="100%" height="5" alt="" />

### 🤝 Let's build something

I take the problems people call impossible — the cross-layer ones, the "no one's done this," the ones that need someone equally at home in a React component and a kernel patch.

**Open to** founding-engineer work · fractional CTO · advisory · select consulting.

💼 [LinkedIn](https://www.linkedin.com/in/michaelfbirney) &nbsp;·&nbsp; ✉️ [convenientlymike@gmail.com](mailto:convenientlymike@gmail.com)

<div align="center">
<br/>
<img src="assets/divider.svg" width="62%" height="5" alt="" />
<br/><br/>
<sub><em>From the kernel to the cloud — I build all of it.</em></sub>
</div>
