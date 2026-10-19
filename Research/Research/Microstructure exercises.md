# Market Microstructure Research Exercises

All exercises are educational. Do not infer profitability from predictive fit alone. Use only properly licensed data and preserve event timing and the full trial log.

## 1. Reconstruct and audit a small book

Use a short sequence of book snapshots or messages. Reconstruct bids/asks in sequence, then check crossed states, nonnegative depth, missing sequences, and quote continuity. Compare to provider snapshots.

**Deliverable:** data dictionary, reconstruction invariants, error counts, event-vs-receive timestamp chart.

## 2. Quote midpoint versus executable prices

Compare a simple signal's next-period mid-price return to returns computed from executable bid/ask prices. Add conservative latency and fees.

**Question:** How much apparent edge is spread capture, stale quotes, or impossible fills?

## 3. Depth imbalance baseline

Define one pre-specified top-of-book imbalance feature and forecast a short-horizon mid-price change. Use chronological validation, event-time awareness, and a simple baseline.

**Question:** Does the feature survive latency and spread? How sensitive is it to depth level and venue?

## 4. Liquidity replenishment/resiliency

Identify book depletion events and measure depth recovery over pre-specified intervals. Compare quiet and high-volatility periods, while accounting for event-size and time-of-day differences.

**Question:** Is recovery predictive of subsequent costs or merely correlated with activity regime?

## 5. Event intensity: Poisson versus Hawkes

Model event arrivals with time-of-day intensity first, then test if a Hawkes model improves held-out calibration. Evaluate parameter stability across sessions.

**Question:** Does self-excitation remain after seasonality and common news controls? Does it improve a feasible execution decision?

## 6. Implementation shortfall decomposition

For a hypothetical order schedule, estimate arrival-price shortfall, spread, fees, market movement, fill rate, and opportunity cost. Vary urgency and order size under a transparent impact assumption.

**Question:** At what cost/capacity does a forecast stop being useful?

## Required report

Log feed/source grade, licensing, market/venue, timestamp semantics, exact filters, all tested horizons/depths/features, chronological split, uncertainty approach, execution assumptions, nulls, and limitations. Append a timestamped [[log]] entry.

## General execution-simulator checks

Keep the simulator's matching and market-data assumptions explicit. For passive orders, model queue priority, cancellation, partial fills, and adverse selection; for aggressive orders, consume available depth and include impact/fees. Do not grant a fill merely because a bar touches a limit price. Validate a small hand-built event sequence against expected fills before running a large backtest. Treat simulated fills as model output and stress against conservative latency/queue assumptions.
