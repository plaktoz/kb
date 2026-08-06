## Part 1: Business Model

*Sources: Alphabet Inc. 10-K for fiscal year ended December 31, 2025 (filed February 5, 2026, SEC CIK 0001652044); Alphabet Q4 2025 Earnings Release; Statcounter Global Search Engine Market Share (July 2026); fourweekmba.com analysis; Yahoo Finance.*

---

### How the Company Generates Income

Alphabet operates three reportable segments: **Google Services**, **Google Cloud**, and **Other Bets**.

**Google Services** (85.2% of FY2025 revenue, $342.7B) contains two distinct income engines:

1. **Advertising (73.2% of total revenue, $294.7B in FY2025)** — Google runs a real-time auction system across its properties. Advertisers bid on keywords and audience signals; placement is determined by bid amount multiplied by a Quality Score. Revenue is recognised per click (Search, Display) or per thousand impressions (YouTube, Display). The model is fundamentally a two-sided market: Google provides free consumer-facing services (Search, Gmail, Maps, YouTube, Android, Chrome) to attract billions of users, then monetises their attention and behavioural data by selling targeted access to those users to advertisers. Importantly, Google collects the full chain: it owns the search engine, the browser (Chrome), the mobile OS (Android), the video platform (YouTube), and the advertising technology stack (AdMob, AdSense, Google Ad Manager). This vertical integration eliminates intermediaries and gives Google structural control over pricing and distribution.

2. **Subscriptions, Platforms, and Devices ($48.0B in FY2025)** — YouTube Premium/TV/Music, Google One (storage + Gemini model access), Google Workspace, Google Play app store commissions, and Pixel hardware sales.

**Google Cloud** (14.6% of FY2025 revenue, $58.7B) sells IaaS, PaaS, and SaaS to enterprises. Revenue is consumption-based and subscription-based. Google Cloud became profitable at the segment level, generating $13.9B in operating income in FY2025 (vs. $6.1B in FY2024), an operating margin of approximately 23.7%.

**Other Bets** ($1.5B revenue, ($7.5B) operating loss in FY2025) — a portfolio of early-stage ventures (Waymo autonomous vehicles, Verily life sciences, etc.) cross-subsidised by the core business. Not material to current economics.

---

### Revenue by Segment (FY2023–2025, $M)

| Segment | FY2023 | FY2024 | FY2025 |
|---|---|---|---|
| Google Search & other | 175,033 | 198,084 | 224,532 |
| YouTube ads | 31,510 | 36,147 | 40,367 |
| Google Network | 31,312 | 30,359 | 29,792 |
| **Google advertising total** | **237,855** | **264,590** | **294,691** |
| Subscriptions, platforms, devices | 34,688 | 40,340 | 48,030 |
| **Google Services total** | **272,543** | **304,930** | **342,721** |
| Google Cloud | 33,088 | 43,229 | 58,705 |
| Other Bets | 1,527 | 1,648 | 1,537 |
| Hedging / other | 236 | 211 | (127) |
| **Total revenues** | **307,394** | **350,018** | **402,836** |

---

### What the Company Provides and What Customer Needs It Addresses

| Product / Service | User Need Addressed |
|---|---|
| Google Search | Information retrieval; purchase research; navigation |
| YouTube | Entertainment; learning; creator monetisation |
| Gmail, Drive, Docs | Productivity; communication |
| Maps, Android, Chrome | Navigation; mobile OS; web browsing |
| Google Cloud (GCP) | Enterprise compute, storage, AI/ML infrastructure |
| Workspace | Business collaboration and productivity |
| Pixel / Nest | Consumer hardware |

The asymmetry is structural: consumer products are provided at zero monetary cost; the actual paying customers are **advertisers** (businesses paying for access to user intent signals) and **cloud customers** (enterprises paying for compute).

---

### Typical Clients and Client Concentration

**Advertising clients:** Millions of businesses globally, from individual SMBs using self-serve Google Ads to large agencies managing Fortune 500 brand campaigns. The base is extraordinarily fragmented. In Alphabet's 10-K history, no single advertiser has ever represented 10% or more of revenues. The lack of concentration is a fundamental feature: it prevents any one customer from exercising leverage and provides revenue stability.

**Cloud clients:** Enterprises, mid-market companies, public sector, and startups. Similarly no disclosed concentration above 10%.

**Key caveat:** Apple is not an advertiser, but is a critical revenue-sharing distribution partner. The Apple-Google default search deal (Google pays Apple ~$15–18B per year to be the default engine on Safari and iOS) inflates Search revenues materially. This arrangement is at legal risk following the August 2024 DOJ antitrust ruling that found Google holds an illegal monopoly in general search. The remedy phase (ongoing) could force termination of such exclusivity agreements.

---

### Billing Model

| Revenue Type | Billing Mechanism |
|---|---|
| Search & Network advertising | Performance-based auction (CPC/CPM); invoiced monthly post-delivery |
| YouTube brand advertising | CPM reservation and auction; can include multi-quarter upfront deals |
| YouTube subscriptions | Recurring monthly/annual (consumer subscription) |
| Google Workspace | Per-seat monthly/annual SaaS subscription |
| Google One | Monthly/annual consumer subscription |
| Google Cloud (IaaS/PaaS) | Consumption-based with committed-use contracts available |
| Google Play | Revenue share on in-app purchases (typically 15–30% cut) |
| Pixel hardware | One-shot point-of-sale |

The dominant model is **performance-based variable revenue** (advertising), which is inherently not predictable quarter-to-quarter. The recurring revenue components (Cloud, Workspace, YouTube subscriptions) are growing but still represent a minority.

---

### Cyclicality

The business is **moderately cyclical**, primarily through its advertising engine. Digital advertising correlates with corporate marketing budgets, which contract during economic downturns.

Evidence of cyclicality: In FY2022, overall revenue growth fell to ~9.8% (from 41% in 2021) as advertisers pulled back; YouTube advertising revenue declined outright (-2%) in 2022. The Google Network segment (AdSense/AdMob) has been declining since 2023 as the broader programmatic ad market contracts and as advertisers shift spend to owned-and-operated properties.

**Mitigant:** Search advertising is relatively recession-resilient vs. display/brand advertising, because it captures commercial intent at the bottom of the purchase funnel — advertisers maintain spend on high-ROI terms even in downturns. However, it is not immune.

---

### CAPEX: Magnitude, Trend, and Type

CAPEX has tripled in three years, becoming one of the defining financial characteristics of Alphabet.

| Year | CAPEX ($M) | Total Revenue ($M) | CAPEX / Revenue |
|---|---|---|---|
| FY2020 | 24,640 | 182,527 | 13.5% |
| FY2021 | 31,485 | 257,637 | 12.2% |
| FY2022 | 32,251 | 282,836 | 11.4% |
| FY2023 | 52,535 | 307,394 | 17.1% |
| FY2024 | 91,447 | 350,018 | 26.1% |
| FY2025 | ~91,400* | 402,836 | ~22.7% |

*Per 10-K: "Capital expenditures, which primarily reflected investments in technical infrastructure, were $91.4 billion for the year ended December 31, 2025."*

**Type of CAPEX:** Overwhelmingly **growth/expansion** in nature. The primary drivers are:
- Custom AI chips (TPUs — Tensor Processing Units) for training and inferencing Gemini and other AI models
- Data centre construction and expansion across multiple continents
- Networking infrastructure and undersea cables
- Server hardware for Search, YouTube, and GCP

This is not maintenance capex. Google is building infrastructure capacity ahead of anticipated AI demand. The acceleration reflects a strategic bet that compute infrastructure will be a durable competitive advantage. The risk is a substantial increase in fixed-cost base; depreciation on property and equipment grew from $11.9B (FY2023) to $21.1B (FY2025).

---

### R&D: Importance and Scale

R&D is central to Alphabet's competitive position. The company has spent over $200 billion on R&D over the past five years, per its own disclosures.

| Year | R&D ($M) | Revenue ($M) | R&D / Revenue |
|---|---|---|---|
| FY2023 | 45,427 | 307,394 | 14.8% |
| FY2024 | 49,326 | 350,018 | 14.1% |
| FY2025 | 61,087 | 402,836 | 15.2% |

R&D funds: Gemini family of AI models; DeepMind (fundamental AI research, AlphaFold, AlphaStar); Google Brain; TPU hardware design; Android/Chrome development; quantum computing (Willow); and moonshots in Other Bets (Waymo, Verily). R&D intensity at 15% of revenue is higher than most software companies and reflects the reality that Alphabet's core products face existential replacement risk from AI — it must invest heavily to both build and cannibalise its own search business before a competitor does.

---

### Pricing Power

Alphabet has **strong, structural pricing power** in its core advertising segment, with meaningful limitations.

**Sources of pricing power:**

1. **Auction mechanism with no price ceiling**: In Google Search, Alphabet does not set prices — advertisers bid against each other in a second-price auction. As more advertisers compete, yields rise automatically without Google having to raise stated prices. In FY2025, cost-per-click grew 7% year-over-year on 6% volume growth, demonstrating ongoing yield expansion.

2. **Declining Traffic Acquisition Cost rate**: Google's TAC rate (TAC as % of advertising revenues) has been structurally declining as revenue mix shifts from Google Network (where Google shares ~70–80% of revenues with publishers) to Google's own properties (Search, YouTube) where it retains full economics. TAC was $54.9B in FY2024 and $59.9B in FY2025, but as a percentage of $294.7B in advertising revenue it represents ~20.3%, down from historical levels above 23%.

3. **Essential channel for advertisers**: Google Search reaches users expressing commercial intent. For most performance advertisers (e-commerce, finance, legal, travel, healthcare), Google Search is not optional — there is no substitute channel with equivalent conversion rates. This gives Google leverage to raise effective prices without losing volume.

4. **Cloud pricing**: More competitive. Google Cloud competes on price as a #3 player against AWS and Azure, using aggressive discount strategies to win workloads. Pricing power here is limited.

**Constraints on pricing power:**
- The DOJ antitrust ruling threatens the exclusive default-search distribution model, which is a core mechanism by which Google controls supply (query volume).
- AI search interfaces (Google AI Overviews, ChatGPT) may reduce click volume over time if users receive answers without clicking ads.
- Cookie deprecation and privacy regulations reduce targeting precision, which could reduce advertiser willingness to pay.

---

### Key Challenges Ahead for the Industry

**1. Generative AI disruption of the search-advertising link**
The 30-year-old model of search — user queries → ranked links → advertiser clicks — is under structural pressure from AI-generated direct answers. Google is responding with AI Overviews in Search, but every AI answer that eliminates a click also eliminates an ad impression. The monetisation model for zero-click AI answers is unproven and unlikely to match current CPCs. Competitors (OpenAI's SearchGPT, Microsoft Copilot, Perplexity) are growing. The industry faces a secular shift in how users retrieve information, with unclear advertising economics at the destination.

**2. Antitrust enforcement risk**
The August 2024 US District Court ruling (United States v. Google) found Google holds an illegal monopoly in general search and general text advertising. The remedy phase is live and ongoing. Potential remedies include: forced divestiture of Chrome or Android; prohibition on default-search exclusivity payments (Apple deal); mandatory data-sharing with competitors. Any of these would be structurally damaging. Separately, the DOJ filed a second antitrust suit targeting Google's advertising technology stack (DV360, Google Ad Manager); the remedy sought is full divestiture of AdTech. EU Digital Markets Act enforcement adds parallel regulatory pressure in Europe.

**3. CAPEX spiral and cloud competition**
Every major tech company is simultaneously investing tens of billions in AI infrastructure (Microsoft $80B+/year, Meta $60–65B, Amazon $75B+). The industry is in a capex arms race that compresses free cash flow across the board. For Google specifically, the transition to AI-first products requires compute at a scale that is challenging to maintain profitably.

**4. YouTube competition for attention**
TikTok, Instagram Reels, and Twitch compete directly for creator and viewer time on YouTube. While YouTube advertising grew 11.7% in FY2025, the short-form video ecosystem is fragmenting attention.

**5. Digital advertising cyclicality and regulatory headwinds on targeting**
Deprecation of third-party cookies (delayed but underway), GDPR enforcement fines, and state-level US privacy laws all erode the behavioural targeting precision that underpins CPM pricing. Less precise targeting leads to lower advertiser willingness to pay, putting structural pressure on CPM rates over time.
