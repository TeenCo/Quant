# Conditional expectation and forecasts

## Definition and derivation

For information set \(\mathcal F_t\), \(m_t=E[Y_{t+1}\mid\mathcal F_t]\) is the measurable forecast minimizing conditional squared loss. Expand \(E[(Y-a)^2\mid\mathcal F_t]\) around \(m_t\): it equals \(Var(Y\mid\mathcal F_t)+(a-m_t)^2\), since \(E[Y-m_t\mid\mathcal F_t]=0\). Thus the forecast is optimal only for squared-error loss; quantile loss selects a conditional quantile and absolute loss a conditional median.

The tower property \(E[E[Y\mid\mathcal G]\mid\mathcal H]=E[Y\mid\mathcal H]\), for \(\mathcal H\subseteq\mathcal G\), gives coherent aggregation across information sets. Conditional variance decomposes total variance into \(E[Var(Y\mid\mathcal F)]+Var(E[Y\mid\mathcal F])\).

## Finance example

Suppose next-day excess return is +2% or −1%, with probabilities 0.4 and 0.6 when a signal is positive. Its conditional mean is \(0.4(2\%)+0.6(-1\%)=0.2\%\). A zero forecast has conditional MSE \(0.4(2^2)+0.6(1^2)=2.2\) percentage-points-squared; using 0.2% reduces MSE by \(0.2^2=0.04\). This does not establish a tradable edge: costs, risk preferences, estimation error, and information timing remain.

## Assumptions and failure modes

Conditional means require integrability. A conditional distribution/forecast is defined only up to almost-sure equivalence; conditioning on a continuous variable's exact value requires a regular conditional distribution. Estimated conditional means can overfit, leak future information, or be unstable under regime change. Mean-optimal forecasts can conceal skew and crash risk.

## Falsifiable exercise

Using a point-in-time daily signal and next-day excess returns, preregister a rolling conditional-mean model versus historical-mean and zero baselines. Compare out-of-sample squared error and net strategy returns with realistic costs. Reject the claimed forecast improvement if its chronological test MSE difference is nonnegative; report uncertainty with time blocks.

## Sources

- [Conditional expectation](https://www.statlect.com/fundamentals-of-probability/conditional-expectation) — **Grade 3**, 2021; novelty low; online mathematical lecture. Direct page reviewed. Gives accessible definitions and tower property; informal treatment, not a measure-theory text or finance evidence.
- [Forecast evaluation](https://otexts.com/fpp3/accuracy.html) — **Grade 3**, 2021/online edition; novelty low; open textbook. Definitions/metrics useful, but not a substitute for dependence-aware inference.

Related: [[Probability]] · [[Statistics]] · [[Forecast evaluation]] · [[Edge validation]]
