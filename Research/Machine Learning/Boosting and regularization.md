# Boosting and Regularization

## Core idea

Gradient boosting builds an additive predictor \(F_M(x)=F_0(x)+\sum_{m=1}^M\eta h_m(x)\), fitting each weak learner to a loss gradient/residual. Shrinkage \(\eta\), tree depth/leaf constraints, row/column subsampling, and early stopping regularize different aspects of the fit. For squared loss, each stage approximates residual structure; for other losses it follows pseudo-residuals. More rounds/deeper trees reduce training loss but can amplify noise and interactions.

Financial example: predict next-week cross-sectional return ranks from lagged fundamentals and market state, then translate ranks to a constrained portfolio only after costs and exposures are modeled. Boosting handles nonlinear thresholds, but a selected split may just encode a historical regime.

## Leakage and validation failures

- Tune rounds, depth, learning rate, feature subsampling, and stopping epoch inside chronological inner folds; freeze the process before outer evaluation.
- Early stopping on the outer test is test-set selection. Fit imputers, encoders, scaling, and feature selection fold-locally.
- Random folds scramble regimes and leak information through overlapping labels; purge by actual label end times.
- Search across many losses/features/seed settings inflates apparent performance; preserve a trial ledger and compare equal tuning budgets against regularized linear baselines.
- Standard tree importance can favor high-cardinality or correlated features; importance is not causal evidence.

## Research exercise

Compare ridge, shallow gradient-boosted trees, and deeper boosted trees on identical point-in-time predictors and purged walk-forward folds. Inner-select shrinkage/rounds/depth. Record outer-fold rank IC, calibration for a direction target, turnover-adjusted returns, feature stability, and sensitivity to excluding the largest volatility episode.

## Sources (graded)

- **Grade 1** — Friedman (2001), *Greedy Function Approximation: A Gradient Boosting Machine*, Annals of Statistics. Recency: established (2001); novelty: functional-gradient formulation. Type: peer-reviewed primary methods paper. Direct: https://doi.org/10.1214/aos/1013203451 . Limit: theory/method is not evidence of financial predictability.
- **Grade 2** — Chen & Guestrin (2016), *XGBoost: A Scalable Tree Boosting System*, KDD. Recency: mature (2016); novelty: systems and regularized objective. Type: peer-reviewed conference paper. Direct: https://doi.org/10.1145/2939672.2939785 . Limit: implementation paper; its benchmark results do not establish robustness under financial nonstationarity.
