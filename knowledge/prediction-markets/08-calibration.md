# 08 — Calibration

## What calibration means

Calibration asks: when markets say "X% likely," does that outcome happen about X% of the time over many similar cases?

Example:
- If 100 events were priced near 70%, and about 70 resolved YES, that bin is well calibrated.

## Why calibration matters

Calibration is essential because prediction markets are used as probability forecasts.

A market can be exciting and liquid, yet still provide biased probability estimates. Calibration checks forecast reliability directly.

## Why prediction markets are evaluated this way

Prediction markets generate explicit numeric probabilities and later produce objective outcomes through resolution. That makes them naturally testable with forecast metrics.

Calibration helps compare:
- market forecasts vs models
- early vs late market prices
- different platforms or event types

## Brier Score (intro only)

The Brier Score is a common measure of probabilistic forecast accuracy.

Intuition:
- lower is better
- confident wrong forecasts are penalized heavily
- confident correct forecasts are rewarded

For binary outcomes, it measures squared distance between forecast probability and final outcome (1 or 0).

## Common misconceptions

1. **"One wrong 90% call means bad calibration."**
   - No. High-probability events still fail sometimes.

2. **"Calibration and sharpness are the same."**
   - Calibration = reliability; sharpness = how concentrated/confident forecasts are.

3. **"Only final price matters."**
   - Path calibration (how probabilities evolved) can also be informative.

## Research relevance

Calibration connects market mechanics to measurable forecast quality. It is the bridge from descriptive market analysis to rigorous evaluation.
