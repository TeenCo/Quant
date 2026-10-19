# Probability and Stochastic Processes

## Foundations

Study random variables and distributions, joint/conditional distributions, expectation, variance, covariance, dependence, conditional expectation, laws of large numbers, central limit results, tail behavior, and concentration. Real financial returns often violate simple iid Gaussian assumptions through heavy tails, volatility clustering, jumps, and changing regimes.

## Stochastic-process topics

Time-indexed random systems include random walks, Markov chains, martingales, point processes, Brownian motion, jump processes, and stochastic volatility. These ideas support time-series models, derivatives, event-arrival models, and risk analysis.

## Quantitative uses

- Model forecast uncertainty and portfolio/risk aggregation.
- Understand when standard errors and asymptotic approximations fail.
- Distinguish conditional predictability from unconditional correlation.
- Model arrival processes, volatility, and state-dependent dynamics.

## Conditional expectation as the forecasting object

For a target \(Y_{t+h}\) and information set \(\mathcal{F}_t\) available at time \(t\), the conditional mean forecast is

\[
m_t=\mathbb{E}[Y_{t+h}\mid\mathcal{F}_t].
\]

Under squared-error loss, this conditional expectation is the optimal forecast among functions of \(\mathcal{F}_t\): for any forecast \(g_t\),

\[
\mathbb{E}[(Y-g_t)^2\mid\mathcal{F}_t]
=\operatorname{Var}(Y\mid\mathcal{F}_t)+(m_t-g_t)^2.
\]

The identity follows by writing \(Y-g_t=(Y-m_t)+(m_t-g_t)\); the cross term has conditional expectation zero. It shows why a better conditional-mean estimate lowers expected squared forecast error, but does **not** imply a profitable strategy: the portfolio decision may depend on tails, costs, constraints, and utility rather than squared error. For quantiles or tail-risk decisions, a conditional mean is generally not the relevant forecast.

## Martingales and the no-free-forecasting baseline

A process \(M_t\) is a martingale relative to information \(\mathcal{F}_t\) if it is integrable, adapted, and \(\mathbb{E}[M_{t+1}\mid\mathcal{F}_t]=M_t\). In an idealized frictionless market model, a correctly discounted traded asset price under an appropriate pricing measure may be modeled as a martingale. This is not a claim that real-world returns are iid or that all conditional patterns are absent. Risk premia, information, constraints, transaction costs, and the choice of measure matter.

For empirical research, compare a proposed forecast with a baseline embodying the relevant null (such as zero excess-return forecast, historical mean, random walk, or current benchmark). Define the information set explicitly: “known at close” differs from “published at close” and from “available in a vendor database later.” See [[Time series]], [[Data vintage and real-time testing]], and [[Forecast evaluation]].

## Tail risk and expected value

Expectation can hide rare, large outcomes. Two return distributions can have the same mean and variance but materially different skewness and tail loss. A strategy with frequent small gains and occasional crash losses may look attractive under averages estimated from a short sample. Report quantiles, drawdown, expected shortfall or another clearly defined tail measure, and scenario behavior alongside the mean. Tail estimates are themselves uncertain, especially when the sample contains few independent extreme events.

## Connected notes

[[Mathematics]] · [[Statistics]] · [[Time series]] · [[Market microstructure]] · [[Options]]

Focused foundations: [[Conditional expectation and forecasts]] · [[Limit laws for dependent returns]]
