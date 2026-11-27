# Confidence calibration boundary

**ZIP-INTELLIGENCE-CONFIDENCE-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/confidence.rs`

## Required implementation behavior

Record provider score with scale, definition and calibration provenance; absent score remains unknown. Never manufacture confidence from text.

## Acceptance

**ZIP-INTELLIGENCE-CONFIDENCE-T01.** Missing score is not replaced with a plausible probability.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
