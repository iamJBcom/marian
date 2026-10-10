# M2c2 — Marian Epoch and Clock-Standard Closure

**Project:** *Marian: An Operating Calendar for Human Mars*  
**Author:** JB Bullock  
**Technical audit:** M2c2, 2026-10-08  
**Status:** **TECHNICAL CONVENTION PROPOSAL PASSED ITS SYNTHETIC TESTS; AUTHOR RATIFICATION PENDING.** The actual MY0/MY1 event is inherently uninstantiated. A high-precision JPL/SPICE founding-epoch verification is not represented as completed.

## 1. Source authority and boundaries

Highest literary source: editor-approved `Marian - Calendar v06F - 2_10_2026.docx`, by JB Bullock. Appendix A §§A.3, A.11–A.16, A.19–A.22, Appendix C §C.16, and Appendix D §§D.17–D.23, D.25–D.32 provide the present rules. No copy of the full copyrighted book is redistributed in this checkpoint.

This document provides the **narrow additional conventions necessary for reproducible MY1 instantiation and absolute-time mapping**. It does **not** change the 668/669-sol year structure, 59/100 rule, months, weeks, named minths, or astronomy anchor. It does not create a real date for the first human step.

Evidence inherited: M2a integer structural audit **PASS**; M2b NASA Mars24 analytical approximation and M2c1 independent Moshier/IAU analytical corroboration **conditional** (not SPICE kernel-backed). See prior release checkpoints for those datasets. All M2c2 tests in this package use a **synthetic epoch**, explicitly marked as hypothetical.

## 2. Recommended deterministic convention set for M3

The following is a candidate **author-ratifiable** normative contract; it has not been silently appended to the master book.

| ID | Proposed rule | Disposition |
|---|---|---|
| E01 | First **recognised human step** is a historical instant `H`, not automatically a midnight. It starts the transition interval `MY0`. | Preserves source; precise recognition awaits future authority |
| E02 | Select the first *strictly later* crossing `C` of Mars areocentric solar longitude `Ls = 15°` after `H`: `C > H`. | Explicit tie-break recommended; author approval requested |
| E03 | Select the first *strictly later* **Airy Mean Time (AMT)** midnight `E` after `C`: `E > C`. `E` starts `MY1` ordinal sol 001. | Clock choice and tie-break recommended; author approval requested |
| E04 | Interpret AMT as **mean solar**, not local true/apparent solar time; canonical planetary date uses the prime meridian; local settlements may display other clocks without changing canonical identity. | Recommended clarification |
| E05 | Adopt a **versioned reference mean-sol clock profile** for operational absolute-time conversion. Initial candidate `MARIAN-AIRY-AMT-MARS24-2025-01-07`, using NASA Mars24's published AMT phase constants and TT Julian Dates. | Candidate; must be adopted explicitly before M3 normative freeze |
| E06 | Use **TT** Julian Dates or an equivalently continuous atomic-based instant representation in the AMT phase computation; astronomical ephemeris `Ls` calculations may be in **TDB**, with explicit documented TT/TDB conversion. | Recommended interface rule |
| E07 | Once `E` is determined and signed into the epoch record, **never recompute each New Year from Ls**. For `MY1+`, apply integer date/ordinal and 668/669-sol rules from M2a. | Already canonically required |
| E08 | If an epoch-dependent numerical model changes sufficiently to change `E`, do not silently rewrite historical dates: use an explicit versioned proposal and migration policy. | Recommended governance rule |
| E09 | `MY0` denotes `[H, E)`, with its original instant preserved; the normal `MYn-MM-WW-DD` tuple and ordinal-sol `MYn-Sddd` are **not defined for MY0**. During MY0, use separately identified mission / absolute-time records. | Preserves source D.20; avoid inventing MY0 syntax |
| E10 | An ambiguous crossing or midnight due to timing/model uncertainty must be reported as **UNRESOLVED**, not silently assigned. | Recommended uncertainty fail-closed policy |
| E11 | UTC is a **presentation / exchange timescale**, not the numeric basis of Marian year arithmetic. Use valid official UTC↔TAI↔TT offsets for the target epoch; never freeze today's `TT−UTC` difference into future calculations. | Recommended technical requirement |
| E12 | A canonical Marian Civil Date identifies a **reference civil sol**, not a Mars-hour, UTC timestamp, true solar time, exact Ls, nor proper time measured at a surface site. | Preserves source scope |

## 3. Candidate AMT reference profile (not a claim of physical exactness)

NASA GISS Mars24's published AMT mean-solar phase (as of its 2025-01-07 algorithm page) is:

```
Q(JD_TT) = (JD_TT − 2451549.5) / 1.0274912517 + 44796.0 − 0.0009626
AMT_hours = 24 × fractional_part(Q)
```

For this candidate profile, **AMT midnight** is any instant where `Q` is an integer. With integer midnight index `k`, the corresponding instant is:

```
JD_TT_midnight(k) = 2451549.5
                   + 1.0274912517 × (k − 44796.0 + 0.0009626)
```

The candidate uniform mean-sol duration is `1.0274912517 TT days = 88775.24414688 SI seconds` (provided TT days are interpreted as 86400-second units). Those are *definition parameters of this proposed profile*, not observations or proof that actual Martian local sunlight remains aligned to this idealised clock indefinitely. The rounded everyday description `24 h 39 min 35 s` is **not** the numerical conversion parameter.

When `C` equals midnight precisely, strict `E > C` means **the subsequent midnight**, not the coincident instant. When `H` equals an Ls crossing precisely, strict `C > H` means **the next annual crossing**. This convention avoids interpretive variability from the source words "following"/"next"; it is an explicit proposed tie-break to ratify.

**Important design boundary:** If future maintainers select a different AMT/mean-sol model, that selection is a *new versioned clock/epoch profile*; it must not be presented as byte-for-byte identical to the profile above. The calendar's integer pattern is separate from its absolute-time bridge.

## 4. Algorithm contract

Given authenticated first-step event instant `H` (in a disclosed timescale), an **independently specified and reproducible** Ls=15° crossing model, and a named AMT clock profile:

1. Validate that `H` has authoritative provenance and uncertainty metadata.
2. Convert `H` to the crossing model's time coordinate, retaining its original representation.
3. Identify the first fully verified Ls=15° crossing `C` with `C > H`; record the ephemeris/kernels and all model parameters and hashes. **Do not** infer a crossing from a missing/short input series.
4. Convert `C` to `JD_TT` using an explicitly specified TT/TDB conversion if needed.
5. Find the smallest integer `k` for which `JD_TT_midnight(k) > C` under the frozen clock profile. Freeze `E = JD_TT_midnight(k)` as the `MY1` instant in an epoch certificate.
6. Check uncertainty bounds. If model confidence spans the first step/crossing ordering, or a midnight boundary, mark the epoch selection **AMBIGUOUS** and seek higher-precision data; never round silently.
7. From `E` onwards, for instant `T` in TT, a *candidate fixed-reference-sol* convention defines zero-based offset `d = floor((T − E) / 1.0274912517)` (where times are expressed in TT Julian days). Convert `d` with the M2a integer year/date rules. **This mapping is only normative if the candidate reference clock is ratified.**
8. From civil date to interval, compute `d = startOffset(Y) + ordinalSol − 1`; its reference start is `E + d × 1.0274912517` TT days, with end at `E + (d + 1) × 1.0274912517` TT days.
9. An event before `E` is **not** assigned a regular Marian date. If `H <= T < E`, identify the event as occurring within `MY0`, preserving its original timestamp. If `T < H`, identify it as pre-era.

`T = E` is `MY1-01-01-01`; `T = E + 1 reference sol` is `MY1-01-01-02`. `T = E + 669 reference sols` is `MY2-01-01-01`, because `MY1` leaps. **No physical sol is omitted**: the shortened-week rule changes only the civil weekday label following a 55-sol month.

### TT, TAI, UTC and TDB distinctions

TT can be represented using the conventional `TT = TAI + 32.184 seconds` realisation. Historical/future `TAI−UTC` comes from the official authority relevant to the timestamp; it is not a global fixed constant. UTC labels can contain leap seconds. SPICE ephemeris time `ET` is seconds past J2000 in TDB, not TT; conversions need a named implementation. A UTC timestamp is therefore not directly interchangeable with a TT Julian Date, a TDB epoch, or Marian ordinal-sol identity.

### MY0 is not a conventional year

The historical human step is an **instant**, so `[H,E)` may include a fractional first reference sol. There is no canonical MY0 month/week/day notation in the source and none is invented here. Separate mission-relative sol counts MAY coexist with event records, but they must carry their own mission anchor, clock convention and reference authority. `MY0-S001` MUST NOT be emitted by an implementation conforming only to the regular Marian date model.

## 5. Boundary and uncertainty cases

The checkpoint includes tests for: `H` before/at/after a crossing; crossing exactly at an AMT midnight; just before and just after midnight; `T` immediately before `E`, exactly at `E`, and exactly one sol thereafter; first-year leap boundary; shortened weekday transition; chronological inversion; invalid/unordered crossing sequences; precision with decimals; uncertainty overlapping a midnight or the step event. All times generated by these tests are **SYNTHETIC**, and use historical modelled crossing examples for convenience rather than claiming any actual human landing.

## 6. What is definitively closed vs deferred

**Closed at mathematical/proposal level:** No change to Marian integer calendar; use a mean (not apparent) Airy-0 reference; MY0 and MY1 have different origins; exact candidate AMT timing equations are publicly documented; testable event-order and midnight-order rules; machine conversion once the reference profile and MY1 epoch are agreed; no silent modern UTC offset; fail closed on uncertain epoch crossings.

**Needs author adoption before M3 normative freeze:** (a) explicitly name AMT as the canonical meaning of "Airy-0 midnight"; (b) select the fixed Mars24-derived `MARIAN-AIRY-AMT-MARS24-2025-01-07` reference sol profile, or another published versioned clock; (c) approve the strict `>` tie policy for `H→C→E`; (d) approve that MY0 has no ordinary civil tuples. These are recommendations derived from the manuscript, **not past author decisions**.

**Cannot yet be instantiated:** real `H`, `C`, and `E` timestamps, real uncertainty intervals and official epoch certificate, because there has been no historical first human step. These are *future data dependencies*, not an obstacle to publishing an explicitly conditional civil-time protocol now.

**Still scientifically desirable but not a block:** Independent high-precision SPICE ephemeris Ls crossing check at the eventual founding era (M2c1 was closed conditionally). None of the synthetic M2c2 test results should be advertised as physical ephemeris verification.

## 7. Versioning contract

The protocol should distinguish **calendar-rule version** (e.g., `marian-civil-v1.0`) from **clock model profile** and **epoch realisation ID**. A date alone does not convey all three. Before `E` exists, temporal interchange should label absolute-time operations `UNINSTANTIATED_EPOCH`, rather than returning a guessed historical date. A future epoch certificate should include status (`PROPOSED`, `RATIFIED`, `SUPERSEDED`), the signing authority, event/crossing/boundary uncertainties, model source and hashes, reference coordinate conventions, and a canonical TT timestamp with precision sufficient to distinguish adjacent reference midnights.

## 8. Source references

- Canonical book: *Marian: An Operating Calendar for Human Mars*, JB Bullock, final DOCX (2026-10-02), Appendix A/C/D. Private, retained copyright.
- NASA GISS, **Mars24 Sunclock — Algorithm and Worked Examples** (updated 2025-01-07): https://www.giss.nasa.gov/tools/mars24/help/algorithm.html
- NASA GISS, **Mars24 Sunclock — Technical Notes on Mars Solar Time** (updated 2023-05-15): https://www.giss.nasa.gov/tools/mars24/help/notes.html
- NAIF, **SPICE `lspcn`**: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/lspcn_c.html
- NAIF, **SPICE Time Required Reading**: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/time.html
- BIPM, **Time metrology / UTC**: https://www.bipm.org/en/time-metrology
- IERS, **Bulletin C metadata and UTC leap-second announcements**: https://datacenter.iers.org/productMetadata.php?id=16

