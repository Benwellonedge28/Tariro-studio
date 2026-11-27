# Forgejo provider mapping

**ZIP-REPOSITORY-PROVIDERS-FORGEJO-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/providers/forgejo.rs`

## Required implementation behavior

Bind configured origin and stable repo identity. Negotiate deployed version capabilities and redact upstream errors; no inference from compatible route names.

## Acceptance

**ZIP-REPOSITORY-PROVIDERS-FORGEJO-T01.** Different server version with no qualified feature gives unsupported outcome.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
