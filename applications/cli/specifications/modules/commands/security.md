# Security command adapter

**ZIP-CLI-COMMANDS-SECURITY-001 · v1.0 · Owner:** Cli maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `applications/cli/src/commands/security.rs`

## Required implementation behavior

List authorized redacted decisions and audit, or submit scope-specific revocation with current revision. Show actual effect receipt and never print raw credential state.

## Acceptance

**ZIP-CLI-COMMANDS-SECURITY-T01.** Revocation race denies the next privileged operation and retained audit metadata is redacted.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
