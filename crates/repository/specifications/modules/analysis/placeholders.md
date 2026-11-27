# Candidate content gaps

**ZIP-REPOSITORY-ANALYSIS-PLACEHOLDERS-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/analysis/placeholders.rs`

## Required implementation behavior

Use explicit heuristics for empty files, repeated boilerplate and markers. Preserve paths/source evidence and require context review. Do not silently replace candidates.

## Acceptance

**ZIP-REPOSITORY-ANALYSIS-PLACEHOLDERS-T01.** False-positive fixture produces candidate status requiring review.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
