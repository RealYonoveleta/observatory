# Study Guide Notes

## Key takeaways

- Prediction markets turn uncertain future events into tradable probability signals.
- Prices are useful probability estimates, but interpretation depends on liquidity and microstructure.
- Resolution quality is not administrative detail; it is central to market credibility.
- Market forecasts improve when incentives reward accurate information revelation.
- Forecast quality should be judged over many events (calibration), not by anecdotes.

## Mental models

1. **Market as sensor network**
   - Each trader contributes partial information.
   - Price is the continuously updated fused signal.

2. **Price = belief under constraints**
   - A price reflects beliefs filtered through risk limits, liquidity, and execution costs.

3. **Order book as x-ray**
   - Last trade is the headline; depth/spread/order flow are the internal anatomy.

4. **Resolution rules as protocol layer**
   - Ambiguous rules create settlement risk, lowering signal quality upstream.

5. **Forecasting loop**
   - Hypothesis -> trade/quote -> price update -> feedback -> revised belief.

## Questions to investigate

- When does market-implied probability diverge most from benchmark forecasts?
- How much do spread and depth predict near-term forecast error?
- Do markets underreact or overreact to different news categories?
- How does trader concentration affect information aggregation quality?
- Are late-stage prices systematically better calibrated than early-stage prices?

## Topics requiring deeper study

- Proper scoring rules beyond Brier score
- Bayesian updating and base-rate integration
- Adverse selection and inventory risk in market making
- Cross-market arbitrage and constraint propagation
- Behavioral biases (herding, partisan motivated reasoning, overconfidence)
- Mechanism design differences: CLOB vs automated market makers
- Regulated vs non-regulated market architecture and data implications

## Practical next steps for engineers

- Build a market data dictionary (event, market, token, resolution fields).
- Create a repeatable ingestion pipeline for prices, order books, and resolution outcomes.
- Track a small watchlist of markets daily and write explicit probability updates.
- Start calibration tracking with simple bins (10%, 20%, ... 90%).
- Record known data-quality edge cases (halted markets, ambiguous resolutions, sparse books).
