# Financial Machine Learning Validation

This note is a practical checklist for applying ML to market data. Models such as [[Sequence models]] do not remove the need for valid targets, point-in-time features, and realistic execution.

## Splits for time-dependent labels

- Keep training earlier than validation and test; avoid random shuffling across time.
- If labels span future windows, remove training examples whose label intervals overlap the test interval (**purging**).
- Apply an **embargo** gap after a test interval when adjacent observations may share information or features.
- Use nested chronological validation for model selection; do not pick hyperparameters with the final holdout.
- Repeat walk-forward evaluation across multiple periods and regimes.

### Deriving the purge requirement

Represent each labeled observation \(i\) by a feature/decision time \(t_i\) and a label information interval \([t_i,e_i]\), where \(e_i\) is the final time used to calculate its target. If a test set uses information interval \([T_0,T_1]\), a training label is contaminated when its outcome interval overlaps the test information interval. Remove every such training observation; do not infer overlap solely from row distance when labels have variable horizons.

An embargo removes a buffer of observations after a test block when nearby records can share information through delayed features, event windows, or operational latency. It is not a magic fixed number of bars: derive it from the maximum relevant overlap/availability window, document it, and run a sensitivity check. Purging addresses label overlap; it does not correct revised data, future universe membership, global preprocessing, or unrecorded researcher choice.

## Worked split example

Suppose observations are sampled daily, and each label is the return from the decision close through the close five sessions later. A test block begins on day 100. Any training sample whose label uses day 100 or later must be removed from the training set for that fold, even if its feature row predates day 100. In this simple fixed-horizon case this removes the preceding five decision dates; with irregular calendars, events, or variable exit rules, calculate actual label end times instead.

For a pipeline with rolling volatility normalization, fit its parameters on the training portion only for each fold. If a scaler is fitted once on the full sample, future distribution information leaks into training even though the labels themselves were purged. The same rule applies to imputation, feature selection, PCA, target encoding, winsorization thresholds, and learned embeddings.

## Label and feature integrity

- Define the decision timestamp and feature cutoff; all values must be available then.
- Compute targets from future data only, but prevent their interval from contaminating training folds.
- Use vintage data for revised series where possible; store release time separately from reference period.
- Avoid full-sample normalization, imputation, feature selection, dimensionality reduction, or class balancing before the split.
- Verify asset identity, corporate actions, delistings, roll schedules, and venue calendars.

## Metrics and economics

Report forecast metrics alongside decision/portfolio metrics. Evaluate calibration, rank/information coefficient, turnover, tail loss, drawdown, exposure, capacity, and net returns with costs. Accuracy or RMSE alone does not demonstrate a trading edge.

Compare predictive models using a pre-specified loss and benchmark, with dependence-aware inference; see [[Forecast evaluation]]. Check whether performance shifts across time or volatility states using [[Structural breaks and parameter instability]] and [[Volatility models]].

## Model selection and reporting

Maintain a trial ledger; account for multiple models and labels. Compare with naive forecasts and simple regularized models. Report stability by time and universe. Preserve failed model runs and explain why any approach was abandoned.

### Nested chronological evaluation

Separate three roles:

1. **Training window:** estimate model parameters and learned transforms.
2. **Inner validation:** choose features/hyperparameters/early stopping settings using only historical data.
3. **Outer test/forward window:** evaluate the frozen inner-selected procedure once for that fold.

At the next forecast origin, move the windows forward and repeat the whole procedure using only information then available. The quantity being evaluated is the **selection-and-refit procedure**, not the single final parameter set selected after seeing every fold. Keep outer predictions and timestamps, and avoid using them to make additional design choices; if they are used, they become development data and a new final test is needed.

### Evaluation units

Report per-fold and pooled measures with careful weighting. A pooled row-level metric can overweight periods with more observations or highly liquid assets. Choose whether the target is average decision, average asset, average calendar time, or portfolio capital, and aggregate accordingly. Include a simple baseline, calibration and rank measures where relevant, turnover/constraints for decisions, and uncertainty that reflects time dependence and model selection.

Related: [[Overfitting controls]], [[Research workflow]], [[Edge validation]], [[Sequence models]], [[Reinforcement learning]].

## Focused model-family validation notes

- [[Supervised loss and calibration]] — proper scores, calibration diagnostics, and decision thresholds.
- [[Boosting and regularization]] — stage-wise fitting, shrinkage, and time-aware tuning.
- [[Clustering and HMM state inference]] — distinguish descriptive partitions from filtered latent-state probabilities.
- [[Deep learning regularization and attention]] — capacity controls and attention-specific leakage checks.
- [[LSTM and state-space forecasting]] — sequence memory versus explicit latent-state recursions.
- [[RL off-policy evaluation]] — support, importance weighting, and doubly robust estimates.
