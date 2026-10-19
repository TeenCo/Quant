# Perpetual funding and venue clocks

Parent: [[Crypto]]. Related: [[Market microstructure]], [[Execution costs and market impact]].

## Funding is a cash flow, not yield

Funding transfers between long and short accounts at venue-defined intervals. Sign conventions differ by venue; verify whether positive funding means longs pay shorts. A linear contract position of q base units with mark M and funding rate f has approximate payment \(qMf\) in quote currency (positive means debit under the stated convention). Inverse contracts require their settlement-currency formula. Funding rates are not interchangeable across venues or forecast periods.

## Example

Long 0.5 BTC linear perpetual, mark $60,000, funding +0.01% per 8h with longs paying: payment is \(.5\times60,000\times.0001=$3\). Three intervals at unchanged rate would cost $9 before price P&L, fees, collateral yield, slippage and liquidation effects.

## Fields and clocks

Store venue/product/version, contract type and multiplier, base/quote/settlement and margin currency, funding rate and formula inputs, predicted versus final rate, funding interval and exact settlement timestamp, mark/index constituents, trade and quote event/receive timestamps, fee tier, position, collateral, liquidation thresholds, outages and instrument status. Convert UTC carefully; settlement schedule can vary by product and change over time. Preserve raw venue records and API documentation version.

## Failure modes

Invert payment sign; annualize one observation as stable yield; apply linear formula to inverse contracts; use last price instead of specified mark; miss settlement boundary or venue schedule change; ignore fees, basis, collateral, ADL/liquidation, outages and venue credit; assume simultaneous fills or withdrawal availability.

## Falsifiable exercise

For one explicitly specified venue and contract, reconstruct funding debits/credits from historical position snapshots and official settlement records, and reconcile against account-level or independently recorded cash flows where available. Pre-register holding windows and compare net basis P&L with a no-funding control, including executable spreads and failed-fill sensitivity. The result tests accounting and implementation, not alpha.

## Source leads

- Binance USDⓈ-M Futures API, funding history (official venue API; grade 2 for fields/endpoints, live documentation, high operational specificity; venue-specific, current docs may differ from historical rules): https://developers.binance.com/docs/derivatives/usds-margined-futures/market-data/rest-api/Get-Funding-Rate-History .
- CME, Cryptocurrency futures (regulated exchange product conventions; grade 2, current product pages, moderate novelty; dated futures, not crypto perpetuals): https://www.cmegroup.com/markets/cryptocurrencies.html .
