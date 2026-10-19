# Persistent homology for market data

## Construction

Given points with a chosen distance, a Vietoris–Rips filtration includes a simplex whenever all its vertices are within distance \(\epsilon\). As \(\epsilon\) grows, connected components, loops, and higher-dimensional holes are born and later merge/fill. A persistence diagram records birth/death scales; long-lived features are more robust to scale choice than short-lived ones, but are not automatically economically meaningful.

For market data, points might be rolling vectors of standardized returns or correlations. The embedding, normalization, window, and metric define the object being analyzed; changing them changes the topology. Statistical inference needs a null distribution that preserves the dependence properties relevant to the claim.

## Worked quantitative example

Use four synthetic 2D states on a circle of radius 1 at the cardinal points. Adjacent Euclidean distances are \(\sqrt2\), opposite distances 2. Under the Rips construction, the cycle appears at \(\epsilon=\sqrt2\) and fills when diagonals are admitted at \(\epsilon=2\); its lifetime is \(2-\sqrt2\approx0.586\). Map this diagnostic to four normalized two-day return states and compare the observed lifetime with shuffled/block-bootstrap nulls; the synthetic geometry alone implies no return forecast.

## Falsifiable exercise

Preregister one persistence statistic and one market-state hypothesis (e.g. whether its trailing value predicts next-week realized volatility beyond lagged volatility). In chronological splits compare against block-resampled null series preserving marginal distribution and short-range dependence, and against a simple volatility baseline. The claim fails if out-of-sample improvement is absent or disappears under null replication/multiple-search correction.

## Assumptions and failure modes

Distance geometry assumes the scaling and metric are meaningful. Sparse high-dimensional samples, outliers, serial dependence, volatility clustering, and nonstationarity can create or erase features. Standard persistence stability results concern perturbations under specified metrics, not predictive validity. Repeatedly trying embeddings, dimensions, scales, and statistics creates selection bias; fit all preprocessing on training windows.

## Sources

- [Wasserman (2018), Topological data analysis](https://doi.org/10.1146/annurev-statistics-031017-100045) — **Grade 1**, 2018; novelty medium; peer-reviewed statistical review. Reviews statistical framing; market application requires bespoke nulls and validation.

Related: [[Topology and geometry]] · [[Unsupervised learning and regimes]] · [[Overfitting controls]] · [[Edge validation]]
