# Revision-bound document edits

**ZIP-DOCUMENTATION-EDITING-001 · v1.1 candidate · Owner** Documentation maintainers

**Planned source** `crates/documentation/src/editing.rs`

Check the live approved path, exact expected blob or absence, and applicable pinned instructions before applying any write. Read existing substantive text and keep content, link meaning and provenance outside the approved edit. Restrict documentation-only changes to scoped regular Markdown creates and modifications under the [repository rules](../../../../specifications/1400-repositories/repositories.md). Stage an isolated write of the new bytes and verify the resulting blob and exact change scope. Unchanged bytes are not a new output.

A changed preimage or unexpected local edit is Conflict. Preserve both versions and prompt revalidation through the assignment boundary. Never overwrite by guessing intent or silently rebase. Stage and verify within the admitted file and output budgets. Failed or cancelled staging leaves durable verified progress intact.

**ZIP-DOCUMENTATION-EDITING-T01.** Revise a target after approval and verify the stale edit does not overwrite the new text.
