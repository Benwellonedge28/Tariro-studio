# Researcher role

**ZIP-AGENTS-ROLES-RESEARCHER-001 · v1.1 · Owner:** Agents maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/agents/src/roles/researcher.rs`

## Boundary and inputs

Collect only scoped sources available through approved readers. Bind source identity, exact relevant version or retrieval context and evidence reference to each observation. Distinguish gathered facts, quoted material, hypotheses and unavailable sources. External retrieval requires authorized egress.

## Behavior and failure handling

Do not cite a source as observed unless retrieval and relevant inspection succeeded. An unsupported claim or conflicting evidence remains explicitly uncertain. Keep private material inside approved data scope, prefer bounded evidence extracts and leave external sharing to its owning authorization.

## Acceptance

**ZIP-AGENTS-ROLES-RESEARCHER-T01.** Use an unavailable source and a retrieved source with different findings. Verify only the retrieved material supports an observed claim and no citation is fabricated for the unavailable one.
