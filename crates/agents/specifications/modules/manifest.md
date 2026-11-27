# Versioned role manifest

**ZIP-AGENTS-MANIFEST-001 · v1.0 · Owner:** Agents maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/agents/src/manifest.rs`

## Required implementation behavior

Declare role, capabilities, budgets, allowed data and adapter versions. Normalize and hash before approval; unsupported mandatory fields deny.

## Acceptance

**ZIP-AGENTS-MANIFEST-T01.** Changed manifest cannot execute under previously reviewed digest.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
