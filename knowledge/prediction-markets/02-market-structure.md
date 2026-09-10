# 02 — Market Structure

## Events

An **event** is the real-world question the market is about, with a deadline and resolution source.

Example:
- "Will Candidate A win state B?"
- Resolution source might be a certified election authority.

## Markets

A **market** packages one event into tradable outcomes.
- Often binary (YES/NO)
- Sometimes multi-outcome (which party wins, which team wins, etc.)

## Outcomes and shares

Traders buy/sell claims on outcomes.
- If outcome happens: winning share settles at $1
- If outcome fails: settles at $0

On many platforms:
- price is quoted from 0 to 1 dollars (or 0 to 100 cents)
- each share has a clear max payoff and clear loss bound

## Settlement and resolution

1. Market closes or transitions to resolution phase
2. Official source is checked per rules
3. Outcome is finalized
4. Contracts settle to payouts

If rules are unclear, trust in price quality falls because settlement risk rises.

## Practical Polymarket framing

- Markets are tied to specific conditions and outcome tokens.
- Order books exist per tradable token/outcome.
- Resolution depends on pre-specified criteria and platform process.

## Practical Kalshi framing

- Contracts are listed as regulated event contracts.
- Resolution criteria are explicit and operationally strict.
- Settlement follows exchange/regulatory procedures in USD.

## Why structure matters for research

Structure determines:
- data schema (event -> market -> outcome)
- comparability across platforms
- interpretation of probabilities
- edge cases (voids, disputes, late corrections)
