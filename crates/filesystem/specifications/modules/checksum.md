# Streaming byte integrity

**ZIP-FILESYSTEM-CHECKSUM-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/checksum.rs`

## Boundary and inputs

Read a scoped immutable or identity-pinned object under an admitted byte, scratch buffer and time envelope. Bind expected digest algorithm and optional exact length to the read request. Stream into the qualified Security hash port rather than materializing an unbounded file.

## Behavior and failure handling

Count bytes with checked arithmetic and require complete EOF for a verified receipt. Differentiate premature EOF, over-limit input, byte mismatch and changed object identity. Keep partial checksums provisional. Return the scoped digest and verified size without leaking path or payload.

## Acceptance

**ZIP-FILESYSTEM-CHECKSUM-T01.** Read unchanged, mutated, truncated and oversized fixtures. Only the first can satisfy the original expected length and digest. Inject a changing identity after the last chunk and verify a current proof is required.
