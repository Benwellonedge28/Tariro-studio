# Qualified capability registry

**ZIP-TOOLS-REGISTRY-001 · v1.0 · Owner:** Tools maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/tools/src/registry.rs`

## Required implementation behavior

Index admitted descriptors by stable ID and version. Resolve request against negotiated interface and current policy; duplicate version identity conflicts.

## Acceptance

**ZIP-TOOLS-REGISTRY-T01.** A mismatched version never silently routes to another adapter.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
