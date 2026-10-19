# Unsupervised Learning and Regime Discovery

Unsupervised methods find structure without a labeled target: clustering, dimensionality reduction, density estimation, latent state models, and anomaly detection.

## Applications

- Explore market state/regime descriptions using volatility, correlation, liquidity, macro, or flow features.
- Reduce dimensionality or identify correlated assets/factors.
- Detect unusual observations or data-quality anomalies.

## Validation cautions

Clusters are not necessarily real, stable, causal, or predictive. Choose scaling carefully, assess stability across time and samples, avoid full-sample transforms, and test whether regime labels improve decisions out of sample versus simple alternatives. Handle look-ahead if regimes are assigned using future observations.

## Example: k-means objective and its limits

For observations \(x_i\) and cluster assignments \(z_i\in\{1,\dots,K\}\), k-means minimizes within-cluster squared distance \(\sum_i\|x_i-\mu_{z_i}\|_2^2\). This favors compact, roughly spherical clusters under the chosen metric; it does not discover a unique “true” number of market regimes. Results depend on feature scaling, initialization, outliers, window, and \(K\). Compare multiple seeds and stability, but do not select the configuration by best downstream test performance without accounting for that search.

## Online regime assignment

Historical cluster labels are often assigned using full-sample centroids, which uses future information. For a realistic test, fit scaling and clustering on a trailing training window, freeze parameters for the next evaluation block, and assign each new point using only the fitted transform/model. If the model is refit periodically, record each refit time and use only data available then. Test regime benefit against a simple observable state rule (e.g., lagged volatility threshold) and a no-regime baseline.

Unsupervised anomalies are not automatically bad data or predictive events. Keep separate labels for data-quality failures and unusual but valid market observations; clipping/removing crashes can erase the very risk under study.

Related: [[Topology and geometry]] · [[Time series]] · [[Feature engineering]] · [[Overfitting controls]]
