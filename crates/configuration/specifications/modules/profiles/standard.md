# Standard profile rules

**ZIP-CONFIGURATION-PROFILES-STANDARD-001 · v1.2 · Owner:** Configuration maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/configuration/src/profiles/standard.rs`

## Boundary and inputs

Load the registered [Standard manifest](../../../../../configurations/profiles/standard.toml). It selects local-only best-fit inference and derives generation-model and agent bounds from admission. Resolve finite per-unit model and agent demand, required quality and all observed capacities through the Resources owner. Configuration publishes explicit caps or derivation markers and does not measure hardware. Register the actual installed definition through [profile dispatch](mod.md).

## Behavior and failure handling

Use only compatible occupancy coordinates when deriving concurrency. The smallest verified occupancy ratio across required pools and the strictest applicable configured cap bound the derived result. Do not inherit the numeric baseline slot preferences when a valid derivation marker applies. A workload must still be admitted atomically under current capacity and policy. Unknown mandatory input preserves an unavailable state. This contract supplies no universal RAM threshold or new concurrency constant.

## Acceptance

**ZIP-CONFIGURATION-PROFILES-STANDARD-T01.** Use one standard profile definition across two synthetic hosts whose measured available RAM differs. Verify the finite slot bound changes when RAM is limiting, a tighter explicit cap still wins, and unknown RAM blocks the hard demand.
