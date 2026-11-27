# Workspace configuration overlay

**ZIP-CONFIGURATION-PROJECT-001 · v1.0 · Owner:** Configuration maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/configuration/src/project.rs`

## Required implementation behavior

Bind layer to immutable workspace/project identity and source revision. Project files are lower authority than owner policy. Reject a privileged override rather than silently adopting it.

## Acceptance

**ZIP-CONFIGURATION-PROJECT-T01.** Repository content requesting egress is denied without mutating the active profile.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
