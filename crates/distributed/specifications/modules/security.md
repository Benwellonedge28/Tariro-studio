# Distributed trust and egress boundary

**ZIP-DISTRIBUTED-SECURITY-001 · v1.0 · Owner:** Distributed maintainers. **Maturity:** D3 file contract draft.

**Planned source:** `crates/distributed/src/security.rs`

## Required implementation behavior

Verify node membership, tenant scope, data locality, signed/approved artifacts and least-privilege tokens before dispatch. Revocation fences further effects.

## Acceptance

**ZIP-DISTRIBUTED-SECURITY-T01.** Wrong node or data class cannot receive artifact.

Before D4, review this file against the component's owning API, error and resource contracts. Define any remaining concrete Rust types, dependencies and fixtures at their respective boundaries. Record independent design review and validation before D5.
