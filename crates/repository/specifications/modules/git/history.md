# Bounded snapshot ancestry read

**ZIP-REPOSITORY-GIT-HISTORY-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/history.rs`

## Required implementation behavior

Walk immutable commit ancestry under cursor and revision algorithm. Mark truncation explicitly and normalize timestamps instead of treating them as topological order.

## Acceptance

**ZIP-REPOSITORY-GIT-HISTORY-T01.** Disconnected or shallow object graph never claims full history.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
