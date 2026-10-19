# Profiling, Vectorization, and Chunking

Optimize measured bottlenecks while preserving research semantics. Define representative input, stable output checks, and resource measurements before changing implementation. Separate I/O, parsing, joins, numerical kernels, serialization, and plotting in profiles; end-to-end latency alone can hide memory or correctness costs.

## Benchmark protocol

Record dataset shape/dtypes, sort/order, hardware, software versions, warm/cold cache, wall time, CPU time, peak RSS, bytes read/written, and output checksums or numeric tolerance. Repeat enough runs to report median and dispersion. Compare to a simple trusted baseline; include setup/JIT costs when production-relevant.

Prefer algorithmic improvement and projection/predicate pushdown before low-level tricks. Vectorization can accelerate array kernels but can materialize huge temporaries; chunk by date/entity with overlap equal to rolling lookback. Maintain stable ordering and boundary state so chunked rolling/lag features equal whole-sample results. For grouped operations, preserve group isolation. Cache keys include source/version, parameters, code, calendar and schema.

## Failure modes

Benchmark excludes parse/I/O; vectorized expression changes NaN semantics; chunk boundary loses prior lookback; oversized temporary causes paging/OOM; parallel reductions change floating-point results; nested BLAS oversubscribes; faster join changes duplicate resolution; benchmark uses a tiny cache-hot sample unlike production.

## Falsifiable benchmark exercise

Generate deterministic panel data with multiple entities, missing days and a 20-session rolling statistic. Compare trusted whole-table baseline, vectorized implementation, and chunked implementation across chunk sizes. Require identical keys/missingness and values within declared tolerance; benchmark representative 10x size, reporting median time and peak RSS. A speedup claim fails if results differ, memory exceeds budget, or end-to-end speed (including reads) does not improve.

## Primary references

- [Python profiling documentation](https://docs.python.org/3/library/profile.html) — **Grade 1**, official Python docs, current runtime reference; documents profiler usage, not benchmark methodology for every workload.
- [Apache Arrow Dataset documentation](https://arrow.apache.org/docs/python/dataset.html) — **Grade 1**, primary project docs, maintained; documents columnar scanning/filtering patterns, not guaranteed speedups on a given storage stack.
- [NumPy broadcasting documentation](https://numpy.org/doc/stable/user/basics.broadcasting.html) — **Grade 1**, primary library docs, maintained; explains vectorized broadcasting and memory implications, not domain-specific numerical equivalence.

Connected: [[Performance]] · [[Research pipeline architecture]] · [[Data validation patterns]]
