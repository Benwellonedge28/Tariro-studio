# Qualified regression comparison

**ZIP-MAINTENANCE-REGRESSION-DETECTION-001 · v1.0 · Owner:** Maintenance maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/maintenance/src/regression_detection.rs`

## Required implementation behavior

Compare matched fixtures, revisions, environment and expected thresholds, preserve inconclusive observations.

## Acceptance

**ZIP-MAINTENANCE-REGRESSION-DETECTION-T01.** Different runtime profile prevents direct regression verdict.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
