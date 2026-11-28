# Role descriptor registry

**ZIP-AGENTS-ROLES-MOD-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/mod.rs`

## Boundary and inputs

Expose versioned role descriptors keyed by canonical role ID and edition. Bind each descriptor to allowed proposal families, required capabilities and required evidence. Construct from the installed, reviewed role catalog. Roles describe distinct duties; the active grant and effect boundary determine the actual permitted actions.

## Behavior and failure handling

Reject duplicate role/edition definitions or unsupported mandatory descriptors before binding an agent. Resolve a request to exactly one enrolled role and retain its reviewed manifest digest. Unknown roles and model labels cannot select a fallback or widen permissions. Check the instance identity and policy at use time.

## Acceptance

**ZIP-AGENTS-ROLES-MOD-T01.** Register two conflicting descriptors for one edition, then request an unknown role. Both deny. Resolve a known version while a capability is revoked and verify the descriptor grants no execution.
