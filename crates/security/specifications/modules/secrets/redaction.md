# Structured redaction rules

**ZIP-SECURITY-SECRETS-REDACTION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/secrets/redaction.rs`

## Boundary and inputs

Reduce structured observations through a validated allowlist before serializing them for prompts, logs, audit, telemetry or support. Classify nested fields at their owning boundary and remove raw credential bytes, authentication material and sensitive adapter diagnostics. Keep approved identifiers or safe evidence references only where output scope allows.

## Behavior and failure handling

Do not pass raw unchecked strings into diagnostics. Use a bounded safe fallback code when required data cannot be reduced safely. Fail a privileged append or transfer when mandatory evidence cannot be made appropriate for its audience. Do not hash plaintext credentials for public evidence or assume a later redaction layer repairs a disclosure.

## Acceptance

**ZIP-SECURITY-SECRETS-REDACTION-T01.** Inject a synthetic canary in nested fields and adapter errors. Verify it is absent from evaluated prompt, log, audit and telemetry payloads. Force failed redaction and check no protected output is emitted.
