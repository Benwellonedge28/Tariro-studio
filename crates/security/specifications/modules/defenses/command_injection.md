# Structured execution defense

**ZIP-SECURITY-DEFENSES-COMMAND-INJECTION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/defenses/command_injection.rs`

## Required implementation behavior

Reject shell fragments from untrusted sources, validate executable and each argument independently and route through admitted terminal capability.

## Acceptance

**ZIP-SECURITY-DEFENSES-COMMAND-INJECTION-T01.** Synthetic metacharacters remain data and cannot introduce an extra command.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
