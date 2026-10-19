# Alternative-Data Measurement and Negative Controls

## Measurement model

Observed proxy \(Z_t\) reflects latent activity \(A_t\), collector coverage/selection \(S_t\), error \(u_t\), and timing: conceptually \(Z_t=g(A_t,S_t,u_t)\). Coverage growth can move observed counts while activity is unchanged. Job postings, for example, reflect hiring and platform share, duplicates, and scraping coverage.

Choose negative controls before outcomes: an outcome sharing likely confounding/measurement processes but not the proposed causal mechanism, or placebo timestamps. Controls diagnose some biases; they cannot prove all confounding absent.

## Failure modes

- Post hoc placebo choice adds another search.
- Supposedly unrelated control shares the mechanism.
- Backfill or missingness is treated as zero activity.
- Platform growth tracks market outcome.
- Proxy is validated only against its own generating source.

## Falsifiable exercise

Lock one market outcome, one negative-control outcome, placebo period, and publication/receipt lag. Test both in an untouched period and on an independent proxy. Similar effects in control or alignment with coverage changes downgrade the mechanism claim.

## Graded sources

- **Grade 1, methods:** Lipsitch, Tchetgen Tchetgen & Cohen (2010), “Negative Controls: A Tool for Detecting Confounding and Bias.” [DOI](https://doi.org/10.1097/EDE.0b013e3181d61eeb). Diagnostic assumptions limit interpretation.
- **Grade 1, causal reference:** Hernán & Robins, *Causal Inference: What If*. [Free book](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/). General observational methods.
- **Grade 2, internal synthesis:** [[Alternative-data research design]]. No evidence here establishes an alternative-data alpha hypothesis.

Related: [[Alternative-data research design]] · [[Feature engineering]] · [[Data vintage and real-time testing]]
