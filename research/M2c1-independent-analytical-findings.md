# M2c1c Scientific Assessment — Close M2c1 Conditionally

**Work:** Marian: An Operating Calendar for Human Mars — JB Bullock  
**Date:** 8 October 2026  
**Finding:** M2c1 may be closed **CONDITIONAL**, with the JPL/NAIF SPICE validation explicitly **unperformed/deferred**. No new ephemeris-grade accuracy has been proved.

## 1. Basis and reproducibility

The prior M2b reproduced NASA's Mars24 analytical short-series for Mars solar longitude (Ls) and obtained 106 estimated Ls=15° passages in the approximately 1900–2100 window. The M2c1 and M2c1b work prepared JPL/NAIF SPICE `lspcn` extraction but binary SPK acquisition failed in the isolated runtime. NASA Horizons API documentation is accessible, but the dynamical data endpoint could not be retrieved. No SPICE/JPL ephemeris crossing data have been represented as generated or verified.

For this closure, a *separate* model was run from a library already installed in the runtime: Swiss Ephemeris 2.10.03 with `FLG_MOSEPH`, which uses Moshier's approximate, built-in heliocentric planetary positions rather than Mars24's analytical formula or a downloaded JPL binary SPK. At each uniform ephemeris-style Julian Day, Mars heliocentric position/velocity in J2000-equatorial coordinates is used to form the instantaneous orbital-normal `z = unit(r × v)`. The Mars north-spin-axis vector `p` is formed from IAU pole right ascension and declination:

- RA(T) = 317.68143° − 0.1061° × T;
- Dec(T) = 52.88650° − 0.0609° × T;
- T = (JD − 2451545.0)/36525.

The reference axes are `x = unit(p × z)` and `y = z × x`, and `Ls = atan2((-unit(r)) · y, (-unit(r)) · x)` reduced to [0°, 360°). The geometry follows the published NAIF `lspcn` reference description, but **does not execute the SPICE routine** and does **not** claim equivalent frame/aberration treatment. Crossings are found with an independent 12-day phase-wrap scan and Brent root-solver. The independent root search uses no Mars24 crossing-date estimates. The Mars24 baseline is used only after the roots are found.

The orbital engine itself is still **semi-analytical**; Swiss Ephemeris documentation describes Moshier as a semi-analytical approximation to JPL's DE404 ephemerides. That is a different computation from Mars24 but is not an independent high-precision JPL DE440 SPK evaluation.

## 2. Results: the two calculations support the same annual-rate conclusion

| Property | Independent Moshier+IAU model | NASA Mars24 analytical implementation |
|---|---:|---:|
| Crossing count, 1900–2100 | 106 | 106 |
| Number of intervals | 105 | 105 |
| Mean Ls=15° recurrence (sols) | 668.589368919 | 668.589175253 |
| Individual interval range (sols) | 668.561834–668.616757 | 668.556124–668.624822 |
| Civil mean from the canonical 59/100 rule | 668.590000 | 668.590000 |

The independently calculated crossings differ from the Mars24 crossing timestamps by **−0.012252 to +0.016905 sol**, i.e. at most approximately 0.017 sol (about 25 minutes). On 402 sampled dates the maximum absolute Ls difference was approximately **0.014032°**. Do **not** call this difference a measured Mars24 error relative to JPL: it also reflects differences in the two approaches' modelling of orientation, coordinates, and correction conventions. The two frames were not proven equivalent at the ephemeris-grade level.

In the M2b historical **synthetic** test window, 100 successive Ls=15° intervals comprise approximately **66,858.970439 sols** in the independent model; the integer civil sequence comprises **66,859 sols**, a **+0.029561-sol** endpoint difference. Mars24's corresponding synthetic result is **+0.047830 sol**. These endpoint numbers apply to that *particular hypothetical* starting crossing, within an earlier historical window, not every possible 100-year interval or an unknown future MY1.

If the initial synthetic following-midnight lag from **Mars24** is held fixed at 0.113446996 sol, the independent orbit-crossing series gives a civil-minus-crossing phase range of roughly **−0.598246 to +1.439685 sols** through the 100-year sample. This is deliberately mixed-model and not an independent test of Airy midnight.

## 3. Third-party ephemeris support versus tests performed here

NASA GISS Mars24 technical notes report that their adopted short-series Ls was compared to an accurate ephemeris with an estimated maximum angular error of **0.008°** over approximately ±100 Earth years of J2000. That is an *external published comparison* by NASA, and helps justify the use of Mars24 as an approximate astronomical reference. It is **not** a reproducible independent SPICE run performed in this audit. In particular, the Moshier-vs-Mars24 maximum angular difference reported above is **not** evidence contradicting NASA's quoted maximum: this implementation has not established that its chosen geometric definition, pole orientation model, and correction conventions match NASA's accuracy-validation setup.

NASA also distinguishes the **mean tropical year** of ~668.5921 sols from the season-specific recurrence of Ls; applying the general mean tropical-year number directly to the Marian Ls=15° target would not be valid.

## 4. Exactly what the evidence allows

**Proven (integer/calendar):** 59 leap sols per 100 regular Marian years, 66,859 sols per century, 668.59 civil mean, deterministic recurrence and date arithmetic. This was established by M2a, not this astronomical calculation.

**Supported by two different approximate astronomical calculations:** around the historical comparison window, the recurrence of Ls=15° has a mean near 668.59 sols. The 59/100 *frequency* is reasonable for that reference and is close in both computations. This supports **selection of the canonical design**, not proof of an optimally placed intercalation regime.

**Not established:** independently executed Horizons/SPICE exact crossing timestamps; guarantees about the future first-step epoch; exact present or future MY1 Gregorian/UTC date; guaranteed centuries-long phase bounds; secular or future drift without a newer ephemeris and founding epoch; all-frame precision; proof that Ls=15° is optimal; changes in the IAU pole model or how Airy-0 time is realised.

## 5. Disposition and M2c2 handoff

The lack of downloadable NAIF binary kernels is **not** an essential blocker to publishing an honestly qualified Marian technical proposal. It is essential only if one wants to claim ephemeris-grade independent validation or a specific guaranteed long-term accuracy. Such claims must not be made.

**Decision:** mark **M2c1 CONDITIONAL SCIENTIFIC CLOSURE (with SPICE deferred)**, retain M2c1b's unused high-precision procedure as a future verification path, and **proceed to M2c2 — Epoch and Clock-Standard Closure**. Do not reopen the settled integer design or presume that any synthetic first-human-step date is a realised epoch. No new authorship or publication claim arises from these tests.

## 6. Sources and restrictions

- Swiss Ephemeris, Moshier approximate planetary model: https://www.astro.com/swisseph/swisseph.htm
- NAIF `lspcn` planetary solar longitude definition: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/MATLAB/mice/cspice_lspcn.html
- NAIF frame/PCK Mars north-pole constants: https://naif.jpl.nasa.gov/pub/naif/toolkit_docs/FORTRAN/req/frames.html
- IAU cartographic constants (Archinal et al. 2011): https://aa.usno.navy.mil/downloads/reports/Archinaletal2011a.pdf
- NASA Mars24 notes (published approximation and external precision comparison): https://www.giss.nasa.gov/tools/mars24/help/notes.html
- NASA Mars24 algorithms: https://www.giss.nasa.gov/tools/mars24/help/algorithm.html
- JPL Horizons API documentation: https://ssd-api.jpl.nasa.gov/doc/horizons.html

Swiss Ephemeris is a third-party library with its own licensing conditions. The source library is **not bundled**, sublicensed, or described as Apache-licensed by this project.
