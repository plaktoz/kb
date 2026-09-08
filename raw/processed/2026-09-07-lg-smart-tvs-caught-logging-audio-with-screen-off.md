---
source_url: https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html
author: Anubhav Sharma
date: 2026-09-07
---

# LG smart TVs caught logging audio with screen off and snooping on local devices

A 135-minute Gamers Nexus investigation, conducted alongside Level1Techs and independent security researchers, revealed that LG smart TVs engage in extensive data collection beyond what users typically expect.

Using Wireshark packet captures, the team found the TVs actively scanning home networks to identify other connected hardware — phones, smartwatches — while also collecting neighboring Wi-Fi network names, signal strengths, and location data. This feeds into **LG Ad Solutions**, the company's advertising arm, which claims access to "363 million secondary addressable devices in the US alone" by tracking hardware on the same network as LG sets.

The TVs also run **Automated Content Recognition (ACR)**, fingerprinting on-screen audio and video to track viewing habits across all inputs.

Most notably, bench testing revealed the TVs could capture microphone audio while appearing to be in standby. When network access was cut, the device stored recordings locally and uploaded them once connectivity resumed.

Researchers additionally found **remote code execution vulnerabilities** in webOS, currently moving through responsible disclosure. Their recommendation: disconnect LG sets from the internet entirely and use external streaming devices.

LG had not commented at time of publication.
