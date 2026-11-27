# Applicable instruction discovery

**ZIP-REPOSITORY-INSTRUCTIONS-DISCOVERY-001 · v1.1 candidate · Owner** Repository maintainers

**Planned source** `crates/repository/src/instructions/discovery.rs`

Input is a verified base snapshot and an authorized set of affected paths. Enumerate exactly `AGENTS.md` at root and in every ancestor directory of each affected file. Include both rename sides, deletion targets and ancestors of newly created paths. New directories absent in the pinned base are recorded as absent. Resolve each candidate by tree traversal, with no worktree fallback and no symlink traversal. A checked absence differs from unreadable content, an incomplete tree, unsupported file mode and a skipped lookup. Only a verified absence may be omitted from applied text.

Deduplicate candidates by exact path. Traverse ancestor depth and then canonical path-byte order within a depth. Retain the complete searched set and per-target association. Enforce configured and admitted path, object and byte budgets before collecting results. If a lookup cannot complete for any affected target, block that candidate mutation.

**ZIP-REPOSITORY-INSTRUCTIONS-DISCOVERY-T01.** A nested rename sees root and both source and destination rules, including an absent destination ancestor when applicable.
