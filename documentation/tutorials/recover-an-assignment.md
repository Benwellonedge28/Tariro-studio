# Exercise assignment recovery

Use a disposable repository and a repeatable synthetic assignment. To exercise the primary acceptance boundary, prepare 30 approved Markdown targets under the [reference profile](../examples/vimbai-documentation.md).

1. Confirm the checkpoint for unit 17 is durable and unit 18 has not started. Record the current plan, committed prefix and worker epoch.
2. Stop the harness at that boundary and restart using the same durable store. Read status before issuing a resume. Verify artifact digests and the original operation identities. An interrupted acknowledgement requires reconciliation before replay.
3. Resume under current authority. The replacement receives a fresh worker epoch and next unit 18. Verify that units 1–17 were not regenerated and that stale worker messages are denied.
4. Repeat from a clean fixture with an expired grant. Expect AwaitingApproval, no new dispatch and preserved verified work. Any required cleanup remains separately scoped.
5. Run remote response-loss faults only through the sandbox adapter. Assert observed branch and draft counts against the [acceptance fixtures](../../contracts/acceptance/documentation/end-to-end-fixtures.json), then record actual outcomes.

A shorter local recovery drill may stop after one unit in a two-unit grant. It exercises the same checkpoint boundary without satisfying the 30-file acceptance case.
