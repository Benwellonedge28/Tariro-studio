# Scoped audit export

**ZIP-AUDIT-EXPORT-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/export.rs`

## Boundary and inputs

Accept an exact scope, immutable snapshot range, current authority, bounded item and byte envelope and approved destination. Filter through [query](query.md) and redact into a distinct export representation. Stage a manifest binding source generation, filters, redaction policy, retained evidence references, range and exported byte digest.

## Behavior and failure handling

Validate the source chain under permitted qualified access and label the export's coverage. A filtered or projected export cannot substitute for a full canonical chain. Enforce bytes and items before staging growth and again before transfer. Require a fresh destination and data disclosure grant at the owning effect boundary. An ambiguous transfer response retains its original intent. Do not widen decryption or evidence access while exporting.

## Acceptance

**ZIP-AUDIT-EXPORT-T01.** Attempt transfer to an unapproved destination and verify zero outbound calls. Revoke after staging and verify the bundle remains untransferred. Change a staged byte and confirm digest verification blocks publication.
