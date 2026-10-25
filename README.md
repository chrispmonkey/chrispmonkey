<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/chrispmonkey/chrispmonkey/main/assets/banner-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/chrispmonkey/chrispmonkey/main/assets/banner-light.svg">
  <img alt="Chris Price — Head of Business Development, AI &amp; DePIN at Aptos Labs" src="https://raw.githubusercontent.com/chrispmonkey/chrispmonkey/main/assets/banner-dark.svg" width="100%">
</picture>

<br>

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Chris_Price-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chrisprice2015/) [![X](https://img.shields.io/badge/X-@chrispmonkey-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/chrispmonkey) [![UpLevel](https://img.shields.io/badge/UpLevel-uplevel.llc-6366F1?style=for-the-badge&logo=vercel&logoColor=white)](https://www.uplevel.llc)

</div>

---

## The short version

I'm **Head of Business Development, AI & DePIN at [Aptos Labs](https://aptoslabs.com)** — and I write the code.

Most people in my seat can *read* a roadmap. I ship against it. When a partner integration stalls on a technical unknown, I don't file a ticket and wait a sprint — I open the repo, build the prototype, and bring back something that runs. That shortens the distance between "interesting conversation" and "live in production" from quarters to weeks.

It's a strange combination on paper. In practice it's the whole advantage: I can sit in a partner's architecture review and a term sheet negotiation on the same afternoon, and be genuinely useful in both.

**Ten years, four platform shifts** — mobile → augmented reality → onchain → AI. I've been early to each one, at the companies defining them.

<div align="center">
<br>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/chrispmonkey/chrispmonkey/main/assets/stats-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/chrispmonkey/chrispmonkey/main/assets/stats-light.svg">
  <img alt="Contribution velocity: yearly GitHub contributions since 2019, refreshed daily" src="https://raw.githubusercontent.com/chrispmonkey/chrispmonkey/main/assets/stats-dark.svg" width="92%">
</picture>
<br><br>
</div>

> This card is **generated from the GitHub API and committed to this repo**, refreshed daily by [a workflow](.github/workflows/refresh-stats.yml). Every hosted README widget I tried was dead or dying — `visitor-badge` returns `410 Gone`, `github-profile-trophy` returns `402`, and `github-readme-stats` sits at `503` for days. A profile that renders broken is worse than one with no stats at all, so I stopped depending on other people's uptime. [See how it works →](scripts/generate_stats.py)

---

## What I'm building

Everything below is publicly announced Aptos work. Most of my day-to-day lives in private org repos, so the public trail here is the tip of it.

| Product | What it is |
|:--|:--|
| **[Watchee](https://watcheeos.com)** | Decentralized streaming platform: consumer app, mini-app developer portal, and rights management for studios and distributors. |
| **[Shelby](https://shelby.xyz)** | Cloud-grade decentralized hot storage, co-built with Jump Crypto. Sub-second reads, pay-per-view access, built for data-heavy AI agent workloads. |
| **[Geomi](https://geomi.dev)** | Developer platform for Aptos — API keys in seconds, no-code indexers, gas sponsorship, one-click NFT collections. |

Alongside that: agentic coding tooling, zero-knowledge identity, confidential compute, and Move smart contract infrastructure.

### On the side — [UpLevel Technologies](https://www.uplevel.llc)

My own studio, where I build and ship full products end to end. These repos are private, but the products are real:

| Product | What it is |
|:--|:--|
| **[Tkay](https://tkay.app)** | *Make that idea happen.* Capture something you learned, connect it to your real work, and a small crew — Scout, Maker, Checker — tries it safely so you keep only what works. [iOS beta on TestFlight](https://testflight.apple.com/join/u18EdQhh). |
| **[CivicChange](https://civicchange.app)** | *What's happening here?* Point your camera at a building in San Francisco and get the story from the city's public records, in plain language. Expo, Supabase, DataSF, 8 languages. |
| **[PluckIt](https://pluckitapp.com)** | A reusable-content launcher: capture anything you'll need again, and PluckIt understands it, makes it searchable, and gets it back out in seconds. iOS, Android and desktop. Pre-release. |
| **[Vessel](https://vessel-website.vercel.app)** | Practice-management and documentation software for licensed therapists, with a between-session reflection app for the clients they invite. |

### Hacking the Humane AI Pin — [PenumbraOS](https://github.com/PenumbraOS)

When Humane shut down the AI Pin's servers, the community behind PenumbraOS set out to keep the device alive. I'm contributing to it, mostly around **music**:

- **Music provider plugin system** — a stable Rust ABI so the Pin's server can load streaming providers as plugins, plus a starter template so anyone can add their own. I wrote providers for **Apple Music, Spotify, Tidal, YouTube Music and Mopidy**.
- **Upstream PRs** to [`humane-system-hook`](https://github.com/PenumbraOS/humane-system-hook) and [`center`](https://github.com/PenumbraOS/center): [redirecting the Pin's music app to a local Tidal mock](https://github.com/PenumbraOS/humane-system-hook/pull/8) (merged), [the music provider seam](https://github.com/PenumbraOS/humane-system-hook/pull/11), and [provider settings and login UIs](https://github.com/PenumbraOS/center/pull/2).

PenumbraOS itself is [Adam Gastineau](https://github.com/agg23)'s project; the plugin repos are mine and private for now.

---

## How I got here

```
  NOW ─┬─  APTOS LABS — Head of BD, AI & DePIN
       │   Perps · decentralized storage · AI agents · DePIN
       │   Rust · Move · TypeScript · Python
       │
 2022 ─┼─  APTOS LABS — Head of Business Development
       │   Joined a pre-mainnet L1 in September. Built out the
       │   partner ecosystem from the ground up.
       │
       ├─  METAPLEX STUDIOS — Partnerships
       │   Solana NFT infrastructure. Closed media, entertainment,
       │   sports and social deals.
       │
       ├─  META / FACEBOOK — BD & Strategic Partnerships, AR
       │   Spark AR and analytics. The AR platform shift, from inside
       │   the company driving it.
       │
 2015 ─┴─  MICROSOFT — Community & Accounts
           Power BI and developer community.
```

The through-line: I go where the platform shift is happening, early, and I learn to build on it before it's obvious. Mobile, then AR, then onchain, now AI — same instinct each time.

---

## Stack

**Languages** &nbsp; ![Rust](https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white) ![Move](https://img.shields.io/badge/Move-4A5568?style=flat-square) ![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white) ![Swift](https://img.shields.io/badge/Swift-F05138?style=flat-square&logo=swift&logoColor=white) ![Solidity](https://img.shields.io/badge/Solidity-363636?style=flat-square&logo=solidity&logoColor=white) ![Objective-C](https://img.shields.io/badge/Objective--C-438EFF?style=flat-square&logo=apple&logoColor=white)

**Onchain** &nbsp; ![Aptos](https://img.shields.io/badge/Aptos-4A5568?style=flat-square) ![Solana](https://img.shields.io/badge/Solana-14F195?style=flat-square&logo=solana&logoColor=black) ![Circom](https://img.shields.io/badge/Circom_·_ZK-8B5CF6?style=flat-square) ![Move Prover](https://img.shields.io/badge/Formal_Verification-06B6D4?style=flat-square)

**AI & agents** &nbsp; ![Claude](https://img.shields.io/badge/Claude-D97757?style=flat-square&logo=claude&logoColor=white) ![MCP](https://img.shields.io/badge/MCP-4A5568?style=flat-square) ![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)

**Spatial & mobile** &nbsp; ![ARKit](https://img.shields.io/badge/ARKit-000000?style=flat-square&logo=apple&logoColor=white) ![Spark AR](https://img.shields.io/badge/Spark_AR-0081FB?style=flat-square&logo=meta&logoColor=white) ![Unity](https://img.shields.io/badge/Unity-100000?style=flat-square&logo=unity&logoColor=white) ![Unreal](https://img.shields.io/badge/Unreal_Engine-0E1128?style=flat-square&logo=unrealengine&logoColor=white) ![SwiftUI](https://img.shields.io/badge/SwiftUI-0071E3?style=flat-square&logo=swift&logoColor=white) ![React Native](https://img.shields.io/badge/React_Native-20232A?style=flat-square&logo=react&logoColor=61DAFB) ![Expo](https://img.shields.io/badge/Expo-000020?style=flat-square&logo=expo&logoColor=white)

---

## Earlier work

My current code is in private repos, which the stat card above counts. The public ones worth a look are from the start:

| Year | Project | What it was |
|:--|:--|:--|
| 2015 | [iAttendance](https://github.com/chrispmonkey/iAttendance) | Class attendance via **iBeacons + TouchID** — biometric proximity check-in, built the year Apple shipped the API |
| 2015 | [Fury](https://github.com/chrispmonkey/Fury) | Microsoft *hACTOthon* entry — an account-management assistant that ranked next-best actions for a rep from customer signals and news |

---

## Open to the right thing

I'm not looking, but I'll always hear out something genuinely interesting — especially at the intersection of **AI agents, DePIN, and onchain infrastructure**, where the work is equal parts partnership strategy and shipping code.

The fastest way to reach me is **[LinkedIn](https://www.linkedin.com/in/chrisprice2015/)** or a DM on **[X](https://x.com/chrispmonkey)**.

<div align="center">
<br>

[![LinkedIn](https://img.shields.io/badge/Let's_talk-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/chrisprice2015/) [![X](https://img.shields.io/badge/DM-@chrispmonkey-000000?style=for-the-badge&logo=x&logoColor=white)](https://x.com/chrispmonkey)

<br>
<sub>San Francisco, CA</sub>
<br><br>
<img src="https://komarev.com/ghpvc/?username=chrispmonkey&style=flat-square&color=6366F1&label=profile+views" alt="Profile views">

</div>
