# Runtime Reduction and Code Execution Optimization

The best performance improvement is often to avoid unnecessary computation while preserving correctness. Profile before optimizing.

## Workflow

1. Define a reproducible benchmark and output-equivalence tolerance.
2. Profile end-to-end and identify bottlenecks (I/O, memory, Python overhead, algorithmic complexity, serialization, numerical kernels, GPU transfer).
3. Improve algorithm/data access first; reduce repeated work and unnecessary precision/rows only with research justification.
4. Vectorize or batch work when it clarifies the computation; avoid giant temporary arrays that cause memory pressure.
5. Use efficient columnar formats (e.g. Parquet), predicate/date pushdown, partitioning, and streaming/chunked reads for large datasets.
6. Cache deterministic transformations with explicit keys including input version, parameters, and code version.
7. Parallelize independent tasks only after measuring resource and reproducibility effects; avoid nested oversubscription.
8. Consider compiled/JIT/GPU execution for measured hot kernels; account for launch/transfer overhead.
9. Re-run correctness, timestamp, and leakage checks after every rewrite.

## Research-compute specific opportunities

- Use rolling sufficient statistics instead of recomputing from scratch.
- Share feature matrices across model variants and avoid repeated joins.
- Use coarse-to-fine parameter search and early stopping without reusing final test data.
- Limit model complexity and data resolution to what the hypothesis needs.
- Record hardware, versions, seeds, wall time, peak memory, and numerical differences.

## Complexity and bottleneck example

Suppose a naive feature builder recomputes a 60-day rolling statistic for every date from all prior rows, causing work to grow roughly quadratically with sample length. A rolling update can maintain a sum/sum-of-squares or use a tested rolling kernel, reducing repeated work toward linear time. For numerically stable variance, prefer a robust online algorithm or validated library rather than subtracting two nearly equal large quantities without checking error.

Profile representative data, not a toy slice that omits I/O or memory pressure. Record wall-clock time, CPU, peak resident memory, I/O volume, and output equivalence. Optimization that changes missing-value, timestamp, or floating-point behavior can change a backtest result; compare outputs with domain-specific tolerances and rerun leakage/data-quality assertions.

## Parallelism and determinism

Parallelize independent instruments, folds, or parameter batches only when results are independent and resource-bounded. Nested BLAS/OpenMP, process pools, and GPU workers can oversubscribe cores and memory. Set thread limits, pin seeds where meaningful, preserve deterministic task IDs, and aggregate outputs in stable order. Floating-point reductions can vary with parallel execution order; quantify acceptable numerical variation.

## Cache invalidation

A cache key should include source snapshot/version, query parameters, transformation code digest, schema, calendar, and relevant environment settings. A cache that omits vintage or universe version can silently reuse stale or hindsight-adjusted data. Cache only deterministic transforms; record whether the value was fetched or recomputed.

## Reliable ingestion under quotas

Chunk large date ranges, paginate deterministically, persist completed partitions, and checkpoint progress. Use bounded exponential backoff for transient failures and respect provider rate limits; do not treat missing pages as empty data. Write each completed partition atomically and maintain a manifest with request range, count, checksum, source version, and status. See [[Research pipeline architecture]].

## Connected notes

[[Research pipelines]] · [[Linear algebra]] · [[Calculus and optimization]] · [[London Strategic Edge]] · [[Profiling vectorization and chunking]] · [[API quotas retries and raw snapshots]]
