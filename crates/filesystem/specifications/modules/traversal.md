# Bounded deterministic tree scan

**ZIP-FILESYSTEM-TRAVERSAL-001 · v1.1 · Owner:** Filesystem maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/filesystem/src/traversal.rs`

## Boundary and inputs

Traverse a scoped pinned directory hierarchy using deterministic relative path order from qualified entries. Admit depth, observations, items, bytes and elapsed work before progressing. Return a bounded page with coverage state and a cursor bound to the scope and generation.

## Behavior and failure handling

Never follow forbidden entries or use unknown identity to widen a scan. Incomplete, denied or changed traversal produces explicit noncomplete status and safe evidence. Cursor replay rechecks grant and root revision. On overflow or nonreplayable cursor conditions resume only from a qualified new scan.

## Acceptance

**ZIP-FILESYSTEM-TRAVERSAL-T01.** Exhaust an admitted item budget midway and verify the result remains partial. Change the root generation and confirm the prior cursor cannot label the remaining output complete.
