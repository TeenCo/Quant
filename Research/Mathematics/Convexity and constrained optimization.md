# Convexity and constrained optimization

## Convexity and optimality

A set \(C\) is convex if every segment between points in it stays in it. A function \(f\) is convex if \(f(tx+(1-t)y)\le tf(x)+(1-t)f(y)\). For twice differentiable functions on a convex domain, positive-semidefinite Hessian is sufficient for convexity. Every local minimum of a convex problem is global. Constraints can be represented by convex inequalities \(g_i(x)\le0\) and affine equalities.

For differentiable convex problems under a constraint qualification (often Slater's condition), KKT conditions—primal/dual feasibility, stationarity, complementary slackness—are sufficient for global optimality. Without convexity, KKT points need not be global optima.

## Worked portfolio example

Minimize \(\frac12 w^T\Sigma w\) subject to \(1^Tw=1\), for \(\Sigma=\begin{bmatrix}1&.2\\.2&4\end{bmatrix}\). Since eigenvalues are positive, the objective is strictly convex and the solution is \(w=\Sigma^{-1}1/(1^T\Sigma^{-1}1)\). Inverse-times-ones is proportional to \((3.8,0.8)\), so weights are approximately (0.826, 0.174). Constraints such as long-only or turnover can change the active set and require a solver.

## Falsifiable exercise

Implement this two-asset solution both analytically and with a convex solver; assert budget feasibility, stationarity, and matching objective to numerical tolerance. Then perturb the covariance correlation and measure weight sensitivity. The claim of stable allocation is falsified if small plausible perturbations cause large weight changes.

## Assumptions and failure modes

Covariance must be positive semidefinite; numerical noise may violate it. Expected returns and covariance are estimated, not known. Feasibility and Slater conditions affect KKT guarantees. Nonconvex costs, integer lots, and discrete trade rules break the simple convex guarantee. Solver status is not sufficient: independently check constraints and objective.

## Sources

- [Boyd & Vandenberghe, Convex Optimization](https://web.stanford.edu/~boyd/cvxbook/) — **Grade 1**, 2004 book with slides updated 2023; novelty foundational; academic textbook/site. Official author page reviewed and links to book/slides; examples are mathematical, not evidence of trading profitability. Copyright remains with publisher; linked only.
- [CVXPY documentation](https://www.cvxpy.org/tutorial/intro/index.html) — **Grade 2**, current online docs; novelty low; software documentation. Useful implementation reference; solver numerics and modeling errors remain user responsibility.

Related: [[Calculus and optimization]] · [[Linear algebra]] · [[Portfolio construction and estimation risk]]
