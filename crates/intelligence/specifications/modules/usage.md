# Observed token and resource usage

**ZIP-INTELLIGENCE-USAGE-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/usage.rs`

## Required implementation behavior

Capture adapter-reported counters, tokenizer/thread context, estimate versus actual, and reconcile unknown provider receipt. Avoid treating absent usage as zero.

## Acceptance

**ZIP-INTELLIGENCE-USAGE-T01.** Provider omission keeps accounting unresolved until classified.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
