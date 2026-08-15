---
source_url: https://podcasts.happyscribe.com/all-in-with-chamath-jason-sacks-friedberg/hour-worker-four-robotics-ceos-on-humanoids-at-home-china-s-threat-and-the-end-of-dangerous-jobs
author: Jason Calacanis, Chamath Palihapitiya, David Sacks, David Friedberg
date: 2026-07-29
---

# The $1/Hour Worker: Four Robotics CEOs on Humanoids at Home, China's Threat, and the End of Dangerous Jobs

A series of four interviews conducted at the Machina conference in Paris, focused on the current state of robotics deployment, AI integration, China competition, and the future of humanoid labor.

## Interview 1: Dr. Peter Fankhauser, Co-founder & CEO, ANYbotics

ANYbotics makes four-legged inspection robots called AnyMal, deployed in critical infrastructure. The company has operated for 10 years, with the first five focused on research.

**Why four legs?** Stability, balance, and wide footprint allow operation on slippery, rough, or outdoor terrain. The form factor suits industrial environments with enough space to maneuver.

**Use cases:** Industrial inspection in oil & gas, offshore wind transformer stations, chemical plants, and explosive atmospheres. Robots carry thermal cameras, acoustic sensors, and gas detectors — capable of detecting micro-leaks and equipment overheating invisible to humans.

Fankhauser noted: "It's not about labor replacement... what can we do better? What can we do superhuman?"

Key metrics: robots run missions up to 40 times per day, with ~2-hour battery life and autonomous docking/charging. Deployed in environments ranging from -20°C (Norway) to +60°C (deserts).

**On sourcing:** Zero percent of components sourced from China, partly by historical design and customer requirements around data sovereignty.

**On Chinese competition:** Chinese robots demonstrate impressive hardware but lack the full solution stack — autonomy, inspection intelligence, workflow integration, and cybersecurity certification. He noted: "You don't want to have 15 cameras in your critical infrastructure that somebody else controls."

**On armed robots:** "As an engineer, you should have pride to build technology for good... putting a gun on it, it's just risky." He noted a 2021 letter co-signed with Boston Dynamics condemning weaponization of robots.

## Interview 2: Bernd Borniek, Founder & CEO, 1X (Neo Robot)

1X is building the Neo, a humanoid home robot targeting consumer and enterprise markets. The company sold out the first 10,000 pre-orders within days at approximately $500/month subscription pricing.

**2026 shipping commitment:** Borniek confirmed delivery will happen in 2026, with early units being "rough around the edges" but trending toward full autonomy capability.

**Open platform strategy:** Neo will launch as a platform, allowing third-party developers to build applications and deploy their own models. 1X will allow competing AI models (e.g., from OpenAI or Anthropic) to run on Neo.

**Data and training pyramid:** A hierarchy — teleoperation data (small, high quality), human-worn sensor data, egocentric video, and general internet video. The key bet at 1X: because Neo's morphology closely mirrors humans, it can train on vast existing human video data on the internet, unlocking "multiple orders of magnitude more data" than competitors collecting from scratch.

**World Model Lab:** 1X launched this to capture scaling laws on general video pre-training.

**Hard takeoff timeline:** Borniek predicted robots building robots and chip fabs — a self-sufficient labor abundance system — within 10 years, with his personal best estimate at **3 years**.

## Interview 3: Amanda McMaster, Interim CEO, Boston Dynamics

Boston Dynamics has passed through Google, SoftBank (Masayoshi Son), and is currently owned by Hyundai.

**Spot robot:** Over 500 customers across 46 countries. Used primarily for industrial inspection — acoustic monitoring, gauge reading, vibration detection — and security perimeter work. Pricing ranges from ~$100K (base) to ~$300K fully loaded.

**Atlas:** Humanoid robot with self-swappable batteries. Battery enables near-continuous operation; mean time between human intervention is over 3,000 hours. Likely to be offered as Robot-as-a-Service.

**Two-brain architecture:** Physical control (dynamic movement, manipulation) stays on-robot. Semantic reasoning can live in the cloud, potentially via partners like Google DeepMind.

**Manufacturing:** 100% of Boston Dynamics robots built outside China. McMaster stated: "We have seen what happens if we let China win in the semiconductor space. We can't do that with robotics." She called for a national robotics strategy and noted Chinese quadrupeds have already been observed leaking data back to China.

## Interview 4: Professor Jonathan Hurst, Co-founder & Chief Robot Officer, Agility Robotics

Hurst holds a PhD in robotics (2008) and remains a professor while leading Agility. The company's humanoid robot, **Digit**, is in its V4 generation.

**Why this time is different:** Previous humanoid robots could look human but couldn't do useful work. That has changed. "Perception was incredibly difficult, and the fact that perception is all but solved... is a really, really huge inflection point."

**Digit V5 significance:** First humanoid that can operate outside a physical safety barrier alongside humans in a warehouse — a critical threshold for scaling deployment. Achieves ~20 hours of daily operation due to fast-charge battery improvements.

**Current deployments:** Picking up bins/totes, palletizing/depalletizing in warehouse environments. Amazon is a noted partner.

**Economics:** Bill of materials heading toward car-level pricing. At 20 hours/day × 365 days × 5-year lifespan = ~40,000 hours of labor. At a $40K robot cost, that approaches **$1/hour** — versus $20–40/hour for human factory workers. Both CapEx and Robot-as-a-Service models offered.

**On AI and training:** Language models provide a "rising tide" but robot control requires separate training data — torque commands, sensor inputs — which doesn't exist on the internet. Solutions include teleoperation data, motion capture, world models, and sim-to-real transfer. He cautioned: "There's always a massive sim-to-real gap."

**Future use cases:** Retail, grocery, hospitals, construction, last-mile delivery. He expressed hope that future generations will look back on today's dangerous, repetitive jobs the way we now view coal mining.
