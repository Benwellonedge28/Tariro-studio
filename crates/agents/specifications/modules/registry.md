# Agent role and instance registry

**ZIP-AGENTS-REGISTRY-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/registry.rs`

## Required implementation behavior

Index stable identities and versioned manifest; reject duplicate version and require current membership on lookup. Registry is not authority source.

## Acceptance

**ZIP-AGENTS-REGISTRY-T01.** A retired agent cannot be recovered as Ready by name reuse.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
