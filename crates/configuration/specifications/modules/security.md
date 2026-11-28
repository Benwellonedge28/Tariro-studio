# Security configuration validation

**ZIP-CONFIGURATION-SECURITY-001 · v1.1 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/security.rs`

## Boundary and inputs

Project only validated security configuration, source authority and policy references from the effective snapshot. Bind isolation requirements, data classes and egress restrictions to their declared scope and revision. Supply opaque credential references to entitled adapters and keep values, token contents and adapter connection logic outside Configuration. Use [mandatory intersections](overrides.md) for conflict handling.

## Behavior and failure handling

Reject an untrusted layer that attempts to grant egress or lower mandatory isolation. For a missing required control, fail activation when required for the selected profile or mark the affected operation unavailable when optional under policy. Verify runtime enforcement and current permission at the owning execution boundary. Reject unavailable required credential references through an authorized capability observation, with redacted diagnoses. Offline policy yields no implicit external check.

## Acceptance

**ZIP-CONFIGURATION-SECURITY-T01.** Use a missing isolation control and two profiles with different requirement classes. Observe activation failure or explicit operation unavailability as applicable. Attempt a workspace egress grant and confirm denial. Serialize a redacted snapshot and inspect that no credential payload appears.
