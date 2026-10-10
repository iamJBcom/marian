# Marian: An Operating Calendar for Human Mars
## An open technical overview of Marian Protocol v1.0

**About this technical companion.** This author-approved explanatory article is subordinate to Marian Protocol v1.0. Original technical prose is designated for CC BY 4.0 release; the literary book and illustrations remain all rights reserved.

### The problem is human coordination, not Martian time measurement

Mars already has accurate systems for counting mission sols, expressing local solar time and locating the planet seasonally by areocentric solar longitude (Ls). But a permanent human settlement needs a *civil* calendar: repeatable dates for schools, contracts, public services, maintenance, birthdays and institutional planning. That calendar must organise an almost Earth-length day inside a year of approximately 668.6 sols. The near-Earth day makes familiar week-length intervals attractive, but the long year makes an ordinary twelve-month division almost twice as long as an Earth month.

A design that preserves twelve annual months produces approximately 56-sol units—good for annual orientation, awkward for short administrative cycles. A design that preserves approximately four-week months naturally produces around twenty-four named periods per year—good for cadence, less familiar as a twelve-part annual map. Marian's central response is **functional separation**: the planet's orbit and people's operating rhythms need not be forced into the same calendrical unit.

### Seven civil scales, with different jobs

A Marian year contains **12 months**, **24 minths**, **6 Sixths**, **4 quarters** and **96 nominal civil-week positions**, all built over uninterrupted physical Martian sols. In a common year the month lengths are **56–56–55**, repeated four times. The first minth of every month is 28 sols; the second is 28 or 27. Thus every month contains two minths, and every year has twenty-four. Four 167-sol common-year quarters provide four annual fractions; six Sixths group two months apiece and last 111–112 sols (the last grows to 112 in leap years). A calendar may have overlapping useful partitions: a Sixth can cross a quarter boundary, because the two represent different functions.

| Scale | Regular form | Civil purpose |
|---|---|---|
| Sol | One continuous Martian mean solar day | Lived day |
| Civil week | Seven nominal weekday positions; some terminal weeks have six | Recurrence |
| Minth | 27 or 28 sols; 24 each year | Near-four-week short cadence |
| Month | 55 or 56 sols; 12 each year | Twelve-part annual orientation |
| Sixth | 111 or 112 sols; 6 each year | Medium-range cadence |
| Quarter | 167 sols, except final leap quarter at 168 | Four-part annual orientation |
| Year | 668 or 669 sols | Seasonal-year civil frame |

### Weeks: the explicit trade-off

Marian gives every month eight *nominal* civil weeks. In a 56-sol month, all eight are seven-position weeks. In a 55-sol month, the eighth ends after weekday 6 (Satsol). The seventh label, Sunsol, **is absent from that terminal civil week**; the next **physical** sol begins the next month as weekday 1 (Monsol). **No physical sol is lost or skipped.** In an ordinary year there are four such short terminal weeks, at the ends of Months 3, 6, 9 and 12. A leap year has only three, because the final Sunsol exists.

This makes the weekday position of every valid recurring civil date invariant, and allows perpetual printed and software calendar layouts. Its price is interrupted civil weekday succession, which some cultural, religious or work-rest practices may reject. A continuous elapsed seven-sol count remains available separately. Marian presents that as a substantive social trade-off, **not** as an unqualified improvement over calendars with a continuous weekly cycle. Darian and Levitt provide important precedent for shortening terminal weekday sequences.

### Exact leap arithmetic

Marian has 668-sol common years and 669-sol leap years. The mnemonic rule is: **“Odd years leap. Tens leap. Hundreds do not.”** A year is leap if it is not divisible by 100 and is either odd or divisible by 10. Exactly **59 of every 100** regular years are leap, giving **66,859 sols per 100 years** and **668.590000 sols** per mean civil year. Leap status and the identity of any date in MY1 onward can be determined entirely by integer arithmetic, without an ephemeris. The leap sol is the final Sunsol of Month 12; it changes no earlier date.

The mathematical structure was independently executed and tested in Python and JavaScript using an exhaustive **66,859-sol** first-century ledger. These are calendar-integer verification results, not evidence that the physical Martian year is constant to six decimal places.

### A Martian year with an Earth-facing benefit

The regular year is astronomically referenced to **Ls = 15°**, a fixed point in the Martian *seasonal* cycle. In the intended reference era, that places the Marian annual origin near the Sun-centred direction of Earth around Gregorian New Year. Thus the two worlds retain comparable **twelve-part annual orientation** without pretending that their years are simultaneous or equal in duration. By design, Marian months do **not** correspond to equal 30° sectors of Mars's orbit; accurate seasonal position remains the business of Ls and ephemerides.

A related coarse visual heuristic uses the circular separation between contemporaneous Gregorian and Marian month numbers, from 0 to 6. In the author's September 2026 preprint, a synthetic 2031–2120 comparison reports a descriptive Spearman correlation of approximately **0.9403** between this month gap and modelled Earth–Mars **one-way light time (OWLT)**, with checks across 41 synodic cycles. The categories overlap substantially. The heuristic may help a human estimate the *general* state of Earth–Mars geometry; it **cannot** give a communications window, a safe command delay or an operational OWLT. Spaceflight operations must use actual ephemerides and communications calculations. These findings belong to a modelled study, not to the normative civil-date arithmetic.

### Identity, language and Martian cultural ownership

The normative computer-readable identities are numeric: 12 months, minths 01–24 and explicitly defined date fields. Marian provides A–X as a compact minth shorthand and familiar recommended weekdays, but it does not require a single worldwide poetic vocabulary. Languages and future communities may choose their own human-facing names without changing a stored date or interoperability rule. This creates room for early Martians to participate in naming their own time rather than inherit a complete terrestrial naming settlement.

### The future founding epoch—and honest limits

The recognised first human step on Mars begins transitional **MY0**. The first passage through Ls = 15° strictly after that step, followed by the first strictly subsequent canonical Airy Mean Time midnight, establishes the start of regular **MY1**. Marian Protocol v1.0 specifies a versioned Mars24-derived, TT-based Airy mean-sol clock for this boundary. Since these events have not yet occurred, there is **no real founding timestamp**, authenticated epoch certificate or presently valid absolute Earth↔Marian civil-date bridge. Synthetic epochs are for testing only.

The Ls = 15° annual recurrence has been checked by two analytic astronomical approaches, but the separate high-precision SPICE-kernel comparison was not completed. Astronomical precision over a far-future settlement era therefore remains conditional. Nor has human preference for minths, Sixths or fixed weekday dates been tested empirically on a Martian population.

### What is available to reuse

Under the proposed release, the **author-ratified Marian Protocol v1.0** and specifically designated original technical explanations and evidence will be available under **CC BY 4.0**, with original reference software and conformance tools under **Apache 2.0**. The independently readable illustrated book *Marian: An Operating Calendar for Human Mars* remains **all rights reserved**. No calendar has been adopted by a Martian government or standards authority. The proposal is offered to future builders as transparent operating architecture, not as a claim of cultural authority over their lives.

**Read next:** normative protocol; test and reproducibility suite; evidence/prior-art analysis; Marian–Darian comparison; web book. **The normative protocol has no new DOI yet; existing Marian research DOIs are listed in PUBLICATIONS.md.**

---

### M6c source verification notes (editorial annex)

These notes document source provenance and do not alter the author-approved analysis. The normative Marian Protocol v1.0 is held in the separate, frozen technical repository; the link must be set to the real public URL at release. The following primary and official sources were checked for the specific facts attributed to them:

- Thomas Gangale, *The Darian Calendar* (1998), [original proposal](https://marspapers.org/paper/MAR98095.pdf): 24 months, 27/28-sol variation and shortened terminal weeks.
- Thomas Gangale, *The Architecture of Time, Part 2: The Darian System for Mars* (2006), [SAE technical paper](https://doi.org/10.4271/2006-01-2249): publication and system overview.
- Josef Šurán, *A Calendar for Mars* (1997), [journal record](https://doi.org/10.1016/S0032-0633(97)00033-0): leap/skip-day and leap/skip-week approaches.
- NASA GISS, [Mars24 calculation documentation](https://www.giss.nasa.gov/tools/mars24/help/algorithm.html), updated 2025: official mean-sol and seasonal-coordinate reference.
- Thomas Gangale, [Darian adaptations for East Asian cultural nomenclature](https://www.researchgate.net/publication/390729531_Expanding_the_Cultural_Relevance_of_the_Darian_Calendar_of_Mars_to_East_Asia) (2025): additional names should not be misrepresented as nonexistent.

**Source limitation:** the 1954 Levitt work is credited through the author's research preprint and historical discussion rather than a newly inspected 1954 scan. The 2031–2120 Earth–Mars OWLT figures come from JB Bullock's archived September 2026 research preprint; M6c reconciles the quotations against that manuscript but does not rerun its 32,872-observation simulation or make the preprint public. External re-evaluation requires release or equivalent reproduction of the corresponding research methods/data. None of these limitations alters the verified integer-calendar rules.

