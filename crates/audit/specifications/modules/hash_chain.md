# Canonical tamper-evident chain

**ZIP-AUDIT-HASH-CHAIN-001 · v1.1 · Owner:** Audit maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/audit/src/hash_chain.rs`

## Boundary and inputs

Compute the candidate v1 record digest using the Security hashing port with SHA-256. Hash, in order, the ASCII bytes zipporah:audit:record:v1, one zero byte, the 32 raw predecessor digest bytes, then the canonical body bytes from [record](record.md). The genesis predecessor is 32 zero bytes only at workspace sequence 1. Use Foundation's tagged digest representation in persisted records.

## Behavior and failure handling

The canonical body binds workspace and sequence. For a later sequence require the preceding committed digest or the exact qualified retention anchor, never genesis. Check sequence continuity before hashing. No free-text payload enters the body. A chain check detects data incompatible with its trusted boundary. End-to-end history and truncation claims require an independently trusted anchor or high-water mark under [integrity](integrity.md).

## Acceptance

**ZIP-AUDIT-HASH-CHAIN-T01.** Create a synthetic chain, reorder two records and mutate a field. Verify the first mismatch is reported for each altered case. Compare two workspaces with otherwise equal inputs and verify their first digests differ.

### Candidate v1 framing vector

For this synthetic nonprivileged case only, use an enrolled operation tag of `observe`. Hash the following exact ASCII body without a trailing newline, using the genesis predecessor.

```json
["1","00000000-0000-4000-8000-000000000001","1","00000000-0000-4000-8000-000000000002",null,"unattributed","observe","00000000-0000-4000-8000-000000000003",null,null,null,null,null,"pending",null,"2026-01-01T00:00:00.000000000Z"]
```

Expected digest `sha256:b80d368d6af9f8e0fa4fe51f28086ea7d434cfce536476771aa426e5e4a87d6f`.
