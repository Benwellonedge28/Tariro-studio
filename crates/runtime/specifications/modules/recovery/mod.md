# Recovery boundary composition

**ZIP-RUNTIME-RECOVERY-MOD-001 · v1.0 · Owner:** Runtime maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/runtime/src/recovery/mod.rs`

## Required implementation behavior

Expose retry classification and restart reconciliation; recovery uses read-only effect observations unless retry is individually authorized.

## Acceptance

**ZIP-RUNTIME-RECOVERY-MOD-T01.** Unknown effect cannot call a mutation by selecting fallback path.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
