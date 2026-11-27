# Repository, instructions and Git effects

**Contract version** 1.1 candidate. Master design §§30 and 71.

Authorize repository access by immutable provider identity and pin the reviewed branch commit and tree. Inspect applicable `AGENTS.md` at the pin, using both preimage and postimage paths of affected changes. A verified absence is distinct from an incomplete result. Apply scoped and constitutional restrictions before repository text. Repository content supplies context and constraints and cannot grant permission.

Run Git in an isolated leased worktree with bounded output and no inherited executable configuration or credentials. Use the [authoritative staged diff](../../crates/repository/specifications/modules/git/diff.md) and exact seal. A documentation-only grant permits authorized regular text Markdown creates and modifications. Check operation, path, mode and blob identity for both sides of each change. Preserve unrelated state. Default-branch update, merge, force push, deployment and CI policy changes require separate scope.

[Push](../../crates/repository/specifications/modules/git/remote.md) verifies immutable repository, pinned base, target compare, validated commit and live grant. [PR creation](../../crates/repository/specifications/modules/pull_requests/creation.md) binds base and head, approved content, draft flag and stable marker. A provider's non-atomic pre/post verification mode needs explicit policy authorization. Require conditional mutation where the grant requires atomic comparisons. On mismatch preserve verified effects and stop subsequent execution.

Reconcile the original operation identity before retry. A completed matching effect is recorded once, a conflict or uncertainty blocks, and only authoritative absence can authorize reconsidering the exact frozen intent under live scope. The [assignment contract](../1200-assignments/assignments.md) owns progress and effect claim history.

Use the [publication fixtures](../../contracts/acceptance/repository/publication-fixtures.json) for nested instructions, deleted and renamed paths, concurrent base and target changes and duplicate PR reconciliation. Record exact inputs, provider policy, runtime limits and evidence. Map applicable release gates in [requirements](../../REQUIREMENTS.md).

## Implementing components

- [Repository](../../crates/repository/DESIGN.md)
- [Source analysis](../../crates/source-analysis/DESIGN.md)
