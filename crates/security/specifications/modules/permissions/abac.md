# Typed attribute predicates

**ZIP-SECURITY-PERMISSIONS-ABAC-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/permissions/abac.rs`

## Boundary and inputs

Evaluate typed subject, resource, operation and environment attributes from the trusted sources named by each policy rule. Validate scope, edition, origin and freshness before predicate evaluation. Distinguish absent, wrong-type, unknown, and verified values. Treat caller claims as untrusted until their owning verifier qualifies them.

## Behavior and failure handling

For a mandatory predicate, missing or incomparable data denies. Do not coerce unknown classification to public or convert time and quantity with unspecified units. Return the typed criterion and scoped observation references in deterministic order. Policy conjunction and applicable denies stay in [permission composition](mod.md).

## Acceptance

**ZIP-SECURITY-PERMISSIONS-ABAC-T01.** Evaluate a public-only rule with public, restricted, missing, and stale classification inputs. Only the exact current public observation can satisfy that predicate. Each other outcome remains explicit within scoped diagnostics.
