# Enforced process budgets

**ZIP-SANDBOX-RESOURCE-LIMITS-001 · v1.1 · Owner:** Sandbox maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/sandbox/src/resource_limits.rs`

## Boundary and inputs

Translate each finite typed admitted dimension into predicates the selected platform adapter can enforce and observe. Check unit conversions, zero semantics, overflows and platform sentinel values before applying. Preserve explicit zero only where the declared resource policy allows that value.

## Behavior and failure handling

Confirm effective limits after installation and before workload entry. Reject unsupported or unintentionally unbounded mappings, including where a platform value silently means unlimited. Track output bytes while reading within a bounded buffer. Exceeded limits request supervised stop, without releasing holds or changing prior accepted evidence.

## Acceptance

**ZIP-SANDBOX-RESOURCE-LIMITS-T01.** Inject a configured bound whose adapter representation means unbounded. Verify setup denies. Exhaust an admitted output envelope in a benign fixture and confirm bounded reads, supervised stop and retained cleanup evidence.
