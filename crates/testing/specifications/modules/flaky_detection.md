# Preserved flaky attempt history

**ZIP-TESTING-FLAKY-DETECTION-001 · v1.0 · Owner:** Testing maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/testing/src/flaky_detection.rs`

## Required implementation behavior

Retry only under reviewed budget, retain every exit and environment, mark mixed outcomes explicitly. Flaky result cannot override a mandatory stable requirement.

## Acceptance

**ZIP-TESTING-FLAKY-DETECTION-T01.** Pass after failure remains flaky, not clean pass.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
