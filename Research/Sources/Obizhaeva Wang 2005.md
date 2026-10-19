# Optimal Trading Strategy and Supply/Demand Dynamics

## Bibliography

- **Authors:** Anna A. Obizhaeva and Jiang Wang
- **Date / version:** NBER Working Paper 11444, June 2005; published in *Journal of Financial Markets* 16(1), 2013, pp. 1–32.
- **DOI:** [10.3386/w11444](https://doi.org/10.3386/w11444)
- **Primary record:** [NBER Working Paper 11444](https://www.nber.org/papers/w11444)
- **Paper PDF:** linked from the NBER record; not copied locally.

## Assessment

- **Evidence grade:** 2 — influential formal microstructure/execution research, but the model is older and its market assumptions must be checked against current venue mechanics.
- **Recency:** 2005 working paper / 2013 journal publication; foundational rather than current empirical calibration.
- **Novelty:** Treats supply/demand as an intertemporal, replenishing object and studies execution when trade timing is endogenous.
- **Source type:** Peer-reviewed journal article / NBER working paper.

## Summary

The paper develops a limit-order-book framework where supply and demand evolve over time. It argues that replenishment dynamics matter for execution cost and optimal order timing. In the model, optimal strategies may combine discrete and continuous trades; the paper also connects execution choices to intraday volume, volatility, and prices.

## Research use and caveats

- Core takeaway: liquidity is dynamic; static spread/depth snapshots may not describe the cost of a schedule.
- Do not treat the model's proposed schedule as a universal modern execution algorithm. Venue rules, hidden liquidity, information asymmetry, latency, and impact differ.
- Useful for specifying replenishment/resiliency measures and for distinguishing static depth from dynamic response.
- Empirical implementations should use point-in-time book events and compare predicted execution costs with realized shortfall.

## Connected notes

[[Market microstructure]] · [[Execution costs and market impact]] · [[Order book data and event-time reconstruction]] · [[Futures]] · [[Equities]]
