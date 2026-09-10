# Learning Resources

## Beginner

### Polymarket Documentation (Getting Started, Market Data, CLOB/API docs)
- **Why valuable**: Explains platform objects, markets, outcomes, order books, and data endpoints in concrete terms.
- **Teaches**: How event markets are represented operationally; how to access market and order-book data.
- **When to read**: First, alongside `02-market-structure.md` and `04-order-books.md`.
- **Start with**: `https://docs.polymarket.com/`

### Kalshi Learn + Market Integrity / Regulation pages
- **Why valuable**: Clear educational framing of event contracts in a regulated U.S. exchange context.
- **Teaches**: Contract lifecycle, settlement, and CFTC-style market safeguards.
- **When to read**: Early, after basic prediction-market intuition.
- **Start with**: `https://kalshi.com/learn` and `https://kalshi.com/market-integrity/regulation`

### CFTC educational material on event contracts / derivatives market oversight
- **Why valuable**: Gives the regulatory context for U.S. event contract markets.
- **Teaches**: Why market design, surveillance, and compliance rules exist.
- **When to read**: Early for researchers comparing regulated vs non-regulated platforms.
- **Start with**: `https://www.cftc.gov/`

### Tetlock & Gardner, *Superforecasting*
- **Why valuable**: Builds forecasting mindset and calibration intuition without heavy math.
- **Teaches**: Probabilistic thinking, updating beliefs, avoiding common judgment errors.
- **When to read**: Early-to-mid stage before deeper quantitative modeling.

## Intermediate

### Robin Hanson papers and writing archive
- **Why valuable**: Foundational arguments for information aggregation and market design.
- **Teaches**: Why incentive-compatible markets can reveal distributed knowledge; LMSR and decision-market ideas.
- **When to read**: After basic market mechanics.
- **Suggested entry points**:
  - *Combinatorial Information Market Design* (2003)
  - *Logarithmic Market Scoring Rules for Modular Combinatorial Information Aggregation* (2007)
  - Archive/index: `https://mason.gmu.edu/~rhanson/`

### Wolfers & Zitzewitz (2004), “Prediction Markets” (Journal of Economic Perspectives)
- **Why valuable**: Classic survey connecting theory and empirical evidence.
- **Teaches**: Accuracy evidence, use cases, limitations, and policy questions.
- **When to read**: Intermediate synthesis step.

### Berg, Nelson & Rietz on Iowa Electronic Markets
- **Why valuable**: Early empirical benchmark for election and macro forecasting markets.
- **Teaches**: Practical market performance and historical evidence base.
- **When to read**: After understanding basic contract mechanics.

## Advanced

### Market microstructure texts (order books, liquidity, execution)
- **Why valuable**: Needed for rigorous interpretation of price signals and slippage.
- **Teaches**: Depth dynamics, spread formation, adverse selection, maker-taker behavior.
- **When to read**: Once basic prediction-market concepts are comfortable.

### Proper scoring rules and calibration literature (Brier, reliability diagrams)
- **Why valuable**: Turns “good forecast” intuition into measurable evaluation.
- **Teaches**: Calibration vs sharpness, scoring-rule tradeoffs, benchmark design.
- **When to read**: Before building forecasting models.

### Event-study and information-arrival methods from financial economics
- **Why valuable**: Useful for analyzing how markets digest news over time.
- **Teaches**: Measuring reaction speed, drift, and over/underreaction patterns.
- **When to read**: During quantitative research design.

---

## Suggested sequence

1. Polymarket docs + Kalshi Learn
2. This directory (`01` to `10`)
3. *Superforecasting*
4. Hanson + Wolfers/Zitzewitz
5. Microstructure and calibration/statistical evaluation resources
