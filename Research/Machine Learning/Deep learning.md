# Deep Learning

Deep learning uses layered differentiable functions to learn representations. Families include multilayer perceptrons, convolutional networks, recurrent networks, attention/Transformers, autoencoders, and generative models.

## Financial strengths and challenges

Potential strengths include nonlinear interactions and unstructured text/image/event inputs. Challenges include data scarcity relative to model capacity, regime shift, computational and energy cost, noisy targets, calibration, interpretability, and severe selection bias.

## Practice

Use simple linear/boosted baselines; justify the architecture by data structure; separate data/model/preprocessing versions; enforce chronological validation and feature availability; use early stopping only on validation data; report seed variability and compute; evaluate net decision value. See [[ML validation]] and [[Overfitting controls]].

## Capacity, regularization, and ablation

Parameter count is only a rough complexity measure, but large representation capacity relative to independent regimes/events raises estimation risk. Weight decay, dropout, data augmentation, early stopping, and architectural constraints impose different assumptions; none creates information absent from the data. In markets, augmentation must preserve plausible economic structure—randomly permuting time or adding arbitrary noise can invalidate the task.

Use ablations to test whether a complex component adds value over a simpler model, but treat each ablation as part of the search if it guides model choices. Report multiple seeds, training instability, calibration, compute, and net utility. Keep data normalization, feature selection, and early stopping fold-local.

## Architecture selection rule

Choose architecture from the structure of the input: convolutions for local spatial/time patterns; recurrent/state-space models for sequential state updates; attention for context-dependent interactions; autoencoders for compression/anomaly hypotheses. This is a reason to test, not proof that the architecture will be superior. Start from a strong non-neural benchmark and compare on identical point-in-time features, samples, tuning budgets, and execution assumptions.
