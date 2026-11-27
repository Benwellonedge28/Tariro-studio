# Effective command policy

**ZIP-TERMINAL-POLICY-001 · v1.0 · Owner:** Terminal maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/terminal/src/policy.rs`

## Required implementation behavior

Intersect executable, arguments, env names, path, network and interactive permission with current grant. Direct shell usage requires separate explicit capability.

## Acceptance

**ZIP-TERMINAL-POLICY-T01.** A general read operation cannot enable interactive shell.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
