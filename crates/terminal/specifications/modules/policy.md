# Effective command policy

**ZIP-TERMINAL-POLICY-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/policy.rs`

## Boundary and inputs

Intersect currently allowed program, arguments, environment, working root, process controls and network policy with the exact grant and resolved resource envelope. Verify current command digest and authorized mode before admission. Any shell or interactive mode requires explicit specific intent, capability and qualified sandbox.

## Behavior and failure handling

Fail closed on missing mandatory control, stale binding or unsupported mode. A granted read action cannot become general command or network authority. No fallback changes executable, containment, destination or permissions. Publish a scoped decision reference for the owning effect claim.

## Acceptance

**ZIP-TERMINAL-POLICY-T01.** Give a read-only command approval and request interactive execution under the same identity. Verify denial. Substitute a weaker containment profile after approval and verify no execution.
