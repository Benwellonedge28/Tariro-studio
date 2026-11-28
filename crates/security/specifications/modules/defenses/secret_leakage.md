# Sensitive content gate

**ZIP-SECURITY-DEFENSES-SECRET-LEAKAGE-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/defenses/secret_leakage.rs`

## Boundary and inputs

Classify data crossing prompt, tool, log, audit and export boundaries before sending or retaining it. Use trusted field schema, scope and configured detector observations. Treat an unknown required classification as unresolved rather than safe. Use reference-only credential handling in approved adapters.

## Behavior and failure handling

Redact through the [secrets reduction boundary](../secrets/redaction.md) before serialization. Block protected disclosure while classification or redaction is incomplete. Record only bounded nonsecret evidence and approved references. Successful filtering does not grant egress or change the data audience.

## Acceptance

**ZIP-SECURITY-DEFENSES-SECRET-LEAKAGE-T01.** Insert a synthetic token in a repository document and in raw adapter diagnostics. Verify neither reaches model context, persisted outputs or unauthorized views. Omit mandatory classification and confirm the boundary blocks disclosure.
