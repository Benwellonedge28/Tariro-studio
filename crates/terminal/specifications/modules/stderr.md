# Redacted standard error

**ZIP-TERMINAL-STDERR-001 · v1.1 · Owner:** Terminal maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/terminal/src/stderr.rs`

## Boundary and inputs

Capture ordered stderr bytes using the shared [combined cap](output_limits.md). Reserve before buffering or persistence, and record provenance and completeness separately. When surfacing diagnostics, apply the scoped safe output projection without retaining classified raw content.

## Behavior and failure handling

Report actual stderr capture or truncation without assigning process success. A benign diagnostic line cannot erase nonzero exit, and empty stderr never proves success. When the cap is reached use the shared supervisor handling and preserve exact output-limit evidence.

## Acceptance

**ZIP-TERMINAL-STDERR-T01.** Flood stderr with stdout idle and verify exhaustion at the same cap. Run a benign nonzero exit with empty diagnostics and confirm there is still an exit failure receipt.
