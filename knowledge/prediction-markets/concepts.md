# Core Concepts in Prediction Markets

## 1. Event Contracts

### What it is
A contract whose payoff depends on whether a defined event occurs.

### Why it matters
It creates a standard unit for expressing beliefs about the future.

### Practical example
"Will CPI YoY be above 3.0% in December?" YES pays $1 if true, $0 if false.

### Common misconception
"It is just gambling." In research use, the key function is information aggregation and probabilistic forecasting.

---

## 2. Price as Probability

### What it is
In binary contracts with clear settlement, price is commonly interpreted as market-implied probability.

### Why it matters
It gives an always-updating forecast that is directly machine-readable.

### Practical example
YES at $0.42 implies roughly 42% chance, before considering frictions.

### Common misconception
"Price is guaranteed truth." Prices are estimates that can be noisy, biased, or liquidity-constrained.

---

## 3. Market Microstructure

### What it is
The mechanics of how orders meet: order books, bids, asks, matching, and execution.

### Why it matters
The same "probability" can mean different things in thick vs thin books.

### Practical example
A price jump from 0.55 to 0.62 on tiny size is weaker evidence than the same move on large traded volume.

### Common misconception
"Last price tells the full story." You also need depth, spread, and trade size.

---

## 4. Liquidity

### What it is
How easy it is to trade quickly at stable prices.

### Why it matters
Higher liquidity usually improves price quality and lowers execution cost.

### Practical example
A 1-cent spread with deep quotes is usually more informative than a 12-cent spread with little depth.

### Common misconception
"High volume always means high liquidity." Volume can be high over a day while the live order book remains thin.

---

## 5. Information Flow

### What it is
How news, private signals, and interpretation enter prices via trades and order updates.

### Why it matters
Prediction markets are valuable because they convert distributed information into one evolving forecast.

### Practical example
An official court filing causes immediate repricing before mainstream summaries appear.

### Common misconception
"Markets only react to public headlines." Much repricing comes from interpretation speed and specialized domain knowledge.

---

## 6. Incentives and Participants

### What it is
Different participant motives: speculators, hedgers, market makers, and noise traders.

### Why it matters
Participant mix shapes price discovery, stability, and temporary inefficiencies.

### Practical example
Market makers narrow spreads; informed speculators push prices toward fundamentals.

### Common misconception
"Everyone is trying to forecast honestly." Some participants seek liquidity, entertainment, hedging, or influence.

---

## 7. Resolution and Settlement Quality

### What it is
The rule system that maps messy reality to final contract payout.

### Why it matters
Weak or ambiguous rules create dispute risk and reduce trust in prices.

### Practical example
A contract specifies exact source (for example, BLS release) and timestamp cutoff.

### Common misconception
"If event is obvious, rules do not matter." Even obvious events need precise operational definitions.

---

## 8. Efficiency and Mispricing

### What it is
Efficiency means prices quickly reflect available information; mispricing is deviation from best estimate.

### Why it matters
Research often studies when and why deviations appear.

### Practical example
Weekend liquidity drops can allow larger temporary pricing errors.

### Common misconception
"Any mismatch with my belief is inefficiency." You need evidence, benchmarking, and execution feasibility.

---

## 9. Calibration

### What it is
Whether stated probabilities match long-run realized frequencies.

### Why it matters
Calibration is a core criterion for forecast quality.

### Practical example
Events priced around 70% should happen about 70 times out of 100 over many similar cases.

### Common misconception
"One bad call means poor calibration." Calibration is a population-level property, not a single-event outcome.

---

## 10. Why Researchers Use Prediction Markets

### What it is
A combined forecasting and behavioral data system.

### Why it matters
You get both outcome predictions and high-frequency traces of belief updates.

### Practical example
Researchers can compare pre-news and post-news price paths, spread changes, and order-book depth shifts.

### Common misconception
"Prediction-market data is only for traders." It is also valuable for economics, ML, decision science, and policy research.
