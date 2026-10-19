# Multivariable Calculus and Optimization

## Core calculus

For a scalar function of many inputs, the gradient collects first derivatives and points in the direction of steepest local increase. The Hessian describes local curvature. Chain rule composition underlies automatic differentiation and neural-network backpropagation. Constraints require feasible-set reasoning, Lagrange multipliers, or constrained solvers.

## Optimization in research

- Least squares, maximum likelihood, regularized models, and neural-network objectives.
- Portfolio allocation under risk, turnover, leverage, liquidity, and exposure constraints.
- Hyperparameter tuning and resource allocation in experiment pipelines.

## Numerical concerns

Non-convex objectives may have many local solutions; scales and conditioning affect convergence. Monitor objective values, gradients, constraints, random seeds, initialization, stopping rules, and reproducibility. Use simple convex baselines before expensive non-convex optimization.

## Worked example: constrained mean-variance allocation

Consider the convex problem

\[
\min_w\; \frac{\lambda}{2}w^T\Sigma w-\mu^Tw
\quad\text{subject to }\mathbf{1}^Tw=1,
\]

where \(\mu\) is an expected-return vector, \(\Sigma\) a positive-definite covariance matrix, and \(\lambda>0\) risk aversion. The Lagrangian is

\[
\mathcal{L}(w,\nu)=\frac{\lambda}{2}w^T\Sigma w-\mu^Tw+\nu(\mathbf{1}^Tw-1).
\]

Stationarity gives \(\lambda\Sigma w-\mu+\nu\mathbf{1}=0\); therefore

\[
w=\frac{1}{\lambda}\Sigma^{-1}(\mu-\nu\mathbf{1}),
\quad
\nu=\frac{\mathbf{1}^T\Sigma^{-1}\mu-\lambda}{\mathbf{1}^T\Sigma^{-1}\mathbf{1}}.
\]

This closed form illustrates why noisy expected returns and covariance estimates can create extreme weights. Realistic long-only, leverage, sector, turnover, and liquidity constraints typically require a numerical solver and change the active set. Estimation error—not solver sophistication—often dominates apparent precision.

### KKT conditions and verification

For constrained convex problems, verify primal feasibility, dual feasibility, stationarity, and complementary slackness (KKT conditions). After a solver returns, calculate constraint violations and objective independently. A successful status flag alone is insufficient. Compare with a simple baseline and perturb inputs to assess stability.

### Gradient and finite-difference check

For a scalar objective \(f(\theta)\), a central finite-difference approximation is

\[
\frac{\partial f}{\partial\theta_i}\approx\frac{f(\theta+h e_i)-f(\theta-h e_i)}{2h}.
\]

Use scale-aware \(h\) and compare numerically with automatic/analytic gradients on small deterministic cases. Finite differences are diagnostics, not a replacement for correct derivatives; cancellation and nonsmooth operations can cause disagreement.

Connected: [[Linear algebra]] · [[Machine learning]] · [[Edge validation]] · [[Performance]]

## Connected notes

[[Mathematics]] · [[Linear algebra]] · [[Machine learning]] · [[Performance]]

Focused foundation: [[Convexity and constrained optimization]]
