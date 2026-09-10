# 09 — Polymarket Overview

## Research-oriented framing

Polymarket is a high-activity prediction market platform where many event contracts trade continuously. For researchers, it is both a forecasting venue and a rich market microstructure dataset.

## Market structure

- Events are expressed as clearly scoped questions with deadlines.
- Markets are often binary YES/NO, though multi-outcome structures also appear.
- Outcomes map to tradable tokens/instruments.

## Events, markets, and resolution

Key research objects:
- event metadata (question, category, dates)
- market/outcome objects (labels, tokens, status)
- resolution criteria and final result

Resolution quality is central: unclear criteria can contaminate downstream calibration analysis.

## Order books and execution

Polymarket documentation describes CLOB-style order-book access for live bids/asks and order management.

For researchers:
- top-of-book price is only one feature
- depth and spread are needed to assess probability quality
- execution constraints shape observed pricing dynamics

## Volume and liquidity

Useful fields include:
- traded volume
- liquidity/depth indicators
- price history

Use these to separate strong repricing (broad participation) from thin-book noise.

## APIs available (conceptual map)

Polymarket docs expose multiple API surfaces (for example, market discovery/metadata and order-book/trading interfaces). Typical categories:
- market/event discovery
- current quotes and order books
- historical prices and market states
- trade/order management endpoints

Primary entry point: `https://docs.polymarket.com/`

## Data available for research

Typical research pipeline uses:
- static reference data: event/market definitions
- time series: price, volume, status changes
- microstructure: order-book snapshots/depth
- terminal labels: final resolved outcomes

## How researchers should think about Polymarket

Treat Polymarket as:
1. **A forecasting signal** (implied probabilities)
2. **A behavior lab** (how information enters prices)
3. **A microstructure environment** (liquidity-constrained belief expression)

Best practice: never analyze price in isolation; always condition on liquidity, resolution quality, and event type.
