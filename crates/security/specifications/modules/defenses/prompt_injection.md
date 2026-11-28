# Trust separation for content

**ZIP-SECURITY-DEFENSES-PROMPT-INJECTION-001 · v1.1 · Owner:** Security maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/security/src/defenses/prompt_injection.rs`

## Boundary and inputs

Label repository, tool, retrieved and model content with immutable source and scope before assembling a model request. Separate trusted instructions loaded through the authorized instruction path from evidence or proposal text. Even trusted instructions remain subject to the effective grant.

## Behavior and failure handling

Treat untrusted content as data through model assembly and interpretation. Normalize model actions as proposed requests for the usual scope, approval and evidence gates. A text claim of owner consent, privileged role or tool access contributes no actor proof. Missing applicable instructions or uncertain trust blocks the affected protected action.

## Acceptance

**ZIP-SECURITY-DEFENSES-PROMPT-INJECTION-T01.** Feed a synthetic source that claims owner authority and asks for an out-of-scope file change. Confirm it is treated as untrusted evidence, the effective grant is unchanged and no write or external call occurs.
