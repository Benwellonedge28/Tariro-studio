# Bounded deterministic tree scan

**ZIP-FILESYSTEM-TRAVERSAL-001 · v1.0 · Owner:** Filesystem maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/filesystem/src/traversal.rs`

## Required implementation behavior

Traverse authorized directories with stable order, count/depth/byte budgets and optional pinned cursor. Report partial scans, forbidden entry types and non-recoverable positions.

## Acceptance

**ZIP-FILESYSTEM-TRAVERSAL-T01.** Mid-scan quota exhaustion returns partial result and no false completeness.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
