# 04 — Order Books

## Why this chapter is central

If you only read last traded price, you miss most of market mechanics. Order books show *how* probability estimates are formed in real time.

## What is an order book?

An order book is a live queue of:
- **Bids** (buy interest)
- **Asks** (sell interest)

Each level has price and size.

Simple snapshot:

```text
Asks (sell)
0.64 | 300
0.63 | 180   <- best ask
-----------------------
0.62 | 220   <- best bid
0.61 | 400
Bids (buy)
```

Interpretation:
- You can buy immediately at 0.63 (best ask).
- You can sell immediately at 0.62 (best bid).
- Spread is 0.01.

## Bid and ask

- **Bid**: highest price any buyer currently offers.
- **Ask**: lowest price any seller currently offers.
- **Spread**: ask - bid.

Tighter spreads generally mean lower immediate trading cost and better liquidity.

## Matching and trade execution

A trade occurs when a buy order and sell order are compatible.

- If you submit a buy order at or above best ask, it executes against resting asks.
- If you submit a sell order at or below best bid, it executes against resting bids.

Large orders may execute across multiple levels ("walking the book").

## Market orders

A market order prioritizes speed over price.

- **Pros**: immediate execution.
- **Cons**: uncertain fill price, especially in thin books.

Example:
- Best ask 0.63 for 180 shares, next ask 0.64 for 300.
- Market buy 400 shares fills partly at 0.63 and remainder at 0.64.
- Average price is worse than top-of-book quote.

## Limit orders

A limit order sets your worst acceptable price.

- Buy limit at 0.62 means "do not pay more than 0.62."
- Sell limit at 0.64 means "do not sell below 0.64."

Benefits:
- price control
- potential to earn spread as passive liquidity

Tradeoff:
- order might not fill.

## Time priority and queue position

When multiple orders share a price, earlier orders usually execute first.

Why researchers care:
- queue position affects fill probability
- execution quality depends on both price and time in queue

## Market makers

Market makers post both bids and asks to keep trading continuous.

They help by:
- reducing spreads
- increasing available depth
- smoothing price discovery

They take on risks:
- adverse selection (being picked off by informed traders)
- inventory risk (holding too much YES or NO exposure)

## Reading order-book signals

Useful practical signals:
- **Depth imbalance**: more size on one side can indicate short-term pressure.
- **Spread widening**: often means uncertainty or reduced participation.
- **Repeated replenishment**: suggests active liquidity provider behavior.
- **Sudden level removal**: can precede fast repricing around news.

## Common misconceptions

1. **"Top price equals fair probability."**
   - In thin markets, tiny size can set the top price.

2. **"Volume alone describes liquidity."**
   - Current depth and spread matter more for immediate execution.

3. **"Market orders are always fine."**
   - They can be expensive in low-depth books.

4. **"No trade means no information."**
   - Quote updates and canceled orders also carry information.

## Why order books matter for prediction-market research

Order books let you study:
- information arrival at sub-minute granularity
- microstructure noise vs real belief change
- liquidity-adjusted probability signals
- transaction-cost-aware backtests

Without order-book context, probability inference can be misleading.
