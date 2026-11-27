# Admitted independent execution

**ZIP-WORKFLOWS-PARALLELISM-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/parallelism.rs`

Intersect execution plan preferences, assignment and scheduler limits, and live resource admission. Independent ready nodes may run concurrently when every compatibility and conflict condition holds. Canonicalize declared conflict keys by authority domain and normalized path or provider effect target. Take required exclusive keys in canonical order before handoff, with an atomic all-or-none claim. Unknown write sets cannot use parallel mutation. A parallelism preference cannot bypass an exclusive key or a tighter current limit.

Hold conflict ownership through verified settlement. An expired worker cannot use a key, yet the key stays unavailable to replacement writers until fencing and cleanup prove it safe. Never release the conflict key solely because a local wait or timer ended. Within each run, use deterministic ready order subject to current eligibility and scheduler fairness. Resource denial defers rather than fabricating success.

**ZIP-WORKFLOWS-PARALLELISM-T01.** Two otherwise eligible steps writing the same normalized path cannot both dispatch. After a lost receipt, the second waits for reconciliation.
