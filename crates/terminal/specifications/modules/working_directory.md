# Scoped cwd resolution

**ZIP-TERMINAL-WORKING-DIRECTORY-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/working_directory.rs`

## Required implementation behavior

Obtain validated directory identity and lease; revalidate before launch with qualified containment. No silent fallback to process cwd.

## Acceptance

**ZIP-TERMINAL-WORKING-DIRECTORY-T01.** Replacing cwd with an unsafe link denies execution.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
