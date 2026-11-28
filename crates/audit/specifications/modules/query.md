# Bounded authorized audit query

**ZIP-AUDIT-QUERY-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/query.rs`

## Boundary and inputs

Authorize the caller, exact workspace, filters, disclosure scope and snapshot before reading the audit stream. Return bounded typed views ordered by workspace sequence. Bind continuation to scope, filter, retained generation, next sequence and authorized cursor lifetime. Treat a cursor as a locator requiring fresh authority.

## Behavior and failure handling

Bound scanned and returned items and bytes under resolved policy. Compare the pinned generation and validated earliest retained position before continuing. Return CursorExpired for an authorized obsolete continuation and do not expose hidden ranks or counts to an unauthorized requester. Build summaries from redacted records or verified evidence references without reading raw referenced payloads.

## Acceptance

**ZIP-AUDIT-QUERY-T01.** Use a cursor from a different workspace, one made obsolete by retention and one current authorized cursor. Verify forbidden or expired outcomes as applicable and stable order within the permitted stream.
