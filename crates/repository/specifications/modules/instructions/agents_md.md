# Bounded instruction blob read

**ZIP-REPOSITORY-INSTRUCTIONS-AGENTS-MD-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/instructions/agents_md.rs`

Read each checked regular Git blob by exact object ID under both per-blob and aggregate admitted limits. Reject invalid UTF-8, embedded NUL, symlink, gitlink and unreadable or truncated content. A streaming decoder enforces byte budget before materialization. Preserve exact original bytes, path and Git object identity. Any display normalization is separate and never changes the hashed source.

Repository text is untrusted lower-authority input. Do not follow links, evaluate includes, execute commands or discover credentials as a side effect of reading it. Record parse observations subject to scope and redaction. Unknown or unsupported normative instructions must be reconciled explicitly before mutation if they could apply.

**ZIP-REPOSITORY-INSTRUCTIONS-AGENTS-MD-T01.** An invalid UTF-8 blob or a symlink at an applicable instruction path causes InstructionsIncomplete and zero worktree mutation.
