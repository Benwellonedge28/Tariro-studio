# Finite agent admission

**ZIP-AGENTS-LIMITS-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/limits.rs`

## Boundary and inputs

Read resolved agents.max_mailbox_items and agents.max_delegation_depth from the [resource key catalog](../../../../contracts/resources/budget-keys.json) through composition. Tighten by the authorized assignment, applicable data scope and admitted memory. Keep queue items, charged bytes, delegation depth and monotonic deadline as independent dimensions. A missing required bound blocks admission.

## Behavior and failure handling

Use checked admission arithmetic and no local fallback constants. Compare depth before child registration and mailbox occupancy before insertion. On a tighter reload close affected new admission even if existing occupancy exceeds the new cap. Preserve accepted items and delegate cancellation or drain to the supervisor. Active leases and attempt deadlines remain governed by their owners.

## Acceptance

**ZIP-AGENTS-LIMITS-T01.** Run the same harness under two different mailbox caps and one tighter assignment limit. Verify each boundary without recompilation. Lower the cap below occupied items and verify no new insertion or silent loss.
