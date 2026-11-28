# Rule normalization and conflict detection

**ZIP-GOVERNANCE-RULES-001 · v1.1 · Owner:** Governance maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/governance/src/rules.rs`

## Boundary and inputs

Normalize registered rule IDs and supported action, identity, path and destination bindings before publishing a policy. Use the owning path and route normalizer with explicit repository, workspace or service scope. Reject ambiguous aliases, wildcard interpretations outside the declared grammar and incompatible units.

## Behavior and failure handling

Canonical equivalent aliases produce one scope identity. An equivalent duplicate can only be collapsed under the reviewed normalization rule. Conflicting definitions under one rule ID deny publication. An explicit allow and a mandatory deny may coexist; the deny wins at evaluation. Export stable ordered rules and provenance for the policy digest.

## Acceptance

**ZIP-GOVERNANCE-RULES-T01.** Normalize two aliases of the same target and verify equal scope without widening. Submit a different target under the same rule ID and verify policy publication fails.
