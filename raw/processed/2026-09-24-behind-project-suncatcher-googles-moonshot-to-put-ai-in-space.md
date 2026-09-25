---
source_url: https://blog.google/innovation-and-ai/models-and-research/google-research/google-project-suncatcher-facts/
author: Travis Beals
date: 2026-09-24
---

# Behind Project Suncatcher: Google's Moonshot to Put AI in Space

Google is launching a prototype satellite on SpaceX's Transporter-18 rideshare mission (developed with Planet) to test whether Tensor Processing Units (TPUs) can function in orbit. The broader goal of Project Suncatcher is to determine if space could host scalable ML infrastructure, leveraging the fact that low Earth orbit satellites can access "up to eight times more solar power than on Earth."

## Key Engineering Challenges

### Hardware Survival

Rocket launches subject components to sustained forces up to 10g, with individual chips experiencing 50–100g. Google conducted multi-axis vibration testing and proton beam radiation tests at UC Davis's Crocker Nuclear Laboratory. Results showed Trillium TPUs can survive radiation doses exceeding what a five-year space mission would deliver.

### Cooling

Space has no airflow, so heat can only be dissipated via radiators. Google is testing heat pipe and radiator combinations in thermal vacuum chambers.

### Satellite Interconnectivity

Future satellite clusters will use lasers for high-bandwidth, short-distance communication — requiring precision comparable to "hitting a coin-size target from miles away while both points are in motion." Two-satellite orbital testing is planned for 2027.
