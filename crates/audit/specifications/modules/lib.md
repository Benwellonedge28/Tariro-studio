# Audit service facade

**ZIP-AUDIT-LIB-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/lib.rs`

## Boundary and inputs

Declare the [Audit crate modules](../../DESIGN.md) and forbid unsafe first-party code. Export typed redacted append staging, bounded scoped query, integrity verification and qualified export ports. Keep canonical record constructors, raw store handles and signer credentials private.

## Behavior and failure handling

Use Foundation, Storage and Security as the only first-party dependencies. Compose callers through injected audit and scope verification ports. All append inputs cross the same redaction and canonical validation boundary. Importing the crate does not open a store or initiate an export. Only the owning Storage transaction commits an append.

## Acceptance

**ZIP-AUDIT-LIB-T01.** Compile a downstream consumer using synthetic scoped audit inputs. Verify raw constructors and direct hash-chain mutation are private, and that import and read-only inspection perform no writes or egress.
