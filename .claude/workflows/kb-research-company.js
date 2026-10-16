export const meta = {
  name: 'kb-research-company',
  description: 'Deep 6-part investment analysis of a company — saved to research/<ticker>/report.md',
  phases: [
    { title: 'Research', detail: '7 parallel agents: Business Model, Market, MOAT, Financials (x2), Management, Valuation' },
    { title: 'Synthesize', detail: 'Coordinator writes Bull vs. Bear synthesis, saves report, logs to kbm.log.md' },
  ],
}

const ticker = typeof args === 'string'
  ? args.trim().toUpperCase()
  : (args && args.ticker ? String(args.ticker).toUpperCase() : null)

if (!ticker) throw new Error('Ticker symbol required. Usage: /kb-research-company AAPL')

const ANALYST_PERSONA = `You are a senior analyst with a long track record of beating the market. Your goal is deep analysis, grounded in facts and free of bias, to assess a company's long-term investment prospects (decades).

Rules:
- Be objective
- Be concise but precise
- Do not make investment recommendations — only analysis
- Surface fundamental flaws; do not overstate positives
- Use only reputable sources: SEC/EDGAR filings, company IR pages, earnings call transcripts, established financial news outlets — no forums or social media

Company ticker: ${ticker}`

const PART_SCHEMA = {
  type: 'object',
  properties: {
    content: { type: 'string' },
  },
  required: ['content'],
}

phase('Research')
log(`Researching ${ticker} across 6 dimensions in parallel...`)

const [p1, p2, p3, p4a, p4b, p5, p6] = await parallel([
  () => agent(
    `${ANALYST_PERSONA}

## Part 1: Business Model

Research and answer all of the following about ${ticker}:

- How does the company generate income? Describe its mechanism.
- What does the company provide, and what customer needs does it address?
- Who are the typical clients?
- How concentrated is their client base (what % do the top 5 or 10 customers represent)?
- How do they bill (recurring revenue, one-shot, hybrid, or other)?
- Is the business highly cyclical?
- How important is CAPEX? What type (growth/expansion vs. maintenance)? Find CAPEX/revenues for recent years.
- How important is R&D?
- Do they have pricing power? If yes, what kind?
- What are the key challenges ahead for the industry, and what would that mean for companies operating in it?

Return a well-structured markdown section with heading "## Part 1: Business Model".`,
    { label: 'part1-business-model', schema: PART_SCHEMA }
  ),

  () => agent(
    `${ANALYST_PERSONA}

## Part 2: Market and Company Position

Research and answer all of the following about ${ticker}:

- What is the current Total Addressable Market (TAM), and how much of it does the company hold?
- What are the TAM's estimated growth prospects and main growth drivers?
- How does the company position itself to capture these growth prospects?
- What levers can it mobilise to support growth?
- Who are its main competitors?
- What does the company do differently from its competitors?
- Why would a client choose them over a competitor?
- Can this differentiation hold over time?
- How do they intend to gain market share?
- Do they have any form of monopoly? If so — is it due to regulation, lack of competition, or quality and customer loyalty?
- Pre-Mortem: If this company were to lose 50% of its market cap in the next 5 years, what would be the most likely cause? (e.g. technological obsolescence, regulatory change, debt burden, specific competitor disruption)

Return a well-structured markdown section with heading "## Part 2: Market and Company Position".`,
    { label: 'part2-market', schema: PART_SCHEMA }
  ),

  () => agent(
    `${ANALYST_PERSONA}

## Part 3: MOAT

Research and answer all of the following about ${ticker}:

- What is the company's MOAT? Does it have more than one?
- Identify which apply: Network Effect, Switching Cost, Pricing Advantage, Intangible Asset (IP, brand, licences), or Scale.
- Does it have room to maintain that moat for the next 5, 10, or more years?
- Is the company currently improving its MOAT, maintaining it, or eroding it?

Return a well-structured markdown section with heading "## Part 3: MOAT".`,
    { label: 'part3-moat', schema: PART_SCHEMA }
  ),

  () => agent(
    `${ANALYST_PERSONA}

## Part 4a: Financials — Margins and Earnings Quality

Research and answer the following about ${ticker}. Source data from SEC/EDGAR filings, company IR pages, Macrotrends, or established financial news. Cover at least the last 5 years.

- What are the gross profit margins (TTM and trend over 5 years)?
- What are the operating margins (TTM and trend over 5 years)?
- How do these margins compare against main competitors?
- Quality of Earnings: compare Net Income to Free Cash Flow (FCF) over the last 5 years. Is FCF consistently lower than Net Income? If so, why? (Look for heavy Stock-Based Compensation, aggressive revenue recognition, or ballooning inventory.)
- Operating Leverage: as revenue has grown over the last 5 years, have Operating Expenses grown at a slower or faster rate? Does the company profit more from each additional dollar of sales, or is it getting more expensive to grow?

Return a well-structured markdown section with heading "## Part 4: Financials" (subsection: Margins & Earnings Quality).`,
    { label: 'part4a-margins', schema: PART_SCHEMA }
  ),

  () => agent(
    `${ANALYST_PERSONA}

## Part 4b: Financials — Key Metrics and Capital Allocation

Research and answer the following about ${ticker}. Source data from SEC/EDGAR filings, company IR pages, Macrotrends, or established financial news.

- Provide a key metrics table covering: current price, market cap, P/E (TTM, forward, and last 5 years), revenue, operating income, net income, ROIC (TTM and 5-year average), cash, current liabilities, EPS, R&D spending, FCF, operating cash flow, EBITDA, EBIT, CAPEX, WACC.
- Capital Allocation Policy over the last 10 years: how much FCF was returned to shareholders (dividends/buybacks) vs. reinvested (CAPEX/M&A)? Did reinvested capital generate higher ROIC, or is ROIC degrading as they grow?

Return a well-structured markdown subsection continuing "## Part 4: Financials" (subsection: Key Metrics & Capital Allocation).`,
    { label: 'part4b-metrics', schema: PART_SCHEMA }
  ),

  () => agent(
    `${ANALYST_PERSONA}

## Part 5: CEO and Management

Research and answer all of the following about ${ticker}'s leadership:

- Does the current CEO have a track record at this company?
- What is their M&A track record?
- Management Compensation Structure (from proxy statements): what are the specific KPIs used for annual bonuses and long-term stock awards? Are incentives aligned with shareholder value (ROIC, FCF per share) or vanity metrics (gross revenue, adjusted EBITDA)?
- What type of M&A do they pursue — expanding to new territories, or acquiring to strengthen existing expertise?
- Do they have good or bad share buyback strategies?
- What is the CEO or management's ownership stake?
- How do they come across when addressing the public and investors? Confident? Overconfident? Pragmatic? Analytical? Careful? Arrogant?

Return a well-structured markdown section with heading "## Part 5: CEO and Management".`,
    { label: 'part5-management', schema: PART_SCHEMA }
  ),

  () => agent(
    `${ANALYST_PERSONA}

## Part 6: Valuation

Research and answer all of the following about ${ticker}'s valuation:

- Reverse DCF: using the current stock price, what implied annual FCF growth rate is the market pricing in for the next 10 years? Is this realistic given historical performance and TAM?
- Compare the valuation with main competitors.
- What are the main drivers of the current valuation? (Market overreaction? Disappointing reports? Scandal or failed products? Underappreciated product? Unwarranted hype?)

Return a well-structured markdown section with heading "## Part 6: Valuation".`,
    { label: 'part6-valuation', schema: PART_SCHEMA }
  ),
])

phase('Synthesize')
log('All 6 parts complete. Writing synthesis and saving report...')

const p4 = (p4a && p4b)
  ? { content: (p4a.content || '') + '\n\n' + (p4b.content || '') }
  : (p4a || p4b || null)
const parts = [p1, p2, p3, p4, p5, p6].filter(Boolean)
const combinedContent = parts.map(p => p.content).join('\n\n')

// Step 1: Write each part to its own staging file in parallel (one part per agent — manageable prompt size)
await parallel(
  parts.map((p, i) => () => agent(
    `Write the following markdown content to the file research/${ticker}/parts/part-${i + 1}.md (create directories as needed):\n\n${p.content}`,
    { label: `write-part-${i + 1}` }
  ))
)

log('Parts staged. Assembling report and adding Bull vs. Bear synthesis...')

// Step 2: Assembly agent reads from disk — no large content in prompt
await agent(
  `Do the following in order:\n\n1. Read files research/${ticker}/parts/part-1.md through research/${ticker}/parts/part-6.md (read whichever exist).\n\n2. Write a concise "## Bull vs. Bear" synthesis section distilling the key investment thesis tension: 3–5 bull points and 3–5 bear points in bullet form. Be objective — no recommendations.\n\n3. Assemble the full report in this order and save to research/${ticker}/report.md:\n   - "# ${ticker} — Investment Analysis"\n   - "Analysed: <today's date YYYY-MM-DD>"\n   - The Bull vs. Bear synthesis section\n   - The content of part-1.md through part-6.md in order\n\n4. Append this row to kbm.log.md (add to the existing table — do not overwrite):\n   | <today's date YYYY-MM-DD> | research/${ticker}/report.md | research |`,
  { label: 'assemble-and-log' }
)

log(`Report saved to research/${ticker}/report.md`)
return { ticker, report: `research/${ticker}/report.md` }
