# Regression, covariance, and PCA

## Regression as projection

OLS minimizes \(\|y-X\beta\|^2\). Differentiating gives \(X^TX\hat\beta=X^Ty\); with full column rank, \(\hat\beta=(X^TX)^{-1}X^Ty\). Residuals are orthogonal to columns of \(X\). In computation, use QR/SVD rather than explicitly inverting the Gram matrix. Under exogeneity \(E[\epsilon\mid X]=0\), coefficients target the conditional linear projection; classical standard errors additionally require suitable error assumptions.

Sample covariance \(S=(n-1)^{-1}X_c^TX_c\) is noisy, especially when asset count is comparable to observations. PCA eigendecomposes covariance (or uses SVD) to maximize variance captured; it does not maximize predictiveness or identify causal factors.

## Worked example

Two standardized assets have correlation 0.8, giving covariance matrix \(\begin{bmatrix}1&.8\\.8&1\end{bmatrix}\). Eigenvectors are common mode \((1,1)/\sqrt2\) with eigenvalue 1.8 and spread mode \((1,-1)/\sqrt2\) with eigenvalue 0.2. The first component explains 90% of total variance. A 50/50 portfolio has variance \((1+1+1.6)/4=0.9\), while a dollar-neutral spread has variance \((1+1-1.6)/4=0.1\); estimated low risk is vulnerable to correlation shifts.

## Falsifiable exercise

Using a fixed universe and monthly rolling windows, compare sample-covariance minimum-variance weights with a diagonal-shrinkage version. Test next-month realized volatility and turnover against equal-weight allocation. Reject shrinkage's asserted improvement if it does not reduce the preregistered out-of-sample risk/turnover criterion across the holdout.

## Assumptions and failure modes

OLS coefficient interpretation depends on design and error assumptions; collinearity destabilizes coefficients. Covariance estimates may be singular when \(p\ge n\); even invertible matrices can be poorly conditioned. PCA signs are arbitrary; near-tied eigenvalues permit rotations. Scaling, window selection, universe survivorship, and fitting transformations outside training data cause misleading results.

## Sources

- [Ledoit & Wolf (2004), A well-conditioned estimator for large-dimensional covariance matrices](https://www.ledoit.net/honey.pdf) — **Grade 1**, 2004; novelty high historically; peer-reviewed Journal of Multivariate Analysis paper (author-hosted PDF). Direct paper reviewed by citation/URL; shrinkage guarantees are setting-dependent, not universal investment performance.
- [NIST: Principal Components](https://www.itl.nist.gov/div898/handbook/pmc/section5/pmc55.htm) — **Grade 2**, handbook online; novelty low; official technical reference. Explains PCA use; does not establish financial predictiveness.

Related: [[Linear algebra]] · [[Statistics]] · [[Feature engineering]] · [[Performance]]
