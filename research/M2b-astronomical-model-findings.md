# M2b — Marian Astronomical and Epoch Assumptions Audit

**Marian: An Operating Calendar for Human Mars** — JB Bullock  
**Audit date:** 8 October 2026  
**Audit result:** **CONDITIONAL / PARTIAL SCIENTIFIC VERIFICATION**, not an ephemeris-grade pass. The canonical calendar is unchanged.

## Scope and evidence tiers

- **A — Verified structural mathematics:** M2a integer arithmetic; 668/669 year forms and 59 leap sols per 100 years. No fresh calendar design decision.
- **B — Reproduced astronomical approximation:** independent implementation of the published NASA GISS Mars24 analytic series and Airy Mean Time conversion, benchmarked against NASA's numerical worked example.
- **C — Quantified within model only:** Ls=15° recurrence intervals, mean and distribution; two *hypothetical* civil-to-astronomy phase trials.
- **D — NOT VERIFIED:** SPICE/JPL Horizons independent ephemeris check; far-future founding-era astronomical rates; exact human-step epoch; authoritative UTC↔TT↔TDB↔AMT implementation and leap second arrangements; empirically optimal Ls=15° versus Ls=22°; realised usability of any month-gap heuristic.

## Mean tropical year is NOT an Ls=15° year

NASA Mars24's technical notes distinguish the mean tropical year **668.5921 sols**, the mean vernal-equinox recurrence (~668.5906 sols), and other seasonal recurrence intervals. A fixed Ls=15° crossing should therefore be computed using the position model; the **668.5921-sol mean** is **not** the appropriate direct comparison target for Marian.

## Method

The script `tools/mars24_model.py` independently applies NASA Mars24's published 2025 equations B-1 through B-5 and D-3 for Ls and heliocentric longitude. TT Julian Days are used uniformly, with the NASA-specified mean-sol scale of **1.0274912517 Earth days**, or **88775.244147 SI seconds**. The Mars24 Airy Mean Time equation C-2 is implemented for the rollover illustration. Roots of unwrapped Ls(t)=15°+360k are found with numerical bracketing. Do **not** mistake this for independent ephemeris data. NASA reports that its short series was tested against precise ephemerides within ~±100 Earth years of J2000. Analysis remains within that range.

A published Mars24 worked example for **2000-01-06 00:00:00 UTC** uses TT−UTC=64.184 seconds. The replicated outputs are **Ls=277.18758944°** (NASA tabulates 277.18758°) and **Airy Mean Time=23.99424946 hours** (NASA tabulates 23.99425 hours). Both pass the declared rounding tolerances.

## Calculated Ls=15° recurrence — *Mars24 model only*

- 106 model crossings, 105 consecutive complete Ls=15° intervals across ~1900–2100.
- Mean interval **668.589175253 sols**; individual intervals **668.556124205 to 668.624821518 sols**.
- That mean represents the examined century-spanning model interval; **it is not a timeless or future settlement-specific recurrence**. The actual model includes short-period perturbations.
- At those modeled Ls=15° crossings Mars's heliocentric ecliptic longitude under NASA's associated formula spans approximately **99.8488° to 100.2455°**. This supports the approximate direction **100°** in the modeled interval; it does not establish that Earth and Mars New Year are simultaneous, or close together.
- Earth's New Year heliocentric-direction comparison is qualitatively consistent with published orbital elements, but **no separate matched-frame Earth ephemeris series was run**; the magnitude and robustness of the Earth–Mars month-gap claim remain open.

## Bounded phase versus genuine drift

The cumulative number of sols from the start of MY1 through MYn can be calculated exactly from the 59/100 cycle; M2a separately proved that. For an idealised strictly constant annual target 668.590000 sols, the century average matches exactly, and phase fluctuations arise only from placement. Real solar longitudes are not precisely periodic with a constant interval.

For a hypothetical instant when MY1 begins immediately at the **first Airy Mean Time midnight after the modelled Ls=15° crossing**, use:

- `crossing0`: original astronomical crossing (TT instant);
- `midnight0`: first model Airy midnight strictly after `crossing0`;
- `lag0 = (midnight0 - crossing0) / 1.0274912517`; `0 < lag0 <= 1` sol;
- `phase_n = lag0 + cumulativeCivilSols(n) − (crossing_n − crossing_0)/solLength`.

A negative `phase_n` means civil New Year is *before* that year's actual Ls=15° crossing. This does not invalidate the ONE-TIME MY1 rollover rule; it confirms that subsequent years must not be independently re-anchored to the sky.

Two **synthetic** starting cases, chosen to remain within the model's approximate validity:

| Measure | Historical 100-year proxy | 21st-century 35-year proxy |
|---|---:|---:|
| Starting crossing JD(TT) | 2418065.49951 | 2461344.59412 |
| Model mean Ls=15° recurrence | 668.589522 sols | 668.589722 sols |
| Initial following-midnight lag | 0.113447 sol | 0.981479 sol |
| Minimum model phase | -0.594910 sols | 0.264199 sols |
| Maximum model phase | 1.454074 sols | 1.689405 sols |
| Endpoint civil elapsed minus astronomical elapsed | +0.047830 sol | +0.359725 sol |

**No modeled phase bound is a permanent real-world bound.** A tiny discrepancy between the century civil mean and future Ls recurrence can accumulate across many centuries. The 35-year trial does not have a 59/100 cycle-mean by construction.

## Approximate, not canonical Airy rollover

NASA documents **Airy Mean Time**, whereas the book's normative phrase **“midnight at Airy-0”** alone leaves the choice between *mean* and *true* solar time (and the reference time-realisation) insufficiently explicit for independent implementers. For this test fixture only, `Airy Mean Time midnight` was chosen. **That is an audit assumption, not a change to Marian's approved rule.**

An eventual standard also needs the authoritative reference for Mars prime longitude (IAU), the adopted Mars rotation/clock model and its version, TT / TDB convention for ephemeris requests, and the applicable realised UTC / leap-second bridge. These details can affect an instant close to a boundary.

## First human step / MY0 and MY1

The manuscript states that MY0 begins with the recognised first human step, and MY1 at the first Airy-0 midnight following the **next** Ls=15° passage. The actual step and first MY1 timestamp are unknown and must never be presented as historical facts.

Four synthetic first-step scenarios are included in `fixtures/M2b-synthetic-MY0-scenarios.csv`. These demonstrate that the intervening MY0 can range from nearly zero to approximately a full Martian orbital year (plus the following-midnight lag), depending on the timing. **A first step exactly at Ls=15° is a protocol ambiguity**: the tests adopt *strictly following* for illustration; it needs an explicit tie-breaking standard before normative implementation. Equally, MY0 has no normal 668/669-sol layout and needs either an expressly partial-date representation or an external timestamp convention.

## Long-term sensitivity

For a **hypothetical constant** true recurrence `R` sols, the arithmetic drift after `N` complete 100-year cycles is exactly `N × (668.590000 − R)` sols, for a century-aligned epoch. The sensitivities in `fixtures/M2b-constant-recurrence-sensitivity-NOT-predictions.csv` are *illustrative, not forecasts*. The actual R varies with epoch and astrophysical conditions; projecting a linear constant R indefinitely would be misleading.

## Publication guidance

**Keep unchanged:** Ls=15° annual anchor; Airy-0 as reference meridian; MY0/first human step; MY1 one-time anchor concept; 59/100 ordinary intercalation rule; all integer calendar conventions.

**Tighten before M3 release:** define epoch-solving inputs and tie-breaks; use the words *Airy Mean Time* or another explicitly chosen reference; identify scientific coordinate/time standards; separate sampled model phase from a permanent accuracy claim; mark the ~100° relationship qualitative and frame-specific; explicitly defer full realised Earth/UTC conversion until epoch authority and timescale conventions are established.

**Do not claim:** actual MY1 determined; any exact UTC conversion currently possible; 59/100 provably optimal; model phase bound is a permanent astronomic guarantee; independent SPICE ephemeris comparison completed.

## External sources

- NASA GISS, Mars24 algorithm and worked examples, 2025-01-07: https://www.giss.nasa.gov/tools/mars24/help/algorithm.html
- NASA GISS, Mars24 technical notes, 2023-05-15: https://www.giss.nasa.gov/tools/mars24/help/notes.html
- Allison & McEwen (2000), underlying paper information: https://www.giss.nasa.gov/pubs/abs/al05000n.html
- IAU, 2015 cartography/prime-meridian changes explained: https://iauarchive.eso.org/news/announcements/detail/ann18010/
- IERS, TT / UTC / TAI conventions: https://www.iers.org/iers/en/service/faqs/thenewiauresolutions/timeargumentforusingiersproducts-104-157
