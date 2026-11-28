# Bounded standard output

**ZIP-TERMINAL-STDOUT-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/stdout.rs`

## Boundary and inputs

Capture ordered stdout under the shared [combined cap](output_limits.md), assigning bounded per-stream observations to the exact process attempt. Reserve bytes before retention and track complete, truncated or unavailable separately. Use safe scoped output projections for user or model disclosure.

## Behavior and failure handling

Treat stream EOF as a stream event. Verified process outcome and cleanup depend on the supervisor. When output is truncated, report a bounded prefix and explicit reason under policy. Never parse text asserting success into a trusted effect receipt.

## Acceptance

**ZIP-TERMINAL-STDOUT-T01.** Flood the synthetic stdout stream and verify the retained bytes do not exceed the combined cap. Use output text claiming success with absent exit proof and confirm the final process disposition stays unresolved.
