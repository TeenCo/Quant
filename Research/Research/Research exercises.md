# Quantitative Research Exercises

These exercises are designed to teach the research process, not produce a deployable strategy. Preserve every run, including null results. Use only data whose terms permit the intended research.

## Exercise 1 — Correlation search and the winner's curse

Generate independent noise features and an independent return target, then search a large feature set and select the top correlation. Repeat the whole experiment many times. Compare the selected in-sample correlation with an untouched out-of-sample correlation. Add autocorrelation or feature dependence and observe how naive uncertainty estimates behave.

**Questions:** How does selected effect size change with the number of trials? What is the effective number of tests when features are correlated? Which results are artifacts of sample reuse?

## Exercise 2 — Point-in-time macro surprise

Choose one macro release with a public real-time release archive and a market series. Build release-time observations using the original vintage, consensus forecast if licensed/available, and the actual surprise. Compare same-day versus pre/post windows while treating simultaneous news and timezone carefully.

**Questions:** Did the signal exist before the release? How does release latency change tradability? Does a result remain after bid/ask and realistic execution timing?

## Exercise 3 — Volatility scaling replication

Implement a simple volatility-scaled version of a transparent baseline portfolio. Freeze the volatility estimator, lag, leverage bounds, and cost model before evaluating. Use rolling chronological splits; compare fixed-risk and scaled versions on the same periods.

**Questions:** Is the improvement driven by lower risk, altered exposure, or better expected returns? How sensitive is it to lag, lookback, cost, and crisis periods? See [[Sources/Moreira Muir 2017]].

## Exercise 4 — Alternative-data lead audit

Select a public non-price series (e.g. weather, shipping, or official release data). Document its generation, publication time, coverage, revisions, license, and likely biases before joining to market outcomes. State one primary hypothesis and a placebo.

**Questions:** Is the data a real-time signal or retrospectively backfilled? Which market has a direct mechanism? Does the relationship survive other proxies and delayed execution? See [[Alternative-data research design]].

Use [[Alternative data experiment design checklist]] and the worked [[Alternative data case study - physical supply chain]] as starting templates.

## Exercise 5 — Hawkes process versus simple arrival baseline

Using permitted event-level data, compare an inhomogeneous Poisson baseline with a Hawkes model for event-arrival intensity. Account for diurnal/session seasonality and common news. Evaluate fit and calibration in chronological holdouts, not just likelihood on the fitted sample.

**Questions:** Does excitation remain after removing seasonality? Are parameters stable across venues/regimes? Does improved intensity prediction improve an execution decision net of costs? See [[Sources/Bacry Mastromatteo Muzy 2015]].

## Exercise 6 — Economic mechanism map

Take an economic mechanism (inventory bottleneck, policy shock, financing constraint) and draw its causal/measurement path to candidate instruments. Identify confounders, alternate proxies, observation/release timestamps, and a falsifiable placebo.

**Questions:** What observation would disprove the hypothesis? Could prices anticipate the event? What is the difference between a causal effect and a useful predictor? See [[Economics-to-market hypotheses]].

For time-series stability and forecast comparisons, see [[Regime-stability and forecast comparison exercise]].

For high-frequency data and execution exercises, see [[Microstructure exercises]].

## Required experiment record

For every exercise log: question, source/data grade, sample and vintage, preprocessing, hypotheses tried, split design, metric and uncertainty, baseline, costs, limitations, and next test. Append a dated entry to [[log]].

## How to judge a completed exercise

Completion means the research design and analysis are reproducible, including null outcomes; it does not require discovering a positive edge. Each memo should distinguish (a) data audit passed/failed, (b) forecast/causal result, (c) implementation result, and (d) what remains unidentified. Students should be rewarded for correctly rejecting an invalid conclusion as well as for a robust finding.
