# Candle adapter contract

**ZIP-INFERENCE-BACKENDS-CANDLE-001 · v1.0 · Owner:** Inference maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/inference/src/backends/candle.rs`

## Required implementation behavior

Check supported model/format and device/tokenizer pin, resolve admitted memory and execute under supervised cancellation. Report missing compiled features.

## Acceptance

**ZIP-INFERENCE-BACKENDS-CANDLE-T01.** Unsupported GPU build cannot claim qualified GPU execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
