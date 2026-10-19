# Supervised Learning

Supervised methods learn a relationship from features `X` to observed targets `y`. Common tasks include regression, classification, ranking, and probabilistic forecasting.

## Methods

Linear/regularized regression, logistic models, decision trees, random forests, gradient boosting, support-vector methods, neural networks, and ensembles.

## Financial targets

Targets may be future returns, volatility, event direction, relative ranking, execution cost, or risk. Choose a target that maps to a decision horizon and realistic action; labels that overlap must be handled in validation.

## Key checks

- Baselines before complexity; out-of-time and cross-asset evaluation.
- Calibration, ranking and decision utility, not only accuracy/RMSE.
- Costs, turnover, capacity, exposure, and uncertainty.
- Nested selection and multiple-trial accounting.

## Loss functions and decisions

Training minimizes an empirical loss, which encodes what errors matter. Squared error targets a conditional mean; absolute error targets a conditional median; quantile loss targets a conditional quantile; log loss evaluates probabilistic classification and rewards calibrated probabilities. Accuracy discards confidence and can be misleading under class imbalance. Rank metrics evaluate ordering but not calibration or economic magnitude.

Map predictions to actions only after specifying utility. A probability forecast \(p_t\) is useful for a binary decision only relative to the payoff asymmetry, base rate, costs, and action threshold. Calibrate probabilities on historical validation data without using the test period. Evaluate forecast metrics and net decision utility separately.

## Regularization example

Ridge regression minimizes \(\|y-X\beta\|_2^2+\lambda\|\beta\|_2^2\), shrinking coefficients toward zero and stabilizing correlated predictors. Lasso uses \(\lambda\|\beta\|_1\), which can set coefficients exactly to zero but may select arbitrarily among strongly correlated features. Standardize predictors using training data only; choose \(\lambda\) in nested chronological validation. Regularization controls variance under a chosen model but does not cure nonstationarity, leakage, or multiple testing.

## Data and target design

Returns are noisy continuous targets, so evaluate forecast error, rank, and portfolio utility at a fixed horizon. Direction labels discard magnitude and can create class imbalance. Threshold labels must be chosen without selecting them on the final test. For cost/volatility targets, ensure labels correspond to the trade and time interval of interest. Retain unscaled raw outcomes for interpretation even when training on normalized labels.

Connected: [[Machine learning]] · [[Feature engineering]] · [[ML validation]] · [[Edge validation]]
