# Multidimensional Geometry and Topology

Geometry studies distances, angles, curvature, and shape; topology studies properties preserved under continuous deformation, such as connectedness and holes. These tools can help describe structure in high-dimensional feature, state, or market data.

## Possible research applications

- Manifold learning and nonlinear embeddings for latent market-state exploration.
- Persistent homology/topological data analysis to investigate multi-scale structure in time series or correlation networks.
- Geometric views of covariance, portfolios, and distances between distributions.
- State-space and regime analysis where Euclidean distance may be misleading.

## Caution

High-dimensional geometry is sensitive to scaling, sample size, noise, and dependence. Exploratory topological patterns are not predictive evidence. Define a test statistic and null/reference process, control for multiple search, use chronological validation, and compare with simple baselines.

## Metric choice changes the result

For a feature vector \(x\), Euclidean distance is \(d(x,y)=\|x-y\|_2\). If features have different units or scales, large-unit coordinates dominate. Standardization changes the metric; Mahalanobis distance

\[
d_\Sigma(x,y)=\sqrt{(x-y)^T\Sigma^{-1}(x-y)}
\]

accounts for covariance under an estimated \(\Sigma\), but can become unstable when dimension is high relative to sample size. Robust/scaled or shrinkage covariance estimates may help, but each choice changes neighborhoods and therefore clusters/embeddings. Fit all metric parameters on the training window.

## Persistent homology as an exploratory tool

Given observations in a metric space, a filtration builds nested neighborhoods as a scale parameter \(\epsilon\) grows. Topological features (connected components, loops, higher-dimensional voids) can appear and disappear across scales; persistence summarizes their lifetimes. Long persistence is not automatically economically meaningful: serial dependence, heavy tails, volatility changes, and point density can produce apparent structure.

For a defensible market test, compare an observed statistic (for example, a persistence summary) with null series that preserve relevant properties such as marginal distribution, autocorrelation, volatility clustering, and calendar structure. Decide which properties the null should preserve from the hypothesis. Then test stability across chronological windows and ask whether the topological feature improves a specified forecast/decision over simpler features. Include all embedding dimensions, distance metrics, scales, and statistics tried in the search ledger.

## Manifolds and embeddings

Manifold-learning methods seek a lower-dimensional representation that preserves some notion of local or global geometry. Different algorithms preserve different quantities; distances in a two-dimensional visualization are not necessarily meaningful globally. Use embeddings for exploration, record random seeds and parameters, assess neighborhood preservation, and do not infer regimes from visual separation alone. Any discovered segmentation must be assigned using only information available at each historical date.

Connected: [[Linear algebra]] · [[Unsupervised learning and regimes]] · [[Feature engineering]] · [[Overfitting controls]]

## Connected notes

[[Mathematics]] · [[Unsupervised learning and regimes]] · [[Alternative data]] · [[Overfitting controls]]

Focused foundation: [[Persistent homology for market data]]
