# Bounded graph walk

**ZIP-KNOWLEDGE-TRAVERSAL-001 · v1.0 · Owner:** Knowledge maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/knowledge/src/traversal.rs`

## Required implementation behavior

Visit stable eligible edge order, enforce visited/depth/result/resource limits before expansion and report explicit truncation.

## Acceptance

**ZIP-KNOWLEDGE-TRAVERSAL-T01.** Cycle terminates and configured lower depth changes output without rebuild.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
