# Debugger role

**ZIP-AGENTS-ROLES-DEBUGGER-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/debugger.rs`

## Boundary and inputs

Accept a scoped failure record, pinned candidate, approved diagnostics and bounded reproduction budget. Use the qualified adapter to collect attributable observations without widening access or touching protected files. Record environment and actual outcome.

## Behavior and failure handling

Distinguish reproduced failure, unavailable evidence and hypothesis. Propose the minimum candidate change supported by observations and keep it bound to the original preimage. Sending candidate edits or executing commands requires the applicable effect scope. Record interrupted runs without manufacturing a result.

## Acceptance

**ZIP-AGENTS-ROLES-DEBUGGER-T01.** Use an unavailable reproduction adapter and then an observed failing fixture. The first returns a hypothesis or unavailable result only. The second supplies a reproducible observation bound to the exact input.
