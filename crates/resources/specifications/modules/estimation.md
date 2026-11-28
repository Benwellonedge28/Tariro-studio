# Conservative demand calculation

**ZIP-RESOURCES-ESTIMATION-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/estimation.rs`

## Boundary and inputs

Accept a reviewed workload descriptor, qualified adapter measurements, immutable configuration/policy references and required typed demand coordinates. Return a minimum and preferred DemandVector when policy allows variants, with the assumptions and revisions behind each rationalized estimate. Calculate checked worst-case component demand and combine only simultaneously resident portions in compatible units.

## Behavior and failure handling

Include applicable model weights, working memory and host-side overhead before admission. Reject unsupported mandatory dimensions or unverifiable measurement inputs. A measured estimate remains distinct from verified allocatable capacity, and a zero is allowed only with evidence for that exact coordinate. If measured usage exceeds an estimate, reporting pressure can stop or constrain new work. Never enlarge a current lease or forgive previously counted usage. See [resources](../../../../RESOURCE_CONTRACT.md).

## Acceptance

**ZIP-RESOURCES-ESTIMATION-T01.** Estimate two contexts from one qualified model input and verify each bounded demand differs appropriately. Inject overflow, a missing metric and observed demand above the estimate. Preserve recorded assumptions and return a typed failure or pressure outcome without an unbounded fallback.
