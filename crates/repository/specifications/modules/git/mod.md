# Restricted Git execution port

**ZIP-REPOSITORY-GIT-MOD-001 · v1.0 · Owner:** Repository maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/repository/src/git/mod.rs`

## Required implementation behavior

Construct structured argv and bounded environment, disable inherited terminal prompts, hooks and unapproved config or credentials. Use authorized executable and isolated workspace root.

## Acceptance

**ZIP-REPOSITORY-GIT-MOD-T01.** Special characters in path are literal argv data and cannot trigger extra command execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
