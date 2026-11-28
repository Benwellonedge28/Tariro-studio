# Independent reviewer role

**ZIP-AGENTS-ROLES-REVIEWER-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/reviewer.rs`

## Boundary and inputs

Compare the exact pinned candidate, planned scope, reviewed instructions and mandatory acceptance evidence. Verify reviewer independence by scoped principal and policy, not by role label or shared model. Bind observed results to the evidence owner and candidate digest.

## Behavior and failure handling

Report pass, fail or blocked with scoped reasons. A mandatory missing check or changed candidate blocks acceptance. Author self-review can contribute observations but cannot satisfy an independent gate. A matching accepted result is evidence for the owning decision and authorizes no external effect.

## Acceptance

**ZIP-AGENTS-ROLES-REVIEWER-T01.** Assign the author as independent reviewer and verify rejection. Use an eligible reviewer, then change one candidate byte and verify the old verdict no longer applies.
