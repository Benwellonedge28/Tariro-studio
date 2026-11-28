# Advisory preference tally

**ZIP-ORCHESTRATION-VOTING-001 · v1.1 · Owner:** Orchestration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/orchestration/src/voting.rs`

## Boundary and inputs

Accept at most one advisory preference per verified eligible principal for one exact proposal digest and round. Preserve observed abstention, support, dissent and invalid input separately. An exact duplicate replays the accepted preference. A different ballot under the same identity is a conflict requiring explicit treatment.

## Behavior and failure handling

Normalize candidate and principal ordering and return counts, ties and evidence references visible to the request scope. Report unavailable or incomplete participation explicitly. A tally cannot widen scope, settle an exclusive-write conflict, bypass independent verification or approve an effect. Only the owning human or policy authority can supply an executable decision.

## Acceptance

**ZIP-ORCHESTRATION-VOTING-T01.** Submit unanimous support with no owner approval and verify the protected operation remains blocked. Replay a ballot and confirm no extra vote. Submit a conflicting ballot and verify its diagnosis remains recoverable.
