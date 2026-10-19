# Statistical Testing Pitfalls in Market Data

## Non-independent observations

Returns may have serial dependence; assets share shocks; multi-day labels overlap. Standard iid standard errors can be misleading. The design must match the sampling and dependence structure.

## Repeated looks and optional stopping

Repeatedly checking a p-value, backtest, or validation score and stopping when it passes changes the false-positive rate. Use pre-specified stopping/validation plans, sequential methods if appropriate, or a clean independent evaluation.

## The winner's curse

Among many noisy estimates, the largest observed effect tends to overstate the true effect. This applies to the best feature, model, parameter, date range, subgroup, or market selected after experimentation.

## Data leakage and look-ahead

Future information can enter through revised macro data, financial statements, index membership, corporate actions, bar timestamp conventions, normalization across the full sample, or overlapping labels. Build an explicit availability-time model for every feature.

## P-hacking and specification search

Trying alternate filters, controls, sample windows, and transformations until a preferred result appears is hidden multiple testing. Record the tried variants and distinguish exploratory analysis from confirmatory testing.

## Multiple comparisons

Correction depends on the family of hypotheses and dependence among tests. False-discovery-rate approaches, family-wise procedures, reality-check/SPA-style tests, deflated performance statistics, and selection-aware bootstrap methods target different problems; none removes the need to report the search process.

## Base rates and low prior probability

When true tradable edges are rare and many claims are tested, even apparently strong nominal significance may produce a low probability that a new result is real. Prior evidence, economic mechanism, independent replication, and realistic costs matter.

As a simple illustration, if only 1% of tested ideas are genuinely useful and a procedure has 5% false-positive rate and 80% power, then among 10,000 tested ideas there are about 100 true positives (80 detected) and 9,900 nulls (495 false positives). Only about 14% of positive results would be true under those assumptions. The numbers are illustrative and assume a simple common test; actual financial search is more complex, but the base-rate lesson remains.

## Backtest return metric pitfalls

Sharpe ratios can be inflated by serial correlation, non-normality, selection, and ignored costs. Annualization formulas assume dependence structures that may not hold. Report raw periodic returns, uncertainty, drawdown/tail behavior, and sensitivity to costs and aggregation.

## Minimum checks

1. What is the independent sampling unit?
2. How many hypotheses/decisions were explored?
3. Was the test period viewed during development?
4. What information was available at each decision timestamp?
5. Were outcomes/labels overlapping?
6. Are uncertainty estimates robust to dependence and heteroskedasticity?
7. What is the effect size after realistic costs?
8. Is there independent replication?

Related: [[Statistical inference for trading]], [[Overfitting controls]], [[Edge validation]], [[ML validation]].
