# Observed sandboxed checks

**ZIP-VERIFICATION-DYNAMIC-ANALYSIS-001 · v1.0 · Owner:** Verification maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/verification/src/dynamic_analysis.rs`

## Required implementation behavior

Run only approved executable fixtures in qualified sandbox with admitted resources and capture actual runtime observations. No automatic acceptance from exit code alone.

## Acceptance

**ZIP-VERIFICATION-DYNAMIC-ANALYSIS-T01.** A missing expected report blocks even with zero exit code.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
