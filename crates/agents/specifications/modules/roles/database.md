# Database reviewer role

**ZIP-AGENTS-ROLES-DATABASE-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/database.rs`

## Boundary and inputs

Review an exact proposed schema or data migration against pinned storage edition, consumers, compatibility requirements and recovery evidence. Bind a staged trial, change footprint, migration ordering and acceptance criteria to the candidate. Keep original store and assumptions visible.

## Behavior and failure handling

Require a demonstrated restore path to a verified preimage under the owning storage contract. A forward migration without an in-place downgrade also requires explicit approval and must retain a qualified recovery procedure. Block destructive operations that lack recovery evidence. A staged test may use authorized synthetic data only within its defined environment. Production changes require independent scope and approval.

## Acceptance

**ZIP-AGENTS-ROLES-DATABASE-T01.** Offer an irreversible migration with no verified restore evidence. Block the proposal. Qualify a reversible staged fixture and confirm it produces no live storage mutation authority.
