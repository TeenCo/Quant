# Daily leveraged ETF reset and path dependence

Parent: [[ETFs]]. Related: [[Time series]], [[Execution costs and market impact]].

## Daily target versus holding-period multiple

For daily target leverage L, idealized gross NAV evolves \(V_T/V_0=\prod_t(1+Lr_t)\), before fees, financing, tracking and distributions. This generally differs from \(1+L(\prod_t(1+r_t)-1)\). The daily objective resets exposure to the next day’s NAV; it does not promise L times a multi-day index return.

## Example

Index rises 10%, then falls 9.0909%: index wealth returns to 1. A frictionless 2x daily fund becomes \(1.20\times(1-.181818)=.981818\), down 1.82%. This is path dependence, not a forecast of actual fund tracking.

## Fields and clock

Use fund objective/prospectus, daily NAV total return, benchmark total return with matching close, distributions/splits, daily target leverage, expense/financing charges, swap/futures holdings, rebalance and valuation time, market price and bid/ask, benchmark session, and fund/benchmark holiday calendar. Compare NAV with NAV for implementation mechanics; market-price returns add premium/discount noise.

## Failure modes

Apply the multiple over arbitrary horizons; compound close-to-close returns with mismatched closes; omit financing, fees, derivatives roll, tracking error and distributions; use price-only benchmark; infer daily path from monthly endpoints; assume realized volatility alone explains tracking.

## Falsifiable exercise

Reconstruct daily NAV wealth from benchmark daily total returns and stated target, then compare observed NAV residuals over a preselected sample. Regress residuals on expense accrual, financing proxies, rebalance-day moves and tracking factors using only contemporaneous data. Report forecast errors and uncertainty, not a presumed volatility edge.

## Source leads

- SEC Investor Bulletin (official; grade 2 for product risk explanation, current web resource, low novelty; general, not fund-specific daily holdings): https://www.sec.gov/investor/pubs/leveragedetfs-alert.htm .
- FINRA, Non-Traditional ETFs (regulatory investor education; grade 3, older but maintained, low novelty; not a price-performance study): https://www.finra.org/investors/investing/investment-products/exchange-traded-funds-etfs/non-traditional-etfs .
