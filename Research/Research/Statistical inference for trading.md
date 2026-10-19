# Statistical Inference for Trading Research

Statistical evidence is only as trustworthy as its sampling design, data provenance, timing, and search history. Financial returns are noisy and dependent, and the researcher is often selecting among many plausible hypotheses. This note organizes the key inference problems before treating a pattern as a candidate edge.

## 1. Define the target before calculating significance

Specify the estimand (what quantity is being estimated), sample, universe, decision time, holding period, benchmark, and return/cost convention. Common targets include conditional expected return, rank ordering, volatility, fill probability, or treatment/event effect. Do not switch estimands after seeing which one looks best without recording that as another trial.

## 2. Effective sample size and dependence

The row count is not necessarily the number of independent observations. Serial correlation, overlapping holding periods, common market shocks, repeated assets, and clustered events reduce effective information. Standard errors designed for independent observations can understate uncertainty. Use dependence-aware inference appropriate to the unit of dependence and report the assumptions.

For a sample mean \(\bar r\) from a weakly stationary series, the long-run variance is \(\Omega=\gamma_0+2\sum_{k\ge1}\gamma_k\), where \(\gamma_k\) is lag-\(k\) autocovariance. Asymptotically, \(\operatorname{Var}(\bar r)\approx\Omega/n\), rather than simply \(\gamma_0/n\). This is the reason autocorrelation changes standard errors and why nominal trade count is not an adequate sample-size argument. The stationarity and summability assumptions can fail at regime changes; treat the approximation as a model, not a repair for nonstationarity.

### Which dependence should uncertainty reflect?

- **Time-series signal/strategy:** serial correlation, volatility clustering, and overlapping holding periods.
- **Cross-sectional portfolio:** shared date shocks and factor exposures across assets.
- **Event study:** events clustered by issuer, event, country, or macro shock, as appropriate.
- **Execution data:** repeated fills/orders nested within day, symbol, venue, or parent order.

Choose HAC, clustering, block bootstrap, or another method based on this design. No method can compensate for a wrongly defined observation unit. If several dimensions matter, explain which are covered and which remain uncertain.

## 3. Effect size, uncertainty, and economic relevance

Report the estimate and its uncertainty interval, not just a p-value. State units and horizon. Convert a forecast into a trade only under an explicit mapping and include spread, fees, slippage, market impact, borrow, financing, turnover, and capacity. Statistical detectability is not a proof of tradable expected value.

### Example: gross edge versus decision hurdle

Suppose a pre-specified signal has estimated gross mean return of 3 bp per decision, with a dependence-aware 95% interval of [-1, 7] bp. If expected round-trip costs are 2 bp, subtracting a fixed cost gives a plug-in net estimate of 1 bp and interval [-3, 5] bp **only if** the cost is genuinely fixed and known. In reality, costs are uncertain and state-dependent, and the signal may trade more in volatile or illiquid periods. Estimate net returns per decision with cost inputs aligned to the same orders and time, and include uncertainty in execution/cost modeling. The estimate is not established as positive simply because its point estimate remains above zero.

The research hurdle should match the decision: for deployment, compare net value to required risk/capital return, operational burden, and uncertainty—not merely to a zero-return null.

## 4. Multiple testing and selection

The hypothesis count includes more than named models: feature definitions, universes, lags, thresholds, sample windows, label choices, preprocessing, hyperparameters, and reporting choices. Correlated tests require careful treatment; a naive Bonferroni count may be too conservative or fail to reflect adaptive search. Preserve the full trial ledger and use appropriate multiplicity-aware methods. See [[Overfitting controls]].

Selection can be expressed simply: if \(\hat\theta_j=\theta_j+\epsilon_j\) is the noisy estimate for trial \(j\), choosing \(j^*=\arg\max_j\hat\theta_j\) tends to select a positive noise realization even when all true effects are zero. The larger and more adaptive the search, the more optimistic the selected estimate can be. Correlation among trials changes the magnitude but does not eliminate the problem. The trial ledger should include failed/null results and decisions made after looking at interim outcomes.

## 5. Out-of-sample design

Choose chronological splits before fitting. Use nested validation for model selection, preserve a final untouched period or prospective test, and avoid repeatedly consulting a holdout. Purge training observations whose future label intervals overlap test data; add embargo gaps where adjacent information can leak. See [[ML validation]].

## 6. Robustness as a research result

Report performance across dates, instruments, liquidity groups, regimes, and plausible implementation assumptions. Stress data definitions, timestamp lags, costs, universe membership, and parameter choices. Robustness checks should be planned and interpreted, not endlessly searched for a positive result.

## 7. Economic mechanism and alternative explanations

An edge hypothesis should explain who is compensated, constrained, delayed, or systematically mistaken. Ask whether the return is a risk premium, known factor exposure, liquidity compensation, data artifact, or chance. A coherent story helps design tests but cannot rescue weak empirical evidence.

## 8. Interpretation of t-statistics

There is no universally valid t-statistic threshold for all financial strategies. Harvey, Liu, and Zhu (2016) show why the factor-discovery literature's large search universe raises the hurdle; Novy-Marx (2015) shows how combining and selecting signals can amplify bias. Their numeric conclusions depend on setting and assumptions. They should motivate better search accounting, not be used as magic cutoffs.

For a single pre-specified mean under independent observations, a t-statistic is \(t=\hat\mu/\widehat{SE}(\hat\mu)\). In a selected strategy, both numerator and nominal reference distribution are affected by search. Replacing the standard error with a HAC estimate fixes only a specified dependence issue; it does not account for searching many strategies. Likewise, a multiple-testing adjustment does not fix point-in-time leakage or unrealistic fills. Map each correction to the failure mode it addresses.

## 9. Research report template

- Hypothesis and mechanism:
- Data source, vintage, universe, and availability timestamp:
- Target, horizon, benchmark, and costs:
- All trials / search dimensions:
- Validation and inference method:
- Effect size and uncertainty:
- Results by period/regime/instrument:
- Robustness, placebo, and alternative explanations:
- Capacity and implementation limits:
- Replication and next falsification:
- Source grade and unresolved data caveats:

## Related notes

[[Edge validation]] · [[Overfitting controls]] · [[Research workflow]] · [[Feature engineering]] · [[Time series]] · [[Statistical testing pitfalls]] · [[Execution costs and market impact]]

Focused extensions: [[Selection-aware inference for strategy search]] · [[Forecast value and decision mapping]] · [[Market event studies and causal identification]]
