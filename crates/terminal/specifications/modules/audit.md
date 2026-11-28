# Execution audit intent and outcome

**ZIP-TERMINAL-AUDIT-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/audit.rs`

## Boundary and inputs

Project a redacted intent and outcome record binding command digest, exact actor and scope, attempt identity, grant and resource references, and safe artifact or cleanup evidence. Do not include raw argv, command environments, secret content or raw stream output in audit. Use the injected owning audit participant for required durable evidence.

## Behavior and failure handling

Commit redacted intent before privileged launch and reconcile final observations under the same attempt. A missing required audit write denies dispatch. If outcome persistence is unknown, keep the active obligation and never fabricate a receipt. Digest a reviewed redacted command representation rather than secret material.

## Acceptance

**ZIP-TERMINAL-AUDIT-T01.** Insert synthetic canaries in command inputs and environment. Verify neither enters audit bytes. Fail the required intent append and confirm zero process starts.
