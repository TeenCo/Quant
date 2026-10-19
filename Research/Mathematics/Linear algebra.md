# Linear Algebra and Matrix Methods

## Essential objects

Vectors encode observations, states, or exposures; matrices encode linear maps, covariance, designs, or portfolios. The concepts most useful in research include inner products, norms, rank, span, basis, orthogonality, projections, least squares, eigenvalues/eigenvectors, singular value decomposition, and matrix conditioning.

## Quantitative applications

- Regression and least squares: projection of the target onto a feature span.
- Covariance and PCA: variance structure, factor exposures, dimensionality reduction.
- Portfolio risk: quadratic forms such as `wᵀΣw` and constraints on weights.
- Numerical stability: ill-conditioned matrices can make estimates sensitive to tiny data changes.
- Neural networks: batched matrix operations dominate many model computations.

## Research cautions

Sample covariance can be noisy in high dimensions; regularization and shrinkage trade bias for variance. PCA components are sample-dependent and can rotate across regimes. Standardization and dimension reduction must be fitted inside each training window to prevent leakage.

## Worked derivation: least squares is a projection

For a design matrix \(X\in\mathbb{R}^{n\times p}\) and target \(y\), ordinary least squares chooses \(\hat\beta\) to minimize \(\|y-X\beta\|_2^2\). If columns of \(X\) are linearly independent, differentiating gives the normal equations

\[
X^TX\hat\beta=X^Ty,\qquad \hat\beta=(X^TX)^{-1}X^Ty.
\]

The fitted vector \(\hat y=X\hat\beta\) is the orthogonal projection of \(y\) onto the column space of \(X\); the residual obeys \(X^T(y-\hat y)=0\). If columns are collinear or nearly collinear, \(X^TX\) is singular or ill-conditioned, making coefficients unstable even when fitted values appear stable. Use QR/SVD solvers rather than explicitly forming an inverse in numerical code, and inspect condition numbers and coefficient sensitivity.

### Covariance risk and shrinkage

For portfolio weights \(w\) and covariance estimate \(\hat\Sigma\), estimated variance is \(w^T\hat\Sigma w\). Small estimation errors in \(\hat\Sigma\) can cause large weight changes when optimization seeks extreme low-variance directions. A simple shrinkage form is

\[
\hat\Sigma_\lambda=(1-\lambda)S+\lambda T,
\]

where \(S\) is the sample covariance, \(T\) a structured target (for example, diagonal or constant-correlation), and \(\lambda\in[0,1]\). Shrinkage adds bias toward the target but can reduce estimation variance. Choose \(\lambda\) inside the research training window; evaluate realized risk and turnover out of sample. The target itself encodes assumptions and should be documented.

## PCA example and interpretation

For centered data matrix \(X\), SVD writes \(X=U\Sigma V^T\). Columns of \(V\) define orthogonal directions in feature space, while singular values in \(\Sigma\) measure sample variation along those directions. PCA maximizes variance captured, not predictiveness, causal meaning, or stability. A high-variance market component may represent broad risk rather than an exploitable signal. Refit and align components carefully across windows; component signs are arbitrary, and near-equal eigenvalues permit rotations.

Related: [[Statistics]] · [[Feature engineering]] · [[Overfitting controls]] · [[Performance]]

## Further links

[[Mathematics]] · [[Statistics]] · [[Feature engineering]] · [[Performance]]

Focused foundation: [[Regression covariance and PCA]]
