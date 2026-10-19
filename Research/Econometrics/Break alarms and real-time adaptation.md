# Break Alarms and Real-Time Adaptation

## Retrospective breakpoint versus live alarm

A full-sample estimated break date is unavailable to a live process. Define an operational detector using information through \(t\), threshold, monitoring cadence, and action delay. A recursive residual is

\[
w_t=\frac{y_t-x_t'\hat\beta_{t-1}}{\sqrt{1+x_t'(X_{t-1}'X_{t-1})^{-1}x_t}}.
\]

CUSUM-type procedures aggregate standardized residuals and signal at a chosen boundary. A rolling refit is an adaptation policy, not a break test.

## Worked example: monitor a forecast relationship

Estimate a daily signal-to-next-day-return regression expanding at each close. Calibrate a CUSUM threshold on training data for a stated false-alarm target. If crossed at close \(t\), permit a refit only for decisions from \(t+1\). Compare this procedure with a 252-session rolling fit and a no-adaptation expanding baseline, including alarm frequency, coefficient noise, turnover, and net performance.

## Assumptions and failure modes

- Classical control limits require assumptions about residual dependence/distribution; heteroskedasticity and fat tails change false-alarm rates.
- Searching series, thresholds, and windows inflates alerts; these choices are model selection.
- Retrospective multiple-break segmentation is not an online detection guarantee.
- Data revisions, release delays, and execution timing must be replayed as available; a schema break calls for data repair.

## Falsifiable exercise

Sequentially replay one historical forecast stream with fixed expanding, calibrated CUSUM-triggered refit, and fixed rolling-window policies. Falsify adaptation benefit if the alarm policy fails to improve predeclared forecast loss or net utility versus expanding, or its stable-period empirical alarm rate exceeds its target.

## Claim-specific sources

- Recursive-residual/CUSUM monitoring: grade **2/10**; recency **1975 foundational**; novelty **low**; source type **peer-reviewed statistical methodology**; [Brown, Durbin & Evans DOI record](https://doi.org/10.1111/j.2517-6161.1975.tb01532.x). Bibliographic landing page checked, full text not reviewed. Limit: classical boundaries require recalibration for dependence, heteroskedasticity, and repeated monitoring.
- Multiple structural change estimation: grade **2/10**; recency **2003 foundational**; novelty **low**; source type **peer-reviewed Econometrica paper**; [Bai & Perron DOI record](https://doi.org/10.1111/1468-0262.00430). Bibliographic landing page only checked. Limit: retrospective segmentation, not a live alarm rule.

Related: [[Structural breaks and parameter instability]] · [[Forecast evaluation]] · [[Data vintage and real-time testing]]
