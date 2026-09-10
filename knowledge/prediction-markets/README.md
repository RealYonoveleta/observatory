# Prediction Markets

Prediction markets are markets where contracts pay based on whether a future event happens. Traders buy and sell contracts tied to outcomes like elections, economic releases, court rulings, weather thresholds, or product launches.

If a YES contract pays $1 when an event happens and $0 otherwise, then a market price near $0.63 is commonly read as "about a 63% market-implied chance."

## What are prediction markets?

A prediction market is an exchange for probabilities:
- **Question**: "Will X happen by date Y?"
- **Contract**: YES/NO (or multi-outcome) claim on that question
- **Price**: continuously updated estimate of likelihood
- **Resolution**: contract settles to a final payoff after the outcome is known

## Why do they exist?

They exist because useful information is scattered across many people. Markets create incentives for people to reveal what they know by risking capital on their beliefs.

Core idea from the prediction-market literature (including Robin Hanson): prices can aggregate dispersed information faster and more continuously than polls or committees.

## Why are they useful?

Prediction markets are useful because they:
- turn opinions into **quantified, comparable probabilities**
- update quickly when new information arrives
- produce a live, auditable forecast history
- align incentives (being correct matters financially)
- help organizations make decisions under uncertainty

## What problems do they solve?

They help with problems where decisions depend on uncertain future events:
- planning under uncertainty (policy, product, operations)
- comparing competing scenarios on one probability scale
- reducing overconfidence by forcing probabilistic thinking
- identifying where market consensus and narrative disagree

## Role in forecasting

Prediction markets are a practical forecasting engine:
- **Prices** are probability estimates
- **Order flow** shows who is updating beliefs
- **Liquidity conditions** tell you how reliable price signals may be
- **Resolution data** enables calibration and scoring of forecasts

For researchers, they are both a forecasting tool and a dataset about belief formation.

## Learning path in this directory

1. `01-introduction.md` — foundational intuition and history
2. `02-market-structure.md` — events, contracts, outcomes, settlement
3. `03-market-pricing.md` — why prices map to probabilities
4. `04-order-books.md` — matching, bids/asks, execution, market makers
5. `05-liquidity.md` — spread, depth, volume, open interest
6. `06-information-and-markets.md` — news, information flow, aggregation
7. `07-market-efficiency.md` — when markets are right/wrong and why
8. `08-calibration.md` — forecast quality and Brier-score intuition
9. `09-polymarket.md` — platform mechanics and research data framing
10. `10-kalshi.md` — regulated event contracts and platform comparison

Then use:
- `glossary.md` for quick term lookups
- `concepts.md` for integrated conceptual understanding
- `learning-resources.md` for primary sources and study sequence
- `notes.md` as a structured study and research checklist
