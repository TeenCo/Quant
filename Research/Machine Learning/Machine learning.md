# Machine Learning in Financial Research

ML estimates predictive mappings or latent structure from data. A useful model must outperform reasonable baselines out of sample, preserve temporal integrity, and improve a decision after costs. Financial datasets often have lower signal-to-noise, stronger distribution shift, and more dependence than benchmark ML tasks.

## Families

- [[Supervised learning]] for prediction/classification.
- [[Unsupervised learning and regimes]] for clustering, dimensionality reduction, and state discovery.
- [[Deep learning]] for high-capacity representation learning.
- [[Sequence models]] for LSTM and other sequence/time-series architectures.
- [[Reinforcement learning]] for sequential decision and control problems.
- Ensemble methods: random forests, gradient boosting, stacking (with careful nested validation).

## ML research protocol

Specify the point-in-time target and action; create chronological validation; fit all preprocessing inside folds; log trials; compare simple baselines; evaluate calibration and net economic utility; assess regime robustness and computational costs. See [[ML validation]], [[Overfitting controls]], and [[Research workflow]].
