# Evidence reference validation

**ZIP-AUDIT-EVIDENCE-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/evidence.rs`

## Boundary and inputs

Accept a scoped immutable evidence reference, declared digest, requirement, producer edition and owning candidate or effect binding. Resolve its existence and verify content identity through Storage or the trusted evidence adapter. Apply the reader's authorization before retrieving or resolving any reference.

## Behavior and failure handling

Store only bounded redacted metadata and safe links. Distinguish linked, missing, restricted and unverifiable evidence without claiming a verification pass. A missing required object blocks the corresponding gate. Avoid refetching or duplicating raw payload bytes for an Audit record. Preserve original evidence and reason codes through replay.

## Acceptance

**ZIP-AUDIT-EVIDENCE-T01.** Supply a matching reference and a different digest at the same location. Verify only the matching evidence is linked as verified. Remove required evidence and observe an explicit blocked finding without leaking payloads.
