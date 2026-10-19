# Deep Learning Regularization and Attention

## Core idea

Regularization adds constraints/penalties to reduce effective fit variance: weight decay optimizes \(L(\theta)+\lambda\|\theta\|_2^2\); dropout randomly masks activations during training; early stopping limits optimization using an inner validation criterion. Attention computes content-dependent weighted context, e.g. \(\mathrm{softmax}(QK^\top/\sqrt{d_k})V\). It enables flexible interactions, not causal attribution or guaranteed long-memory discovery.

Financial example: attend over a trailing window of market events to estimate execution cost, with a strictly causal mask so each decision sees only already-arrived events.

## Leakage and validation failures

- A bidirectional attention mask or centered normalization can expose future tokens. Enforce causal masks and verify timestamp alignment with an adversarial unit example.
- Early stopping, architecture choice, regularization strength, and seed choice belong to inner validation; repeatedly inspecting outer results turns them into training data.
- Random time permutation/augmentation can destroy market structure; only use transformations justified by invariances of the data-generating process.
- Small effective sample size and overlapping windows make nominal data volume deceptive. Report seed dispersion and compare equal-budget linear/boosted baselines.
- Attention weights are not feature causality; use controlled ablation and perturbation with the full selection process acknowledged.

## Research exercise

On a fixed event-time forecasting task, compare a small causal attention model with a parameter-matched temporal baseline and ridge on the same folds. Run causal-mask leakage tests, three predeclared regularization settings, multiple seeds, and one feature ablation. Compare calibration, net utility, inference latency, and outer-fold variability.

## Sources (graded)

- **Grade 1** — Vaswani et al. (2017), *Attention Is All You Need*. Recency: established architecture (2017; arXiv record revised 2023); novelty: attention-only Transformer. Type: primary conference paper/preprint. Direct source verified: https://arxiv.org/abs/1706.03762 . Limit: machine translation experiments, not financial forecasting evidence.
- **Grade 2** — Srivastava et al. (2014), *Dropout: A Simple Way to Prevent Neural Networks from Overfitting*, JMLR. Recency: established (2014); novelty: influential regularization method. Type: peer-reviewed journal paper. Direct: https://jmlr.org/papers/v15/srivastava14a.html . Limit: benchmark evidence does not determine the appropriate financial regularizer.
