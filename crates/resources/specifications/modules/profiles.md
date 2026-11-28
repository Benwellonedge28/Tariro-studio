# Profile resource DTOs

**ZIP-RESOURCES-PROFILES-001 · v1.1 · Owner:** Resources maintainers. **Maturity:** D4 candidate for the scope below.

**Planned source:** `crates/resources/src/profiles.rs`

## Boundary and inputs

Consume the immutable Configuration resource view with selected profile digest, typed preferences, explicit ceilings and registered derivation markers. A valid marker can exclude the corresponding numeric default preference. It cannot remove mandatory restrictions or substitute a larger permission domain. Keep device and host observations separate from the profile.

## Behavior and failure handling

For a derivable occupancy bound, compute floor of available enforceable capacity divided by positive validated per-unit consumption across the compatible mandatory coordinates. Take the minimum across applicable capacities and policy caps. Reject absent mandatory evidence, invalid units or a model with no finite limiting coordinate. A zero compatible capacity yields zero slots. Use the derived limit as an input to fresh atomic admission, where current revisions and holds are checked again.

## Acceptance

**ZIP-RESOURCES-PROFILES-T01.** Keep one profile digest over two hardware snapshots with different qualified capacity and show the derived slot count changes. Apply a stricter cap and a known zero sample. Test missing evidence and an explicit override competing with a derivation marker.
