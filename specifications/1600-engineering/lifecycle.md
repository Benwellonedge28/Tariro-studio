# Software lifecycle workflow

**ZIP-ENG-LCY-001 · v1.0 candidate · Owner** Engineering and Workflows maintainers

This contract specifies a reusable workflow over existing subsystem adapters. It recovers the stage model of the [legacy application development modules](../../LEGACY_FEATURE_REGISTER.md). Existing crates continue to own code, workflow state, resource admission and deployment.

## Stage contracts

Each row defines the minimum typed input and the output that permits completion of a required stage. An output refers to a durable artifact and its evidence. Workflow configuration may split a row or combine compatible checks. A required input must still resolve to the declared producing step. Optional omission requires a recorded rationale and policy permitting that omission.

| Stage | Minimum input | Required output and evidence | Owning subsystem |
| --- | --- | --- | --- |
| Concept | Sponsor brief and constraints | Approved problem statement, users and measurable outcome | Engineering |
| Feasibility | Problem statement and explicit assumptions | Evidence-backed feasibility report with alternatives, risks and unresolved gates | Engineering |
| Requirements | Approved outcome and feasibility evidence | Stable requirement IDs, scope and acceptance criteria | Engineering |
| Planning | Requirement revisions and target repository snapshot | Dependency-ordered work plan with estimates and approval boundaries | Assignments |
| Architecture | Requirements and existing boundaries | Approved interfaces, ownership and recorded architecture decisions | Engineering |
| UI/UX | User flows and accessibility requirements | Reviewed prototype or design artifact and accessibility acceptance cases | Studio and Engineering |
| Implementation | Reviewed plan, source snapshot and grant | Candidate patch and source tree digest mapped to requirements | Engineering and Repository |
| Static analysis | Candidate tree and pinned analyzers | Actual tool receipts and diagnostics for that tree | Analysis and Verification |
| Code review | Candidate tree, requirements and analysis evidence | Attributed review, findings and disposition tied to candidate digest | Engineering |
| Testing | Candidate, fixtures and acceptance cases | Actual test results identifying command, environment, inputs and output evidence | Testing and Verification |
| Documentation | Candidate, approved interfaces and audience | Reviewed docs and pinned source claims | Documentation |
| Deployment | Verified candidate, target and effect authorization | Reconciled release receipt, health evidence and rollback reference | Deployment |
| Operations | Release receipt and authorized observation scope | Attributed metrics and evaluated service objectives | Observability |
| Maintenance | Observed issue, approved scope and current snapshot | Triage decision, linked maintenance assignment or evidence-backed closure | Maintenance |
| Updates | Approved change intent and active release | New plan revision and evidence trail into the affected stages | Assignments and Engineering |
| Decommissioning | Owned asset inventory, retention policy and effect grant | Verified export or approved disposal, dependency clearance and reconciled retirement receipt | Deployment and Storage |

## Integration and execution

Encode the stages using the [workflow compilation and replay contract](../1300-workflows/workflows.md). Pins include workflow definition digest, effective policy revision, revision of each repository under review, adapter versions and artifact digests. Any step that touches an external system uses a typed capability and declares its effect. Receipt verification is part of stage completion.

A step output binds its workflow revision, step ID and attempt, deterministic input digest, producer, output digest and evidence references. Persist the attempt checkpoint and artifact references together before dependents become eligible. A blocked prerequisite never authorizes a dependent action. A workflow change creates a new revision. Reuse completed evidence only when the new plan explicitly references the same inputs, policy and compatible adapter version.

Admission uses the [resource contract](../../RESOURCE_CONTRACT.md). Before queueing an expensive step, derive its minimum and preferred estimate from the declared input size and adapter capability. Acquire a lease before effect dispatch. Refuse an unsupported capability and defer a resource shortage according to the authorized deadline. Observe cancellation before external dispatch. After uncertain dispatch preserve its outcome as unknown and reconcile per [repository](../1400-repositories/repositories.md) or [deployment](../3300-deployment/deployment.md) rules. Each project owns its workflow profile and provides its deadlines, retry budgets and parallelism within policy.

## Acceptance

- **ZIP-ENG-LCY-T01.** Use a synthetic local application with a pinned base, approved scope and a fake test adapter. Feed a real passing adapter receipt and verify the successor becomes eligible. Feed a generated success summary with no receipt and verify the successor stays blocked.
- **ZIP-ENG-LCY-T02.** Interrupt the runner after committing an artifact but before dispatching the dependent step. Resume from the same workflow revision, retain one artifact and dispatch the dependent step once.
- **ZIP-ENG-LCY-T03.** Supply a denied deployment grant and a valid candidate. Record denial with no deployment call. Repeat with an authorized grant and an unknown provider reply. Reconcile before attempting any repeat effect.
- **ZIP-ENG-LCY-T04.** Change the source tree after static analysis and review. Verify the earlier evidence cannot qualify deployment of the changed tree.
