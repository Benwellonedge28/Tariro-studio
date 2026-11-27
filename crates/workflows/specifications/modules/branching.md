# Durable deterministic branch decisions

**ZIP-WORKFLOWS-BRANCHING-001 · v1.1 candidate · Owner** Workflows maintainers

**Planned source** `crates/workflows/src/branching.rs`

After dependencies settle, evaluate the guard using immutable inputs and their ordered digest. A missing guard means true. Commit a decision record keyed by run, plan and node, together with the Runnable or Skipped disposition. Record guard digest, input digest and compiler version. False is a durable Skipped outcome with no capability claim. A guard error blocks this node; it cannot substitute for false. Later eligibility and optional artifact rules decide whether successors may run.

Replay the stored decision only when exact compiled guard and immutable input identities match. Mismatch is StaleCheckpoint and requires revalidation or a new plan revision. Complementary branches can be expressed by guarded steps over the same inputs. If a plan requires exclusive choice, validate that its branch declaration cannot select multiple outputs before accepting any effect. Downstream joins require the declared typed bindings and predecessor policy.

**ZIP-WORKFLOWS-BRANCHING-T01.** Replay a stored branch from the same inputs. Vary an input digest and verify the prior decision does not authorize a step.
