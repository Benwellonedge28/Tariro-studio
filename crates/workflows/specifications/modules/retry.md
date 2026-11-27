# Policy-limited step retry

**ZIP-WORKFLOWS-RETRY-001 · v1.0 · Owner:** Workflows maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/workflows/src/retry.rs`

## Required implementation behavior

Retry only definitive transient or verified-absent effects with unchanged identity, live grant and remaining attempt/deadline budget.

## Acceptance

**ZIP-WORKFLOWS-RETRY-T01.** Unknown remote mutation blocks generic retry.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
