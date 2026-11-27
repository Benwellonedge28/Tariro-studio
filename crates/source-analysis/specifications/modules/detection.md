# Deterministic language detection

**ZIP-SOURCE-ANALYSIS-DETECTION-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/detection.rs`

## Required implementation behavior

Prefer approved explicit hints, then qualified recognition from path and bounded byte prefix. Record uncertain ties and fallback to text only.

## Acceptance

**ZIP-SOURCE-ANALYSIS-DETECTION-T01.** Ambiguous extension and absent parser produce explicit unknown detection.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
