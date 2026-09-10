# 05 — Liquidity

## What is liquidity?

Liquidity is how easily a market participant can trade size quickly without causing large price movement.

A liquid market has:
- tight spreads
- meaningful depth near top of book
- frequent two-sided participation

## Spread

Spread is the difference between best ask and best bid.

Why it matters:
- it is an immediate trading cost
- wider spread often means lower confidence in current quote quality

## Trading volume

Volume is total traded amount over a period.

Why it matters:
- shows market activity and participation
- helps identify when price moves are supported by real trading

Caution: high daily volume does not guarantee current depth at this exact moment.

## Open interest

Open interest is the amount of outstanding, unsettled contract exposure.

Why it matters:
- indicates how much capital is committed
- helps distinguish short-lived noise from sustained positioning

## How low liquidity creates inefficiencies

Low liquidity can produce:
- exaggerated reactions to small trades
- stale prices that lag new information
- larger gaps between similar related markets
- higher execution costs that block arbitrage correction

Result: observed "probabilities" become noisier and less reliable.

## Practical examples

- A market can print 0.70 on one small trade, but deep executable size may still be around 0.64-0.66.
- Two related markets may disagree because one has active makers while the other has almost no resting orders.

## Why this matters for researchers

Liquidity metrics should be part of any forecasting or trading analysis. Always pair price with:
- spread
- top-of-book depth
- depth within a price band
- recent volume and open interest
