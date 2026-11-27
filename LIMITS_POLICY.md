# Operational limits policy

**ZIP-LIM-001 · v1.0 · Owner:** Resource and security maintainers. **Maturity:** D4 candidate.

For every limiting dimension classify the value as invariant, protocol ceiling, measured capacity, administrative policy, profile default, assignment agreement, or adaptive budget. Operational call sites must receive a validated budget or charge a lease. A literal used for arithmetic identity or a prescribed representation is permissible. A literal that restricts file size, count, context length, time, retries, worker count or retention requires a registered source and cannot be embedded at the enforcing call site.

| Category | Source | Enforcement |
| --- | --- | --- |
| Invariant | Mathematics, representation, cryptographic algorithm or constitutional requirement | Fixed and documented with provenance |
| Protocol ceiling | Negotiated or versioned external contract | Bound adapter, report incompatibility if local budget is insufficient |
| Profile default | Typed configuration default | Starting preference, re-evaluate against measured capacity |
| Administrative cap / quota | System, organization, workspace or assignment policy | Intersect applicable ceilings using compatible units |
| Exact constraint | Approved assignment format | Reject mismatch; do not silently shrink the contract |
| Adaptive budget | Hardware and sandbox observations, current accounting | Tighten capacity, apply authorized service tradeoffs only |

No default implies unlimited. Missing, unknown or stale required limits cause a typed denial unless policy defines an independently enforceable fallback. Exact 30-file acceptance remains scoped to the reference Vimbai grant. In existing designs, numeric operational examples serve as candidate profile values unless explicitly classified as inherent or assignment-bound. Replace them with registered keys in the owning design before D5.

Migration review records each source mention, classification, new key, caller, unit and test. CI scans literals as a review aid and requires a rationale for exceptions. Test the same runtime build under at least two different budgets and verify behavior changes without recompilation.
