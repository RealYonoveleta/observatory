# 03 — Market Pricing

## Why prices represent probabilities

In a binary event contract that pays $1 on YES and $0 on NO, a rational buyer compares price to expected payout.

If traders collectively think an event is about 65% likely, YES often trades near 0.65.

This is why market prices are treated as **implied probabilities**.

## How to interpret probabilities

- 0.20 means market sees event as unlikely, not impossible.
- 0.50 means high uncertainty or balanced evidence.
- 0.85 means event is considered likely, but still not certain.

These are live beliefs, not guarantees.

## YES and NO relationship

Intuition:
- YES and NO are complementary claims on the same event.
- If frictionless, YES + NO should be close to $1 in binary markets.

In real markets, fees, risk limits, and liquidity frictions can create small deviations.

## Market expectations and repricing

Prices move when participants update beliefs from new information.

Example:
- Before economic release: 0.47
- Strong report appears: buyers lift asks, price jumps to 0.61

The move is the market’s revised probability estimate.

## Mispricing intuition

Mispricing can appear when:
- liquidity is thin
- many participants share the same bias
- information is costly or slow to process
- execution constraints prevent arbitrage

Not every disagreement with your model is mispricing; you must test whether a trade was actually executable after costs.

## Why pricing matters for research

Price series let researchers study:
- forecast updates through time
- reaction speed to news
- cross-market consistency
- calibration after settlement outcomes are known
