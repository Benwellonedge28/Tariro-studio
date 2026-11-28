# Executable identity restrictions

**ZIP-TERMINAL-ALLOWLIST-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/allowlist.rs`

## Boundary and inputs

Resolve an enrolled executable capability from exact adapter, approved source identity, version and integrity evidence. Match the selected executable through a trusted handle or equivalent qualified identity proof. Never resolve unrestricted caller-supplied names using ambient process search state.

## Behavior and failure handling

Check current policy and actual executable binding again at launch. A changed digest, path identity or adapter version requires fresh qualification. Enrollment describes what can be selected and confers no authority to launch. Reject unavailable identity evidence before starting the body.

## Acceptance

**ZIP-TERMINAL-ALLOWLIST-T01.** Install a synthetic same-name executable outside the approved scope and confirm it cannot be selected. Replace the approved fixture after preview and verify its stale evidence cannot authorize launch.
