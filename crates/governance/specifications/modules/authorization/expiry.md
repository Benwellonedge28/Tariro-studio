# Grant expiry and clock checks

**ZIP-GOVERNANCE-AUTHORIZATION-EXPIRY-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/authorization/expiry.rs`

## Boundary and inputs

Represent validity as an absolute start-inclusive, expiry-exclusive interval bound to a grant or approval. Read trusted time with qualified uncertainty and compare the full possible current-time interval to the validity window. A new effect requires the interval to lie wholly inside the window. At equality with expiry, deny. Reject absent, untrusted or rolled-back clock observations when verified continuity cannot be established.

## Behavior and failure handling

Keep expiry distinct from the attempt's process-local monotonic deadline. Execute only while both remain valid at their owning boundaries. Never convert a persisted monotonic instant into fresh authority after restart. A short observed pause, replay or local clock adjustment cannot reopen an expired or revoked grant. Preserve history and independently authorized cleanup after expiry. The owning journal must retain observed terminal revocation and any expiry decisions needed to fence future claims.

## Acceptance

**ZIP-GOVERNANCE-AUTHORIZATION-EXPIRY-T01.** Test before start, exact start, exact expiry and uncertainty overlapping expiry. Restart after revocation and move the clock backward. Verify no new operation derives permission from a process snapshot or an expired record.
