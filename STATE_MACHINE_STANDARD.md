# Durable state-machine standard

**ZIP-STM-001 · v1.0 · Owner:** Domain and storage maintainers. **Maturity:** D4 candidate.

Define initial, active, suspended, recoverable and terminal states. A machine-readable transition references source, event, guard, destination, atomic writes, resource requirements, audit, recovery and rollback or compensation. A transition is denied unless listed. Terminal states are immutable except separately modeled retention actions.

Within a mutation, validate actor and scope, check record revision, evaluate guards, commit state plus outbox and outcome, then notify. For external effects first persist an intent and fencing/idempotency key; external effects are not part of the local database transaction. Separate an external start from a verified remote result. After interruption recover from durable intent and recorded evidence.

Use a transition matrix with tests for every legal edge and one representative of every illegal edge class. Race two commands on one revision. Replaying an accepted command must return its recorded result without a second transition.
