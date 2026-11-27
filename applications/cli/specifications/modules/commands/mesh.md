# Mesh command adapter

**ZIP-CLI-COMMANDS-MESH-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/mesh.rs`

## Required implementation behavior

Join using explicit invitation reference after node and egress policy checks. Nodes and status are scoped reads. Do not enable discovery automatically.

## Acceptance

**ZIP-CLI-COMMANDS-MESH-T01.** No authorized invitation or offline mode yields denial before network.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
