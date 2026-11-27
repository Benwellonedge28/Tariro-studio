# Tariro Studio legacy feature register

**ZIP-MIG-002 · v1.0 candidate · Owner** Architecture maintainers and the owning subsystem maintainers

The [inventory](contracts/legacy/inventory.json) records each file in the pinned legacy Git tree. The [migration map](contracts/legacy/migration-map.json) records bounded static findings against individual legacy files and the associated candidate design dispositions. Acceptance statements in that map describe tests for a successor. This pass did not execute the legacy code or qualify a successor.

## Evidence levels

| Level | Verified fact |
| --- | --- |
| Inventory | Git path, mode, byte count and blob exist at the pinned revision. |
| Static | The identified source was read and the recorded observation describes its actual contents. |
| Executed | A specific behavior was observed in an authorized isolated run and has a reproducible evidence reference. |

The static map can cover one capability in a file while additional behaviors in that file remain open. A path absent from the map has inventory evidence only. Before closing the audit, record a reviewed disposition for every independent capability and a coverage decision for each source and design file. Check deployment wiring and runtime dependencies before upgrading a finding to Executed.

## Review and use

1. Match every source path, blob and revision to the inventory. Use the exact path even if two legacy files have the same basename.
2. Separate observed behavior from proposed disposition, target behavior and acceptance. A simulated or unwired result may reveal a useful requirement, but promotion requires independent evidence.
3. Verify that the selected target already owns the capability. Resolve contract changes in the owning subsystem and its dependency registry before assigning source files.
4. For an excluded capability, record whether it is an external integration, a research topic or prohibited within core. An external proposal inherits existing authorization and effect controls.
5. Verify replacement evidence against the [migration procedure](MIGRATION.md) before retiring a legacy capability. An incomplete audit or unapproved decision remains open.

A machine consumer must preserve inventory-only records and distinguish them from audited dispositions. It must reject a migration entry with an unknown source path, mismatched blob, duplicated feature ID, missing target for a proposed core capability or an acceptance claim without evidence.
