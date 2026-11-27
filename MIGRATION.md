# Tariro Studio migration

**ZIP-MIG-001 · v1.1 candidate · Owner** Architecture maintainers

The preserved Tariro Studio tree is [legacy revision `f085e513`](https://github.com/Benwellonedge28/Zipporah/tree/f085e513c740416bd33d26758ead6d0ce89b3bbc). Sections 88 and 89 of the [master design](ZIPPORAH-STUDIO-DESIGN.md) govern migration. The branch was verified at that revision. No archival tag was listed at the time of verification, so the archive-tag milestone remains open.

## Evidence and scope

Use the pinned [legacy file inventory](contracts/legacy/inventory.json) for provenance and the [feature register](LEGACY_FEATURE_REGISTER.md) for review and acceptance. Read source as data. A file name, comment, type signature, generated report or mock result alone cannot establish working behavior. Any future execution of legacy code requires an authorized isolated environment and a test plan with synthetic inputs.

Inventory coverage and feature coverage are independent. For each source or design file, close the audit by mapping its behaviors to feature records or recording why it has no independent capability. A feature spanning several files needs evidence from its actual entry point, dependencies and fixtures before it can be qualified as working. Preserve reported results with the exact tree commit and source blob.

## Classification and handover

Use one of the master design's classifications per audited capability.

| Classification | Required disposition |
| --- | --- |
| Preserve | State the reusable behavior or requirement and name its current owner and acceptance test. |
| Rewrite | Define Safe Rust behavior, dependency ports and compatibility requirements. |
| Consolidate | Identify the surviving owner and prove the combined design covers each required behavior. |
| Redesign | Record the architectural incompatibility and qualify a replacement contract. |
| Experimental | Define a research question, evaluation fixture and gate before any product commitment. |
| Simulated | Identify the placeholder boundary and the evidence required to demonstrate real behavior. |
| Retire | Record the scope decision and any data retention or export obligations. |
| Blocked | Record the missing evidence or approval and the condition that resolves it. |

Each mapped capability changes disposition only after a review identifies the previous disposition and explains the new evidence. Moving a feature from an experimental or simulated disposition into the product requires an approved target design and measured acceptance.

## Activation and recovery

Before migrating persistent state, record the source schema and revision and export a consistent snapshot. Validate the export offline and import into a separate destination. Compare record counts by type, identity and reference integrity, normalized summaries and digests for immutable payloads. Any mismatch stops activation and preserves the source snapshot. Activate only after target acceptance, grant checks and a verified restore rehearsal. Record the last known good configuration and snapshot. If rollback is required, stop writers, preserve new records for reconciliation and restore the approved checkpoint. Resolve uncertain external actions against recorded receipts before repeating an action.

Safe Rust owns first-party execution. Use approved embedded storage and indexes through their interfaces. Legacy service coupling, hosted inference and containers require explicit adapter review. External effects use the existing [repository reconciliation rules](specifications/1400-repositories/repositories.md) and the [authorization contract](specifications/2400-governance/governance.md).
