# Scientific evidence and uncertainty

This page is a summary of **recorded historical tests** and is not a new ephemeris computation. Original reports and result JSONs are preserved under [`research/`](../research/README.md).

| Proposition | Evidence | Status |
|---|---|---|
| 59 leap years per 100; 66,859 sols; civil mean exactly 668.59 | Exhaustive M2a integer audit, independent CORE tests | **Verified mathematical property** |
| Ls = 15° recurrence is close to 668.59 sols in a historical model interval | M2b NASA Mars24 analytical crossing series | **Model-dependent approximation** |
| Distinct analytical approach corroborates recurrence near 668.59 | M2c1c Swiss Ephemeris/Moshier + IAU Mars pole model | **Independent analytical corroboration, not high-precision SPICE** |
| SPICE/JPL kernel-backed Ls = 15° crossing series | M2c1b prepared execution plan | **Not executed** |
| Actual first human step and MY1 midnight | Events have not yet occurred | **Uninstantiated future facts** |
| Real UTC/TT/Gregorian conversion from MY dates | Requires authentic epoch certificate and time-standard realisation | **Not implemented for real dates** |
| Long-term bounded error for any unknown future Mars founding era | No founding-era high-precision ephemeris test | **Not established** |

**Recorded 1900–2100 model sample:** Mars24: 106 crossings, 105 intervals, mean **668.589175 sols**. Independent Moshier/IAU analysis: 106 crossings, mean **668.589369 sols**. A specific illustrative 100-year civil-minus-model interval gave approximately +0.048 sol and +0.030 sol respectively. These are *examples for the analysed interval*, not general future guarantees or a proof of phase bounds across centuries.

The **civil mean 668.590000** is exact by arithmetic. The **astronomical recurrence** varies and depends on ephemeris, Ls convention and interval. Avoid confusing the two. Do not infer precise Earth–Mars light-time or opposition dates from simple calendar month arithmetic.

**Authority:** the [ratified normative specification](../protocol/spec/MARIAN-PROTOCOL-v1.0.md) fixes what Marian *defines*. The historical evidence in `research/` describes what earlier investigations *calculated*. They play different roles.
