# Difference-in-Differences for Market Events

## Estimand

For treated and comparison units before/after intervention,

\[
\hat\tau=(\bar Y_{T,post}-\bar Y_{T,pre})-(\bar Y_{C,post}-\bar Y_{C,pre}).
\]

In the simple two-group/two-period case this removes fixed group differences and common time movement. Causal interpretation requires parallel untreated trends and a valid control.

## Worked example: exchange fee change

Suppose an exchange cuts fees for designated contracts while matched contracts on another venue are untreated. Choose an outcome such as quoted spread or volume, define eligibility and timestamp, align contract maturity and trading hours, and compare pre/post changes. A relative spread decline is causal only if no differential concurrent change, anticipation, or spillover explains it. For returns, common news and cross-asset spillovers make controls particularly difficult.

## Assumptions and failure modes

- Parallel trends concerns untreated potential outcomes; a flat pre-trend cannot prove it.
- Require no anticipation, differential simultaneous shocks, changing composition, or control contamination.
- Treatment timing must reflect when information became available; leaked policy details can invalidate the pre-period.
- Staggered dates and heterogeneous effects make conventional two-way fixed effects potentially misleading.
- Inference follows assignment/shared shocks; many intraday bars do not create many independent treatment units.

## Falsifiable exercise

For one documented market-design intervention, pre-specify treated instruments, controls, outcome, window, and inference unit. Run DiD plus three pre-event placebo dates and one unaffected outcome. Falsify the causal account if placebo effects approach the main estimate, pre-event differential trends are economically material, or a treated-only concurrent intervention is documented.

## Claim-specific sources

- DiD identification: grade **2/10**; recency **2009 textbook; method current**; novelty **low**; source type **academic methods text**; [Mostly Harmless Econometrics companion site](https://www.mostlyharmlesseconometrics.com/). Landing page checked, specific chapter not reviewed. Limit: general methods, not market-event identification evidence.
- Staggered treatment and heterogeneous effects: grade **2/10**; recency **2021 journal publication**; novelty **high/practical**; source type **peer-reviewed econometrics paper**; [Callaway & Sant'Anna DOI page](https://doi.org/10.1016/j.jeconom.2020.12.001). Bibliographic/abstract page checked, full text not reviewed. Limit: not finance-specific anticipation/interference guidance.

Related: [[Causal inference]] · [[Economics-to-market hypotheses]] · [[Market microstructure]] · [[Statistical inference for trading]]
