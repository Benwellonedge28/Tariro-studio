# Role descriptor registry

**ZIP-AGENTS-ROLES-MOD-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/roles/mod.rs`

## Required implementation behavior

Expose explicit versioned role descriptors with allowed proposal types and evidence requirements. Role labels alone never convey permissions.

## Acceptance

**ZIP-AGENTS-ROLES-MOD-T01.** Unknown role cannot authorize fallback execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
