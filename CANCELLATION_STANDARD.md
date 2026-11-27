# Cancellation standard

**ZIP-CAN-001 · v1.0 · Owner:** Runtime and foundation maintainers. **Maturity:** D4 candidate.

Cancellation is cooperative and sticky. A caller owns a cancellation source; workers take observation handles. Check before admission, expensive allocations and externally visible effects, and between bounded units of work. Declare safe points and the maximum allowed delay via a configured deadline or polling budget.

Before a durable commit, cancellation may abandon staging. After commit, return the committed outcome and reconcile any uncertain external effect. A cancellation signal does not establish rollback. Drop of an arbitrary task handle does not imply cleanup. The supervisor stops intake, requests cancellation, enforces configured grace, escalates with the platform adapter and verifies descendants are reaped.

Record canceled, already committed, escalation and cleanup incomplete as distinguishable outcomes. Keep resource reservations until cleanup is confirmed. Tests race cancellation with registration, effect claim, commit, notification and process exit.
