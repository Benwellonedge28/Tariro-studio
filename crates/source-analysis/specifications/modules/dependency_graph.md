# Pinned source dependency graph

**ZIP-SOURCE-ANALYSIS-DEPENDENCY-GRAPH-001 · v1.0 · Owner:** Source-analysis maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/source-analysis/src/dependency_graph.rs`

## Required implementation behavior

Derive dependencies from qualified imports/manifests and preserve source and revision. Unknown edges remain uncertain. Detect cycles without traversing unauthorized targets.

## Acceptance

**ZIP-SOURCE-ANALYSIS-DEPENDENCY-GRAPH-T01.** An unresolved dynamic import is visible as unknown.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
