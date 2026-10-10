# Marian Protocol v1.0 — Author-Ratified Normative Specification

**Full work:** *Marian: An Operating Calendar for Human Mars*  
**Author:** JB Bullock  
**Document ID:** `marian-protocol-v1.0`  
**Ratified:** 8 October 2026; **external publication:** not yet performed  
**Status:** **AUTHOR-RATIFIED / NORMATIVELY FROZEN v1.0 — NOT YET PUBLICLY PUBLISHED OR INSTITUTIONALLY ADOPTED**  
**Subject:** Marian regular civil calendar, optional clock/epoch profile, and implementer conformance  
**Master source:** Editor-approved `Marian - Calendar v06F - 2_10_2026.docx`, Appendices A–D  
**Ratification basis:** The author explicitly approved decisions D01–D10 without amendment in this project conversation on 8 October 2026; see `../author/AUTHOR-RATIFICATION.md`. The source-locked civil mathematics is unchanged. Machine grammar (D05), error vocabulary (D07), JSON profile (D08), clock conventions (D01–D04 and D06), and scoped technical licenses (D09–D10) are adopted as stated here.

**Evidence boundary:** M2a integer audit PASS; M2b/M2c1 astronomical evidence CONDITIONALLY CORROBORATED (no independent SPICE run); M2c2 synthetic epoch-model tests PASS; no real future MY1 epoch certificate exists. The historical first step and absolute calendar epoch remain unknown and are not supplied by ratification.

## 1. Purpose and conformance vocabulary

Marian defines civil dates for possible permanent human habitation of Mars. Its function is to organise successive Martian mean solar days into regular, mechanically computable civil units. It is not a new astronomical ephemeris, a clock for every location, an authority over future human customs, or a continuation of Earth's Gregorian weekdays.

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** express compliance requirements. Unless stated otherwise, numerical formulae use exact integer arithmetic, counting starts at 1 for human-facing period identities, and intervals are half-open `[start,end)` when expressed as absolute instants. **[M3c-RATIFIED]**

There are two distinct implementable interfaces:

- **CORE**: regular civil-year mathematics and canonical identity, operable now for `MY1` and all later years, without an actual epoch or ephemeris.
- **EPOCH-ADAPTER**: a parameterised map between core sol offsets and absolute instants that requires a named and frozen clock profile plus a ratified future MY1 epoch certificate.

The canonical CORE wire identifier is `marian-civil-v1.0`. The AMT clock model uses independent profile identifier `MARIAN-AIRY-AMT-MARS24-2025-01-07-v1`; a future epoch realisation uses its own certificate identifier.

An implementation MUST NOT imply that satisfying CORE proves any ephemeris, historical-epoch, astronomical-accuracy, or physical-rotational claim. Conversely, lack of a historical MY1 timestamp does not invalidate mathematical CORE computations.

## 2. Applicability and exclusions [SOURCE-LOCKED]

A regular Marian year is a Mars-centred **civil** time division. Core date identity addresses an entire canonical civil sol; it does **not** encode a time within the sol, a longitude, local time zone, solar longitude `Ls`, Mars Sol Date (MSD), UTC date, mission sol, Earth–Mars light-time, or planetary position.

Marian does not specify sub-sol hours/minutes/seconds, local time zones, daylight adjustments, work/rest schedules, religious practice, holidays, school terms, fiscal use, ages, birthday conventions, or settlement governance. An application MAY attach those separately but MUST NOT alter the meaning of a Marian structural identifier when doing so.

## 3. Physical succession, canonical sol, and clock separation [SOURCE-LOCKED]

The base civil unit is a Martian **sol**, grounded in the Martian mean solar day. Every regular Marian sol has exactly one civil date. Sol succession and continuous elapsed counting are never interrupted, omitted, or repeated by a shortened civil week. Omission of the civil weekday label `D7` at specified month ends does not remove a physical sol or modify a circadian rhythm.

An actual civil-boundary instant is an additional horological definition; it is **not** inferred by treating the rounded statement “24 hours 39 minutes 35 seconds” as an exact duration. Section 15 describes the **author-ratified** mean-sol model for absolute conversion.

## 4. Regular civil-year structure [SOURCE-LOCKED]

A normal year is identified by positive integer `Y` (rendered `MY1`, `MY2`, …). A common year contains exactly **668** consecutive sols; a leap year contains **669**.

Each regular year has exactly **12 months**, **24 minths**, **6 Sixths**, **4 quarters**, and **96 nominal civil-week slots**. Quarters and Sixths are overlapping partitions, not an exclusive hierarchy. The 96 slots are **not** 96 complete seven-sol intervals: some terminal civil weeks contain only six occupied weekday positions.

The following functions are normative, with zero-based array indexes forbidden as a substitute for displayed identifiers:

```
isLeapYear(Y):
    REQUIRE Y is an integer and Y >= 1
    IF Y mod 100 == 0: RETURN false
    IF Y mod 2 == 1: RETURN true
    IF Y mod 10 == 0: RETURN true
    RETURN false

yearLength(Y) = 669 IF isLeapYear(Y) ELSE 668
```

The century exception takes precedence. `MY1` is leap; `MY2` common; `MY10` leap; `MY100` common; `MY101` leap. Exactly **59** of every 100 regular years are leap years, repeated for subsequent 100-year blocks. Their combined length is **66,859 sols**, and the civil mean is exactly **668.590000 sols**. These are integer-calendar facts, not independently established astronomical quantities.

## 5. Month lengths [SOURCE-LOCKED]

A common year follows `56–56–55 | 56–56–55 | 56–56–55 | 56–56–55`, giving 668 sols. The leap year is the same except that **Month 12** contains 56 rather than 55 sols. Months are numbered **01–12**. All regular months start at civil weekday position D1.

| Month | Common sols | Leap sols | Minths | Quarter | Sixth |
|---|---:|---:|---|---|---|
| 01 | 56 | 56 | 01–02 | Q1 | S1 |
| 02 | 56 | 56 | 03–04 | Q1 | S1 |
| 03 | 55 | 55 | 05–06 | Q1 | S2 |
| 04 | 56 | 56 | 07–08 | Q2 | S2 |
| 05 | 56 | 56 | 09–10 | Q2 | S3 |
| 06 | 55 | 55 | 11–12 | Q2 | S3 |
| 07 | 56 | 56 | 13–14 | Q3 | S4 |
| 08 | 56 | 56 | 15–16 | Q3 | S4 |
| 09 | 55 | 55 | 17–18 | Q3 | S5 |
| 10 | 56 | 56 | 19–20 | Q4 | S5 |
| 11 | 56 | 56 | 21–22 | Q4 | S6 |
| 12 | 55 | 56 | 23–24 | Q4 | S6 |

```
monthLength(Y,M):
    REQUIRE Y >= 1 and 1 <= M <= 12, with integer inputs
    IF M in {3,6,9}: RETURN 55
    IF M == 12 AND NOT isLeapYear(Y): RETURN 55
    RETURN 56
```

## 6. Minths [SOURCE-LOCKED]

Each month contains exactly two **minths**. The first is 28 sols; the second is 28 sols in a 56-sol month or 27 sols in a 55-sol month. Number minths **01–24** in ascending chronological order: Month `M` contains minths `2M−1` and `2M`.

In common years, minths **06, 12, 18, 24** contain 27 sols; in leap years, only **06, 12, 18** do. Every minth starts at weekday D1. `A–X` is recommended compact shorthand for 01–24 and is not a canonical machine substitute. Optional proper names, including an alternative terminal leap-minth name, MUST NOT alter its canonical number.

```
minthLength(Y,N):
    REQUIRE Y >= 1 and 1 <= N <= 24, integers
    M = floor((N+1)/2)
    RETURN 28 IF N is odd ELSE monthLength(Y,M) - 28
```

## 7. Weekday recurrence and shortened weeks [SOURCE-LOCKED]

Within each month, weeks are numbered **01–08** and days within each week **01–07**, when occupied. The recommended weekday-name sequence is **Monsol, Tuesol, Wedsol, Thursol, Frisol, Satsol, Sunsol**. The canonical identifiers remain D1–D7.

A 56-sol month has eight complete D1–D7 weeks. A 55-sol month has seven complete weeks and Week 08 D1–D6 only. It ends on `W08-D06` (Satsol), and the **next physical sol** starts the next month as `W01-D01` (Monsol); **no** D7 label is placed between them. Date-to-weekday recurrence is fixed wherever the date exists, but a continuous seven-position civil weekday sequence is deliberately **not** preserved.

The common year contains 92 complete seven-position weeks plus 4 six-position terminal weeks. The leap year contains 93 complete weeks plus 3 six-position terminal weeks. The nominal week-slot count is always 96.

## 8. Quarters and Sixths [SOURCE-LOCKED]

Quarter `Q = floor((M−1)/3)+1`, numbered `Q1`–`Q4`, groups three months. A common year has four 167-sol quarters; leap Q4 contains 168 sols, with Q1–Q3 unchanged. The source's reference quarter names are **Primiv, Secondiv, Tertiv, Quartiv**, separate from machine identities.

Sixth `S = floor((M−1)/2)+1`, numbered `S1`–`S6`, groups two months. Common-year lengths are `112,111,111,112,111,111` sols, while leap S6 contains 112. The source's reference Sixth names are **Primus, Secundus, Tertius, Quartus, Quintus, Sextus**. Sixth boundaries need not coincide with quarter boundaries. Names MAY be localised without redefining these mathematical divisions.

## 9. Canonical civil date [SOURCE-LOCKED; serialization D05 RATIFIED]

The primary date is the four-component tuple `(Y,M,W,D)` (year, month, week within month, weekday within week). Canonical printed interchange form is `MY<year>-MM-WW-DD`. Month, week and weekday use **two decimal digits**. The year is a positive decimal integer with variable digit count.

**Normative canonical grammar (D05 ratified):**

```
CIVIL  = "MY" POSINT "-" TWODIGIT "-" TWODIGIT "-" TWODIGIT
ORDINAL = "MY" POSINT "-S" DIGIT DIGIT DIGIT
POSINT = NONZERO *DIGIT
TWODIGIT = DIGIT DIGIT
DIGIT = ASCII "0" … "9"
NONZERO = ASCII "1" … "9"
```

The canonical profile **disallows padded years** (`MY042`), leading/trailing whitespace, sign prefixes, lowercase `my`, unpadded subdivision fields and non-ASCII digits in canonical interchange. Lenient human-input parsers MAY exist but MUST emit the exact canonical representation on interchange. Structural invalidity is distinct from syntactic invalidity. The manuscript fixes two-digit subdivisions; this explicit padded-year restriction is an author-ratified v1.0 machine-interchange convention (D05), not an original manuscript requirement.

## 10. Valid dates [SOURCE-LOCKED]

Inputs must be integers, and `Y >= 1`, `1 <= M <= 12`, `1 <= W <= 8`, `1 <= D <= 7`. Define month position `P = 7(W−1)+D` (one-based). The date exists **iff** `P <= monthLength(Y,M)`.

Thus `MY2-03-08-06` exists; `MY2-03-08-07` does not. `W08-D07` is always absent in M03, M06 and M09, and absent in M12 for common years only. `MY1-12-08-07` exists because MY1 is leap. Implementations MUST reject an impossible date, not normalise or roll it into another date.

## 11. Ordinal-sol identity [SOURCE-LOCKED]

An alternative representation addresses the **one-based sol ordinal within the same regular year**: `MY<year>-SNNN`, using three ASCII digits from `S001` to `S668` or `S669` as appropriate. This is a year-local ordinal, **not Mars Sol Date (MSD)**; conforming software MUST NOT label it MSD.

```
civilToOrdinal(Y,M,W,D):
    REQUIRE valid civil date
    P = 7*(W-1)+D
    RETURN sum(monthLength(Y,j) for j=1..M-1) + P

ordinalToCivil(Y,R):
    REQUIRE Y >= 1 and 1 <= R <= yearLength(Y)
    remaining = R
    FOR M=1..12:
        IF remaining <= monthLength(Y,M):
            W = floor((remaining-1)/7)+1
            D = ((remaining-1) mod 7)+1
            RETURN (Y,M,W,D)
        remaining = remaining - monthLength(Y,M)
```

Example: `MY42-08-03-05` is `MY42-S409`. Both address one and the same civil sol.

## 12. Zero-based absolute civil-sol offset [SOURCE-LOCKED; exact inverse algorithm RATIFIED]

Define `L(N)` as the count of leaps in MY1 through MY N, inclusive, and `B(Y)` as the count before MY Y:

```
L(N) = floor((N+1)/2) + floor(N/10) - floor(N/100), N>=0
B(Y) = floor(Y/2) + floor((Y-1)/10) - floor((Y-1)/100), Y>=1
startOffset(Y) = 668*(Y-1) + B(Y)
offset(Y,M,W,D) = startOffset(Y) + civilToOrdinal(Y,M,W,D) - 1
```

The first civil sol of MY1 has `offset = 0`; the next has `offset = 1`. A zero-based offset does **not** denote seconds. Its value increases by one at every reference civil-sol boundary, including when a six-position terminal week restarts at D1. Calendar arithmetic MUST use exact integer operations, without converting an integer sol offset into a Gregorian day count.

**Exact inverse (normative algorithm)**: given a nonnegative integer `o`, find the unique positive integer `Y` with `startOffset(Y) <= o < startOffset(Y+1)` by integer binary search (optionally first bracket with exponentially increasing bounds); let `R = o−startOffset(Y)+1`; return `ordinalToCivil(Y,R)`. The manuscript suggests an approximate `o/668.59` year estimate followed by exact boundary correction; the normative inverse avoids floating-point rounding/overflow for large offsets. Both are correct **only** if final results are tested against the exact integer boundaries.

## 13. Derived date fields [SOURCE-LOCKED]

For a validated date, define `P = 7(W−1)+D`:

```
minth = 2*M-1 IF P<=28 ELSE 2*M
quarter = floor((M-1)/3)+1
sixth = floor((M-1)/2)+1
nominalWeekOfYear = 8*(M-1)+W
```

The last value ranges from 1 to 96 but MUST NOT be used as an uninterrupted elapsed-seven-sol week index. There is no global Marian modulo-seven weekday counter in this protocol.

## 14. MY0, founding event, and MY1 [SOURCE-LOCKED; tie policy D03 RATIFIED]

`MY0` begins at the future **recognised first human step** onto the Martian surface. It is a **transitional historical interval**, not a 668- or 669-sol normal year. `MY1` begins at the first canonical Airy-0 midnight after Mars next crosses `Ls = 15°`. From `MY1` onward only the integer rules in §§4–13 determine regular year boundaries. Subsequent New Years MUST NOT be reset from annual ephemerides.

Let `H` be the verified first-step instant, `C` the selected Ls crossing, and `E` the beginning of `MY1`.

**Normative tie resolution (D03):** choose the first Ls=15° crossing `C` **strictly later than** `H` (`C>H`), then the first Airy Mean Time midnight `E` **strictly later than** `C` (`E>C`). Consequently an exact H=C tie selects the *following year's crossing*; an exact crossing-midnight tie selects the *next midnight*. This explicit tie-break resolves an ambiguity left open by the manuscript words “next” and “following”; the author ratified it for v1.0.

`MY0` is `[H,E)`. **Normative MY0 representation (D04):** no ordinary `MY0-..` date string or `MY0-S...` ordinal is defined. Use the original authenticated mission/event timestamp until the regular epoch. Regular CORE converters MUST reject `Y=0` and negative offsets. A historical event before `H` is pre-era; an event in `[H,E)` belongs to the transitional interval without a regular date tuple.

As of the author-ratified v1.0 freeze, **H, C, and E are unknown**, and no historical `MY1` Gregorian/UTC/TT timestamp exists. A protocol may be published parametrically without fabricating these.

## 15. Clock-standard reference and future epoch adapter [D01–D04, D06 RATIFIED]

**Source-locked definition:** the canonical planetary rollover is **midnight at Airy-0**, distinct from the instantaneous Ls=15° crossing. Marian does not mandate other settlements' time zones or clock displays.

**Normative convention (D01):** Airy-0 midnight means **Airy Mean Time (AMT) midnight**, not apparent/true solar midnight. The author-ratified v1.0 reference clock profile (D02) is `MARIAN-AIRY-AMT-MARS24-2025-01-07-v1` and implements the published NASA Mars24 affine mean-time phase:

```
Q(JD_TT) = (JD_TT - 2451549.5) / 1.0274912517 + 44796.0 - 0.0009626
AMT_HOURS = 24 * fractionalPart(Q)
midnight occurs when Q is an integer
JD_TT_midnight(k) = 2451549.5 + (k - 44796.0 + 0.0009626)*1.0274912517
```

The reference mean-sol duration is **1.0274912517 TT-based 86,400-second days = 88,775.24414688 SI seconds** within this defined computational profile. Its constants define a reproducible *mean-sol reference clock*, not observed exact rotation, proper time at a landing site, or unlimited astronomical precision. Implementations that compare instants near boundaries SHOULD use exact decimal/rational representations and declared uncertainty; binary floats may not be used as authoritative tie-break evidence.

**Time-scale separation:** identify input/output scales explicitly. `TT` is the recommended continuous computation coordinate for the defined AMT reference model; SPICE ephemeris calculations may use `TDB` and REQUIRE documented TT/TDB transformation for an actual epoch certificate. UTC is an exchange/display scale, with applicable epoch-specific UTC–TAI conversion rules. `TT=TAI+32.184 seconds` in the corresponding conventional time-scale realisation. Never freeze present-day leap-second assumptions for a future epoch; do not silently interpret a UTC string as JD_TT.

Given an authenticated real E and a ratified named reference-clock profile, a conforming EPOCH-ADAPTER MAY calculate:

```
T >= E (both in TT JD)
d = floor((T - E) / 1.0274912517)
regularDate = offsetToCivil(d)
startTT(regularDate) = E + offset(regularDate)*1.0274912517
endTT(regularDate)   = startTT + 1.0274912517
```

These expressions are normative **for the identified reference clock profile**, but cannot be evaluated against real events until an authenticated, ratified future epoch certificate supplies E. An uninstantiated implementation MUST report `UNINSTANTIATED_EPOCH` for requests requiring an actual absolute timestamp, not invent a date or apply the Mars24 test epoch as the real founding event.

## 16. Solar longitude and astronomical evidence [SOURCE-LOCKED with qualified evidence]

Marian's astronomical **annual reference** is areocentric solar longitude `Ls = 15°`, which is a **seasonal longitude**, not an inertially fixed heliocentric azimuth. The ordinary intercalation mean **668.590000 sols** is intended to track the recurrence near a founding era. It is not a claim that every actual Ls crossing is separated by exactly 668.59 sols, or that date alone supplies precise seasonal angle.

The M2b Mars24 calculation and M2c1 independently implemented Moshier/IAU calculation corroborate a ~668.589-sol mean in their *historical test window*. That evidence is **analytical and conditional**, not an executed independent SPICE-kernel comparison. Any claimed physical phase error MUST specify model, timescale, interval, and initial anchoring offset; a mathematical drift relative to constant 668.59 is not a verified long-term ephemeris drift.

No automatic future correction is defined by v1.0. Any future maintenance leap rule, astronomical model replacement or epoch-redefinition must use explicit versioned governance and conformance, and MUST NOT silently change existing date identities.

## 17. Canonical parsing, validation errors and machine interchange [D05, D07, D08 RATIFIED]

A strict canonical parser MUST: (i) distinguish malformed string syntax from nonexistent but well-formed dates, (ii) validate the whole `(Y,M,W,D)` or `(Y,R)` tuple, (iii) reject invalid positions rather than normalise, (iv) emit ASCII strings exactly as specified, and (v) round-trip to the same canonical string.

Normative machine error identifiers (D07; human-readable messages remain nonnormative):

| Error ID | Meaning |
|---|---|
| `SYNTAX_ERROR` | String fails canonical grammar |
| `INVALID_DATE` | Well-formed tuple uses a nonexistent month/week/day/ordinal |
| `UNSUPPORTED_YEAR` | Regular date requested for MY0 or pre-MY1 |
| `NEGATIVE_OFFSET` | Negative offset relative to MY1 requested from CORE |
| `UNINSTANTIATED_EPOCH` | Absolute-time mapping requested without authenticated future E |
| `UNRATIFIED_CLOCK_PROFILE` | Clock mapping attempts an unapproved reference model |
| `UNCERTAIN_BOUNDARY` | Event/model uncertainties prevent determining an exact crossing or midnight boundary |
| `UNSUPPORTED_PROFILE` | Clock/epoch/rule version cannot be interpreted |

For machine interchange, the accompanying **v1.0 JSON schema** encodes `year` as an unpadded decimal **string**, preserving arbitrarily large year identifiers without relying on JavaScript's limited safe numeric integer range. Month/week/day are JSON integer fields; their combination still requires algorithmic validity checking. A JSON Schema alone is insufficient to apply year-dependent leap rules.

## 18. Conformance profiles and proof obligations

**CORE-DATE** conformance requires: leap predicate; year/month/minth lengths; 12/24/6/4 annual partitions; valid/invalid civil coordinates; absent terminal Sunsol handling; canonical date and ordinal conversions; exact civil-sol offsets in both directions; no skipped physical sols; stable localised identity. The conformance suite MUST test all dates in at least one complete 100-year cycle and representative century transitions; see `M3a-conformance.md`.

**EPOCH-ADAPTER** conformance additionally requires: an explicit clock-profile ID; evidence-provenance and uncertainty model; authenticated and ratified `H,C,E`; reversible interval mapping; correct time-scale conversion; and fail-closed errors for unknown epoch/boundaries. M2c2's *synthetic* exercises are a reference test of the subsequently ratified procedure only. They do not confer real-epoch conformance.

An implementation that passes the released CORE-DATE suite MAY state **“conforms to the Marian Protocol v1.0 CORE-DATE reference conformance tests”**, naming its test-suite revision and scope. This is not a third-party certification, an assertion of official institutional adoption, or a claim of EPOCH-ADAPTER conformance. The EPOCH-ADAPTER can be specified and tested synthetically now, but real-epoch conformance requires an authenticated future certificate.

## 19. Interface, localisation and governance

Human-facing month names (Janiix–Deciix), weekday names, minth shorthand/proper names, and names for Sixths/quarters are interface vocabulary. Structural machine interchange is numeric. An implementation MUST preserve the same canonical identity under any localised display form.

A date **does not** imply which weekday an independent uninterrupted seven-sol religious/rest schedule would use; the civil week deliberately resets at selected boundaries. Future social policies are outside this technical protocol.

The protocol versions separately: (a) **civil rule set**, (b) **reference clock profile**, and (c) **historical epoch realisation certificate**. Do not conflate all three into a lone date string. A later civil-rule change cannot retroactively reinterpret stored date strings without explicit versioning/migration.

## 20. Normative provenance, licensing and author freeze

This **author-ratified technical standard** is a distinct work derived from the author's editor-approved manuscript and checked technical evidence. © JB Bullock 2026. This standalone normative specification and marked original technical documentation are offered under **Creative Commons Attribution 4.0 International (CC BY 4.0)**; marked original reference implementations and software test tools are under **Apache License 2.0**, as expressly approved by author decisions D09–D10. See `../LICENSES/README.md` and included complete legal texts. Attribution and identification of modifications remain obligations of downstream reusers.

The literary book *Marian: An Operating Calendar for Human Mars*, its cover and all illustrations are separately **all rights reserved**, and are **not included** in this release. External NASA/IAU/NAIF material is not relicensed. JSON fixtures and schemas follow the package's explicit licensing map; bibliographic links and names do not confer rights over third-party source texts.

All ten decisions D01–D10 were author-approved on 8 October 2026. Future H/C/E event instantiation, high-precision SPICE execution, public deposit, a DOI and institutional adoption remain outside this normative freeze. No actual first-step or MY1 timestamp is asserted here.

### Source and evidence register

- JB Bullock, *Marian: An Operating Calendar for Human Mars*, editor-approved DOCX (2 October 2026), Appendix A (calendar structure), B (tables), C (astronomical rationale), D (identity/conversion). **Controlling literary source.**
- M2a, *Marian Integer Structural Audit*, 8 October 2026: exact structural test suite, golden century and proof.
- M2b, *Marian Astronomical and Epoch Assumptions Audit*, 8 October 2026: NASA Mars24 analytic crossing model (conditional).
- M2c1, *Scientific Conditional Closure*, 8 October 2026: independent Moshier/IAU analytic corroboration, not JPL SPICE execution.
- M2c2, *Epoch and Clock-Standard Closure*, 8 October 2026: tested synthetic AMT clock bridge; its four convention decisions subsequently author-ratified in M3c.
- NASA GISS Mars24 published algorithm: https://www.giss.nasa.gov/tools/mars24/help/algorithm.html . NASA GISS Mars24 technical notes: https://www.giss.nasa.gov/tools/mars24/help/notes.html .
- NAIF SPICE `lspcn`: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/cspice/lspcn_c.html . SPICE time definitions: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/C/req/time.html .
- IERS leap-second service: https://datacenter.iers.org/productMetadata.php?id=16 . BIPM time metrology: https://www.bipm.org/en/time-metrology .

**End of author-ratified Marian Protocol v1.0. No claim of formal institutional adoption, actual MY1 timestamp, completed SPICE verification, public release or editorial change to the manuscript.**
