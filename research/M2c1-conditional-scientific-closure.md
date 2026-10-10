# Marian M2c1 — Final closure determination

**Decision:** CONDITIONAL SCIENTIFIC CLOSURE — proceed to M2c2. Do not call this SPICE-verified.

## Evidence accounting

| Evidence | Status | Conclusion |
|---|---|---|
| Canonical Marian integer year/sol arithmetic | Verified in M2a | Exact 668.59 civil mean under 59 leap sols/100 years |
| NASA Mars24 analytical crossing series (M2b) | Reproduced / published-model approximation | Seasonal Ls=15° mean near 668.59 sols over an historical test range |
| Separate Swiss Ephemeris built-in Moshier/IAU crossing series (M2c1c) | Executed / analytical corroboration | 106 crossings; 105 intervals; 668.589368919-sol mean |
| NASA Mars24's published accurate-ephemeris comparison | External evidence (not independently reproduced here) | NASA estimates a maximum 0.008° Ls angular error for their Mars24 model ±100 Earth years of J2000 |
| JPL Horizons or NAIF SPICE kernel-backed crossing series | NOT EXECUTED | No high-precision independent ephemeris-grade claim |
| MY0/MY1 realised timestamps, Airy-0 clock realisation, future phase | UNRESOLVED | To M2c2 / future epoch authority; no invented dates |

## Guardrails for M3 language

Acceptable: 'The 59/100 leap-sol frequency yields an exact arithmetic mean of 668.59 sols; published NASA astronomy and an independent semi-analytical cross-check show that this closely approximates the Ls=15° recurrence over a historical comparison interval.'

Not acceptable: 'Independently SPICE-verified to sub-minute accuracy'; 'precisely 668.5900 sols at the first Martian settlement'; 'guaranteed bounded deviation indefinitely'; 'first year timestamp already determined'; 'Marian has a demonstrated accurate long-term Earth-Mars light-time conversion'.

Future work: SPICE verification using frozen M2c1b harness remains desirable if executable resources or evidence later become available, but it is **not a release blocker for an explicitly qualified technical proposal**.

Nothing in this closure changes the book or the canonical sol-based calendar.
