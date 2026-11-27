# Remote provider boundary

**ZIP-INTELLIGENCE-PROVIDERS-REMOTE-001 · v1.0 · Owner:** Intelligence maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/intelligence/src/providers/remote.rs`

## Required implementation behavior

Verify exact destination, data disclosure policy, credentials and spend before sending. Reconcile unknown charge or effect on disconnect.

## Acceptance

**ZIP-INTELLIGENCE-PROVIDERS-REMOTE-T01.** Provider URL change requires revalidation before sending context.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
