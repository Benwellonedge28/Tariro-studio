# Egress authorization boundary

**ZIP-SECURITY-DEFENSES-DATA-EXFILTRATION-001 · v1.0 · Owner:** Security maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/security/src/defenses/data_exfiltration.rs`

## Required implementation behavior

Bind destination, data class, purpose and operation to approved scope. Validate before transmission and revalidate redirects. Filter body according to policy.

## Acceptance

**ZIP-SECURITY-DEFENSES-DATA-EXFILTRATION-T01.** Redirect to disallowed destination causes no second request.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
