# Repository path and artifact classification

**ZIP-REPOSITORY-ANALYSIS-STRUCTURE-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/analysis/structure.rs`

## Required implementation behavior

Produce normalized directory/file tree under cursor and stable category labels. Preserve source modes/object digests and report incomplete traversal.

## Acceptance

**ZIP-REPOSITORY-ANALYSIS-STRUCTURE-T01.** Unsupported binary or symlink entry remains explicit.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
