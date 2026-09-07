---
type: literature-note
source_url: https://www.notebookcheck.net/LG-smart-TVs-caught-logging-audio-with-screen-off-and-snooping-on-local-devices.1391214.0.html
author: Anubhav Sharma
tags: [smart-tv, privacy, surveillance, lg]
date_consumed: 2026-09-07
---

## Summary

A 135-minute Gamers Nexus investigation revealed that LG smart TVs conduct extensive covert data collection, including scanning home networks for connected devices, capturing neighboring Wi-Fi metadata, and running Automated Content Recognition on all inputs. Most critically, bench tests confirmed the TVs record microphone audio even in apparent standby mode, storing recordings locally and uploading them when connectivity resumes. Researchers also discovered remote code execution vulnerabilities in webOS and recommended disconnecting LG sets from the internet entirely.

## Core Concepts

- **[[LG Ad Solutions]]**: LG's advertising arm that aggregates data from LG TVs and claims access to 363 million secondary addressable devices in the US by tracking hardware co-located on the same home network.
- **[[Automated Content Recognition]] (ACR)**: A fingerprinting technique that samples on-screen audio and video to track viewing habits across all inputs — including HDMI — not just streaming apps.
- **[[Network Snooping]]**: LG TVs were caught scanning the local network to enumerate connected devices (phones, smartwatches) and collecting neighboring Wi-Fi SSIDs, signal strengths, and location data.
- **[[Standby Audio Capture]]**: TVs captured microphone audio while the screen was off; when internet was cut, recordings were stored locally and exfiltrated on reconnection.
- **[[Remote Code Execution]] (RCE)**: Vulnerabilities discovered in [[webOS]], currently moving through responsible disclosure channels.
- **[[Wireshark]] Packet Analysis**: The investigative methodology used to observe and document the TV's network traffic.

## Key Takeaways

- LG TVs scan home networks to identify phones, smartwatches, and other hardware.
- Wi-Fi network names, signal strengths, and location data are collected passively.
- ACR fingerprints all on-screen content regardless of input source.
- Audio can be recorded with the screen off; data is stored and uploaded later.
- LG Ad Solutions claims 363 million secondary addressable US devices via this data.
- webOS contains unpatched RCE vulnerabilities under responsible disclosure.
- Mitigation: disconnect LG TVs from the internet; use an external streaming device.
- LG had not commented on the findings at time of publication.

## 🧠 First Principles & Mental Models

- **[[Security Through Obscurity]]**: LG's data collection relies on users not inspecting network traffic — the moment researchers used Wireshark, the full scope became visible, illustrating why obscurity is not a security or privacy control.
- **[[Asymmetric Information]]**: Users consent to vague terms without knowing the true scope of collection; the investigation closes this gap by making the data flows legible to non-experts.

## 🃏 Review Questions

**Q1**: What is the central finding of the Gamers Nexus investigation into LG smart TVs?
**A**: LG TVs engage in extensive covert data collection including home-network device enumeration, ACR fingerprinting across all inputs, and microphone audio capture while in apparent standby mode.

**Q2**: How does LG's standby audio capture work, and what happens when the TV loses internet access?
**A**: The TV records microphone audio even when the screen is off; if network access is unavailable, it stores the recordings locally and uploads them once connectivity is restored.

**Q3**: What practical mitigation do researchers recommend, and why?
**A**: Researchers recommend disconnecting LG TVs from the internet entirely and using an external streaming device, eliminating both the data exfiltration and the webOS RCE attack surface.
