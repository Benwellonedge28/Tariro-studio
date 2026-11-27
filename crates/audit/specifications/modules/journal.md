# Ordered atomic audit append

**ZIP-AUDIT-JOURNAL-001 · v1.0 · Owner:** Audit maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/audit/src/journal.rs`

## Required implementation behavior

Allocate next sequence under writer, append record with prior digest and record related intent in the same transaction. Missing prior digest or sequence overflow denies.

## Acceptance

**ZIP-AUDIT-JOURNAL-T01.** Concurrent appends maintain one contiguous chain.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
