# Deterministic degradation selection

**ZIP-RESOURCES-OPTIMIZATION-ADAPTIVE-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/optimization/adaptive.rs`

## Boundary and inputs

Take an affected pool revision, effective policy and a bounded set of approved alternatives with measured demand, quality score and stable identity. Exclude candidates below the declared floor, with unproven requirements or which change locality, disclosure or spend scope without separate authority. Use the owner's stable rank for remaining candidates and break equal ranks with canonical identity.

## Behavior and failure handling

Return an advisory alternative with demand, assumptions and decision evidence or typed unavailability. Recheck live policy and available capacity before any fresh allocation. An in-flight workload may change only through its owning transition. Release the original lease through verified cleanup or reserve any approved overlap before starting the successor. No candidate extends the existing lease.

## Acceptance

**ZIP-RESOURCES-OPTIMIZATION-ADAPTIVE-T01.** Test equivalent candidate permutations and stable ties, all candidates below the floor, and a once-fitting candidate whose observations become stale. The first result stays deterministic. The latter cases deny or re-estimate without changing active holds.
