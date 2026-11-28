# Mandatory invariant boundary

**ZIP-GOVERNANCE-CONSTITUTION-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/constitution.rs`

## Boundary and inputs

Load the exact reviewed [constitution](../../../../CONSTITUTION.md) edition and digest from trusted composition. Compile its mandatory invariant identifiers and applicable authoritative controls before loading mutable overlays. If the version, authenticity or required control is unsupported, keep affected operations closed.

## Behavior and failure handling

Do not let workspace, assignment or exception policy weaken an invariant. Incompatible tightening also denies the affected candidate rather than choosing a weaker interpretation. Record the controlling version and invariant in redacted decisions. Constitutional updates require dedicated owner approval, impact analysis, review and validated transition evidence. Retain the active generation if candidate qualification fails.

## Acceptance

**ZIP-GOVERNANCE-CONSTITUTION-T01.** Provide an overlay permitting egress where a constitutional control denies it. Verify the invariant remains effective and the conflicting candidate cannot expand authority.
