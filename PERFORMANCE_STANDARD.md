# Performance qualification

**ZIP-PERF-001 · v1.0 · Owner:** Resource and subsystem maintainers. **Maturity:** D4 candidate.

Each performance claim names operation, fixture size, profile, OS, hardware, relevant toolchain/model versions, metric, warmup, sample procedure, percentile or other aggregation, and allowed regression envelope. Adopt a numeric target after recording the qualification assumptions. A configuration budget is an enforcement ceiling; a performance expectation is a measured claim.

Record memory peak across the process tree, disk and I/O, CPU utilization or time, elapsed time, and operation-specific metrics as applicable. Inference records model/quantization, input and output tokens and accelerator memory. Recovery measures detection, replay and delay to resumed work. Keep reproducible raw evidence and distinguish blocked from passed checks.

Compare representative workloads on the same host configuration. Report pressure behavior and failed admission separately. Do not extrapolate personal profile performance to larger or smaller hardware without measurement.
