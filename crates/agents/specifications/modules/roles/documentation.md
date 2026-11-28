# Documentation role

**ZIP-AGENTS-ROLES-DOCUMENTATION-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/documentation.rs`

## Boundary and inputs

Read the authorized pinned source, instruction bundle and planned change set before drafting. Bind factual claims to exact source path and revision or to clearly attributed design evidence. Stage only approved Markdown and allowed design artifacts when explicitly in scope.

## Behavior and failure handling

Check staged bytes and final-tree links, preserve unsupported or pending statements as proposed behavior, and return a candidate for independent verification. Authoring never implies permission to push, create a PR or merge. A missing claim reference or a conflicting applicable instruction blocks the relevant candidate. See [documentation](../../../../../specifications/1700-documentation/documentation.md).

## Acceptance

**ZIP-AGENTS-ROLES-DOCUMENTATION-T01.** Draft a factual implementation claim without supporting source and verify it fails review. Add a checked source citation and detect a different path that exceeds the authorized batch.
