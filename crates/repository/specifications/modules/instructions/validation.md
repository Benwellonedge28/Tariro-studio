# Instruction bundle provenance

**ZIP-REPOSITORY-INSTRUCTIONS-VALIDATION-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/instructions/validation.rs`

Seal the immutable base commit, stable repository ID, canonical sorted affected path set, per-target ancestor associations, candidate paths with checked absence or regular blob identity, raw payload digest, reviewed interpretation version and approved constraints digest. Encode a versioned envelope with canonical ordering, explicit presence and object-format tags, and length-prefixed identifiers and paths. Choose the final authority codec and golden vectors before independent approval. The complete bundle is input to commit review and the final effect seal. A skipped, unreadable or unresolved input cannot yield a valid bundle.

Recompute against the exact pinned base and actual staged affected paths before commit and before publishing. A different base, path set, blob identity, grant binding or interpretation requires a fresh reviewed seal. Staged rule edits cannot satisfy review for their own mutation.

**ZIP-REPOSITORY-INSTRUCTIONS-VALIDATION-T01.** Change applicable instructions or add a new affected path after approval. The stale bundle cannot authorize publication.
