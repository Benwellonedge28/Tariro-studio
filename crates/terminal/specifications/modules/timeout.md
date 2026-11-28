# Effective wall-time deadline

**ZIP-TERMINAL-TIMEOUT-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/timeout.rs`

## Boundary and inputs

Compute effective deadline from the earliest finite live monotonic request, terminal.deadline_ms policy and applicable lease deadline. Compare only qualified local clock-domain instants and check converting relative time before opening the execution gate. Expire at equality.

## Behavior and failure handling

On expiry notify the supervising owner and close new execution or publication. Use separately authorized cleanup with its own bounded grace. Expiry after uncertain external dispatch is not evidence of absence. Never restore fresh execution authority from an old observed instant or wall-clock adjustment.

## Acceptance

**ZIP-TERMINAL-TIMEOUT-T01.** Change UTC during a synthetic run and verify the monotonic cutoff is unchanged. Race capped expiry with exit and confirm it remains distinct from explicit cancellation and confirmed cleanup.
