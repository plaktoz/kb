---
source_url: https://www.resonanzcapital.com/insights/every-day-the-market-hires-a-counter-trend-trader
author: Unknown
date: 2026-09-28
---

# Every Day, the Market Hires a Counter-Trend Trader

Two thirds of S&P 500 options now expire the same day. Here's how dealer hedging quietly damps index moves, and what it changes for a trend or vol sleeve.

The tape has been calmer than the news. Rates still unsettled, tariffs unresolved, an equity market leaning hard on a handful of AI names, and yet the S&P has spent long stretches grinding higher in tight ranges with the VIX pinned low.

Part of that is ordinary complacency. Part of it is mechanical, and the mechanical part is the one worth understanding, because it changes what a quiet tape is actually telling you. The mechanism is the option that expires the same day you buy it.

## From a rounding error to two thirds of the market

Zero-days-to-expiry options, the ones that expire the same session, were a niche a decade ago. In 2016 they were roughly 5% of S&P 500 index option volume. After the exchange added Tuesday and Thursday expiries in 2022, and then a full daily cycle, the share climbed fast: past 45% by 2023, through 59% across 2025, and to a record 66% of all SPX options volume in July 2026. On a typical day now, more S&P option volume expires within hours than survives to the next morning.

Source: Cboe (monthly and full-year figures); 2026 point is July. Values rounded. More S&P option volume now expires within hours than survives the night. Share of total SPX option volume made up by same-day (0DTE) contracts. The July 2026 reading of 66% is a record.

The growth is easy to explain and easy to underrate. Retail platforms opened index options to everyone, the day-trading rule that slowed small accounts was repealed in mid-2026, and institutions found same-day options a cheap, precise way to trade a single event or hedge a single session. What's less obvious is what all that same-day trading does to the people on the other side of it.

## Who takes the other side, and what they have to do

Every one of those options is sold by a market maker who doesn't want a directional view. To stay neutral the dealer hedges in the underlying, and the size of that hedge changes as the index moves. That second-order sensitivity is gamma, and it decides which way the dealer is forced to trade.

In the ordinary regime, dealers are net long gamma on these positions, and that forces them to lean against the market. They sell a little as the index rises and buy a little as it falls. Multiply that across two thirds of a very large options market and you get a steady, mechanical bid under dips and offer over rallies. The effect is to fade whatever just happened.

Source: The same machinery that pins a quiet Tuesday can pour fuel on a Thursday sell-off. Schematic. Which regime holds depends on aggregate dealer gamma, which flips from positive to negative once a move is large and fast enough.

This isn't a theory assembled from positioning screenshots. A 2026 study of the S&P found a robust negative relationship between days with heavy same-day option activity and realised index volatility, and traced it to exactly this hedging: dealers carrying positive gamma trade against the move, which shows up as stronger intraday reversals, muted momentum, and lower realised volatility. Cboe's own research and the street's desk notes land in the same place. The index has, in effect, acquired a large counter-trend trader who turns up every session.

## A low VIX is a noisier signal than it used to be

If part of the market's calm is a hedging by-product rather than a considered judgment about risk, a low VIX carries less information than it once did. Some of the quiet is dealers mechanically smoothing the tape between the open and the close. The volatility hasn't gone anywhere. It's been compressed into a narrower window and, as we'll see, stored up for the moment the mechanism reverses.

It also lands unevenly. Same-day flow is concentrated in the index, not in the single stocks inside it, so it damps index volatility more than it damps the volatility of the names. That widening gap between single-stock and index vol is the raw material of the dispersion trade, which Resonanz has written about in "Dispersion Trading and the DSPX Index" and "After the Correlation Shock." One quiet consequence of the 0DTE boom is that it keeps feeding the most crowded relative-value trade in the equity vol market.

Source: Adams et al., "Do S&P500 Options Increase Market Volatility? Evidence from 0DTEs," SSRN 5641974 (2026). The paper's baseline average 10-minute realised volatility is 9.10% annualised; it estimates that the presence of same-day options lowers realised volatility by about 61 basis points, close to 7% of that average.

## The counter-trend trader goes home when it matters

The comfortable regime holds only while dealers are long gamma. Push the index far enough, fast enough, and their positioning flips. Once dealers are short gamma they hedge the other way, selling as the market falls and buying as it rises, which accelerates the move instead of fading it. The same flow that pins the tape on a quiet day pours fuel on a sharp one.

So the honest description of this market isn't "calmer." It's more quiet days punctuated by sharper, faster reversals. August 2024 was the clean example, when a modest unwind tipped into a VIX print above 60 in a single session, and 2026 has had its own smaller versions. The distribution has fatter tails hiding behind a lower average.

## What it changes for a trend or a vol sleeve

For anyone running or sizing systematic strategies, three things follow, and none of them requires taking a view on whether 0DTE is good or bad for markets.

**Short-horizon trend has a headwind.** If the index is being faded every session, fast momentum signals are trading into a mechanical counter-current. The same 2026 research that found lower realised volatility also found muted momentum returns. This doesn't touch multi-month, multi-asset trend, which lives on horizons the intraday hedging never reaches, but it does erode the short end where a lot of equity-only models operate.

**Short volatility and carry look better than they are.** A strategy that sells index volatility earns steadily while dealers are damping the tape, and the low realised vol flatters its Sharpe. What the number doesn't show is that the same strategy is short the gap, exposed to precisely the regime flip the calm is quietly building toward. The premium isn't free. It's payment for standing in front of the reversal.

**A low VIX needs a second reading.** If you size risk off realised or implied volatility, remember that part of the reading is now mechanical supply rather than a consensus that the world is safe. Size to what the position does when the counter-trend bid disappears, not to the average of the quiet days.

## What we're not saying

The academic evidence is genuinely mixed and it's worth being careful with it. The dampening is intraday and regime-dependent, some studies find realised volatility actually runs higher at the open and the close of heavy same-day sessions, and 0DTE is better read as a transmission mechanism than a root cause. The doomsday version, where same-day options blow up the market on their own, doesn't survive contact with the data.

The point that does survive is narrower and more durable. Two thirds of the options market now expires within hours, the hedging that creates leans against the tape on most days and with it on the worst ones, and any strategy whose edge depends on short-horizon momentum or on selling volatility is trading around that flow whether it models it or not.

The market didn't get calmer. It hired someone to fade the crowd, and that someone goes home the moment the move gets big enough to matter.
