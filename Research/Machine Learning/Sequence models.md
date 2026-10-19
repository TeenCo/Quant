# LSTM and Sequence Models

Sequence models consume ordered observations. Recurrent neural networks update a hidden state over time; LSTMs use gated memory to support longer dependencies. GRUs, temporal convolutions, state-space models, and Transformers are alternative sequence approaches.

## Potential financial inputs

Bars, returns/volatility, order-book events, text sequences, macro release histories, and cross-asset observations. Define sequence time resolution and prevent feature timestamps from extending beyond the simulated decision time.

## Limitations and controls

Long lookback does not guarantee useful memory. Strong capacity can fit noise; shuffled folds leak temporal structure; overlapping labels inflate apparent sample size; nonstationarity can render learned patterns stale. Compare to naive/time-series and regularized baselines, use walk-forward validation, test ablations, and include trading costs.

## LSTM cell intuition

An LSTM maintains hidden state \(h_t\) and cell state \(c_t\). Gates use sigmoid functions to control retention, writing, and output; a simplified form is

\[
f_t=\sigma(W_f[x_t,h_{t-1}]+b_f),\quad i_t=\sigma(W_i[x_t,h_{t-1}]+b_i),
\]
\[
\tilde c_t=\tanh(W_c[x_t,h_{t-1}]+b_c),\quad c_t=f_t\odot c_{t-1}+i_t\odot\tilde c_t,
\]
\[
o_t=\sigma(W_o[x_t,h_{t-1}]+b_o),\quad h_t=o_t\odot\tanh(c_t).
\]

The additive cell update can support gradient flow across longer sequences compared with a basic RNN, but it does not guarantee that the learned memory is economically stable or useful. Hidden state is a learned representation whose meaning can drift across retraining windows.

## Sequence and label alignment

For a decision at time \(t\), the input window must end no later than the last observation actually available at \(t\); the label interval begins after the decision and ends at its declared horizon. Build windows after chronological splitting or ensure each sample carries explicit start/end times so purging can remove overlap. Beware that overlapping windows share most raw observations, so sample count overstates independent information.

Compare LSTM/GRU/attention to (i) last-value or persistence forecast, (ii) linear autoregression, (iii) regularized tabular model on lag features, and (iv) simpler temporal convolution/state-space baseline where appropriate. Conduct feature/sequence-length ablations with nested chronological selection, report inference latency/memory, and test sensitivity to retraining cadence.

## Reading

[[Sources/Miyato Dai Goodfellow 2017]] is an example of recurrent sequence modeling and regularization in text—not evidence of trading performance.
