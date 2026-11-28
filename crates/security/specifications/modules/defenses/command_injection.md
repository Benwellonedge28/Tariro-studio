# Structured execution defense

**ZIP-SECURITY-DEFENSES-COMMAND-INJECTION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/defenses/command_injection.rs`

## Boundary and inputs

Accept only typed executable selection and structured argument values from a qualified tool descriptor. Verify the executable, parameter classes, approved working root, credential handling and environment allowlist. Keep untrusted text in data fields and preserve token boundaries through the owning terminal adapter.

## Behavior and failure handling

Reject requests that would turn data into interpreter control, exceed the approved argument schema or select an unscoped program or path. Qualification requires equivalent behavior at the target platform interface. If argument boundaries cannot be guaranteed, deny. Command construction and review supply no effect authority and do not start processes.

## Acceptance

**ZIP-SECURITY-DEFENSES-COMMAND-INJECTION-T01.** Use a benign fixture that records arguments. Submit inert text containing sentinel punctuation as one argument and verify the same single argument arrives with no additional process. Reject an unqualified execution adapter before dispatch.
