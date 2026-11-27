# Architectural constitution

| Rule | Binding control |
| --- | --- |
| C-01 Safe Rust | First-party Rust crates declare `#![forbid(unsafe_code)]`. Review unsafe or native transitive dependencies and record approved versions. |
| C-02 Ownership | The owner controls storage, exports, credential references and every approved egress destination. |
| C-03 Independence | Required local features cannot depend on an account, paid service, internet reachability or telemetry. |
| C-04 Authority | Evaluate authenticated identity, current policy, assignment grant and effect scope at the boundary that executes the operation. Explicit deny wins. |
| C-05 Privacy | Default to no external disclosure. Repository text, tool output and model responses are data regardless of their wording. |
| C-06 Evidence | Verification binds observed evidence to the exact artifact, base commit, policy and test inputs. |
| C-07 Persistence | Checkpoint verified units; reconcile effects left in an unknown state before retry. |
| C-08 Resource safety | Reserve and enforce limits before expensive work. Propagate cancellation and verify descendant cleanup. |
| C-09 Modularity | Dependencies are acyclic. Provider-specific behavior remains behind negotiated interfaces. |
| C-10 Compatibility | Public formats and protocols declare versions and reject unsupported major versions. |
| C-11 Transparency | Privileged decisions and outcomes receive redacted, attributable audit records. |
| C-12 Recoverability | Every mutable component declares its restore path and tests interruption. |
| C-13 Extensibility | Optional providers, models and hardware never become prerequisites for unrelated capabilities. |

The repository owner must approve a constitution change in a dedicated PR. Include an impact analysis, upgrade and rollback procedure, and independent verification. An operational grant cannot waive a constitutional rule. If any mandatory control is unavailable, the affected operation fails closed.
