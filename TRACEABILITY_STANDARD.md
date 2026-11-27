# Requirement-to-evidence traceability

**ZIP-TRC-001 · v1.0 · Owner:** Architecture and verification maintainers. **Maturity:** D4 candidate.

Use immutable requirement IDs of the form `ZIP-<DOMAIN>-<NUMBER>`. Never reuse a retired ID. Record scope, owner, status, version introduced, and link to superseding IDs for retired requirements. Tie each to design section, exact source-file path, test IDs, expected evidence and release gate. Mark planned source as planned.

For a release bind requirements and test evidence to the reviewed artifact digest, source revision, policy and toolchain. Input changes invalidate affected evidence. An approved implementation exception must record expiry and approving authority. Lack of evidence maps to blocked rather than implicitly passed.

CI validation rejects duplicate IDs, orphan links, requirements without tests, and evidence that does not match the candidate. A trace row with unresolved dependency decisions cannot claim D5.
