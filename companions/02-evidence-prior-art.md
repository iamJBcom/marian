# Marian: Evidence, Prior Art and the Limits of the Claims

**About this technical companion.** This author-approved explanatory article is subordinate to Marian Protocol v1.0. Original technical prose is designated for CC BY 4.0 release; the literary book and illustrations remain all rights reserved.

## The three evidence categories

**1. Proven by construction and executable tests.** The 56–56–55 common-year pattern gives 668 sols; a final extra Sunsol gives 669. Every month comprises two minths, yielding 24 per year. Sixths group two months; quarters group three. Four ordinary short terminal civil weeks (three in leap years) preserve invariant weekday labels for valid recurring dates. The odd/ten/century rule yields 59 leaps and 66,859 sols per 100 years. The reference package tests all 66,859 positions in MY1–MY100, plus additional boundaries. These are exact claims about a *defined integer system*, not observations of Mars.

**2. Corroborated by modelling, with limitations.** The annual Ls = 15° recurrence was compared using NASA Mars24 and an independent Moshier/IAU analytical calculation across the tested historical interval, supporting a rate near 668.59 sols. That does not constitute an executed independent JPL-SPICE-kernel verification, nor does it guarantee the error bound at a future founding epoch. The 2031–2120 Earth–Mars *circular month-gap / OWLT* study in the earlier research preprint reports ρ ≈ 0.9403 across 32,872 modelled daily observations, a monotone rise in median OWLT across gaps 0–6, and within-cycle checks across 41 complete synodic cycles. It is an approximate communications *orientation*, not an operational prediction. The pooled daily observations are strongly serially dependent: do not report naïve inferential significance as if they were independent experimental samples.

**3. Design judgements and hypotheses.** Whether a four-week cadence is useful for Martian work, whether inhabitants prefer weekday invariance to an uninterrupted named week, whether 'minth' or 'Sixth' becomes natural language, whether Marian nomenclature reduces onboarding cost, and whether its open implementations cause adoption are **not experimentally established facts**. They are explicit human/institutional design arguments that can eventually be tested.

## Intellectual lineage: what Marian does not claim to invent

**I. M. Levitt (1954).** The decisive direct antecedent for 12 Martian months arranged **56–56–55** repeatedly, equal common-year 167-sol quarters and shortened terminal weekday sequences. Marian must credit this origin directly, not market the month arithmetic as unprecedented.

**Thomas Gangale / Darian Calendar.** Darian formalised a 24-month Martian architecture using 27/28-sol months and a comparable six-position terminal-week convention, preserving fixed weekday positions. Gangale's own work explicitly recognised the connection between bisected Levitt months and Darian's short-period structure. The meaningful Marian move is to preserve both scales *as explicitly named distinct functions*, not to imply Darian lacked knowledge of the arithmetic.

**Gangale and Dudley-Rowley.** The history of Martian civil time demonstrates a long and serious field of alternative proposals. Marian's systems-engineering framing sits within, rather than erases, that literature.

**Josef Šurán.** Explored leap/skip-day and whole-week adjustments, clarifying the trade-off between exact annual length, fixed date recurrence and uninterrupted weekly succession. Marian chooses the shortened-week side of that trade.

**Robert Zubrin.** Greater orbital/seasonal angular representation in months, accepting unequal civil durations. Marian keeps civil elapsed-duration periods regular and retains precise Ls as a separate coordinate.

**Hargitai and collaborators.** Used a 12×56-sol climate representation with irregularity concentrated in the terminal month and a different annual starting reference. Marian's distributed four one-sol reductions yield equal 167-sol common quarters.

**Dennis Silin / Exodus.** Retains familiar Earth month names and assigns a different pattern of annual adjustment; it illustrates another legitimate way to prioritise immediate familiarity.

**Fairman and long-term seasons.** Highlights the difficulty of maintaining simple permanent alignment among a seasonal calendar, Mars's elliptical orbit and evolving orbital geometry. Marian cannot promise that a fixed static civil calendar will encode exact future seasonal position.

The original comparative works are cited in the author's research preprint. An external-source bibliography and source-specific URLs should accompany this page at publication; copied images or excerpts from those works are *not* included in the open technical grant.

## Marian's narrower positive contribution

Marian explicitly combines twelve annual-orientation months, twenty-four near-four-week minths, six medium-range Sixths and four quarters in a consistent civil coordinate system. It adds canonical numeric identities, optional compact A–X minth shorthand, adaptable local human names, a Mars-seasonal **Ls = 15°** year origin selected partly for coarse Earth–Mars phase intelligibility, a memorable 59/100 leap sequence, an independently testable conformance suite and a source-specific public licensing plan. **The architecture is a composition plus an evaluation against stated requirements; it is not a claim to invent each constituent part.**

## Specific numerical evidence and scope

| Claim | Source/evidence | Correct qualification |
|---|---|---|
| 668 / 669 sols; 59/100; 66,859/century | Frozen Marian Protocol v1.0 and M2a/M3b tests | Exact mathematical behaviour for MY1+ |
| 12 months, 24 minths, 6 Sixths, 4 quarters | Protocol construction | Exact defined structure |
| Fixed weekday for valid recurring dates | Shortened terminal civil week plus tests | Interrupts uninterrupted weekday naming; no physical sol skipped |
| Ls = 15° annual rate near 668.59 | M2b/M2c1c analytic models | Model-dependent; SPICE execution outstanding |
| Gregorian–Marian month-gap vs modelled OWLT, ρ ≈ 0.9403 | September 2026 preprint §§6.4, 7.5–7.6, Fig. 6 | Synthetic 2031–2120 study; not a navigation instrument |
| OWLT median gap 0 ≈ 5.21 min; gap 6 ≈ 20.98 min | Preprint Fig. 6 | Distribution overlap; medians not guaranteed individual values |
| 41 synodic-cycle robustness analyses | Preprint §7.5 | Serial-dependence control, not experimental validation |
| Better learner adoption, greater community preference | Design hypothesis only | No empirical study; do not state as proven |
| Open technical standard and original reference implementation | Author-approved CC BY / Apache scopes, M3 ratification | Open release **planned**, not yet made public; avoid unsupported claims that competing systems lack openness |

## Publication and independent evaluation safeguards

- Keep the normative Protocol v1.0 **immutable**; technical papers, overview and comparative advocacy are explanatory and subordinate.
- Do not present the earlier JBIS/Acta preprint as accepted or published; check venue rights and preprint policy before attaching a PDF or converting it into an open technical artefact.
- Include the published original sources as citations, not as bundled copies. Attribute Darian and Levitt fairly.
- Keep experimental/analytical figures traceable to the actual simulation, parameter regime and source code; don't call a modelled OWLT an observed OWLT.
- Preserve the lack of an authenticated founding epoch and the incomplete SPICE validation.
- Disclose exactly which technical files are CC BY 4.0 or Apache 2.0; exclude the literary book/illustrations from those grants.
- Encourage third parties to challenge these claims through alternate ephemerides, test vectors, human-factors research and comparative reference implementations.

**Scientific qualification:** authorial sign-off is complete; first-hand inspection of the Levitt (1954) print original and independent re-execution of the preprint OWLT study remain separate evidence improvements, not claims of completed verification.

---

### M6c source verification notes (editorial annex)

These notes document source provenance and do not alter the author-approved analysis. The normative Marian Protocol v1.0 is held in the separate, frozen technical repository; the link must be set to the real public URL at release. The following primary and official sources were checked for the specific facts attributed to them:

- Thomas Gangale, *The Darian Calendar* (1998), [original proposal](https://marspapers.org/paper/MAR98095.pdf): 24 months, 27/28-sol variation and shortened terminal weeks.
- Thomas Gangale, *The Architecture of Time, Part 2: The Darian System for Mars* (2006), [SAE technical paper](https://doi.org/10.4271/2006-01-2249): publication and system overview.
- Josef Šurán, *A Calendar for Mars* (1997), [journal record](https://doi.org/10.1016/S0032-0633(97)00033-0): leap/skip-day and leap/skip-week approaches.
- NASA GISS, [Mars24 calculation documentation](https://www.giss.nasa.gov/tools/mars24/help/algorithm.html), updated 2025: official mean-sol and seasonal-coordinate reference.
- Thomas Gangale, [Darian adaptations for East Asian cultural nomenclature](https://www.researchgate.net/publication/390729531_Expanding_the_Cultural_Relevance_of_the_Darian_Calendar_of_Mars_to_East_Asia) (2025): additional names should not be misrepresented as nonexistent.

**Source limitation:** the 1954 Levitt work is credited through the author's research preprint and historical discussion rather than a newly inspected 1954 scan. The 2031–2120 Earth–Mars OWLT figures come from JB Bullock's archived September 2026 research preprint; M6c reconciles the quotations against that manuscript but does not rerun its 32,872-observation simulation or make the preprint public. External re-evaluation requires release or equivalent reproduction of the corresponding research methods/data. None of these limitations alters the verified integer-calendar rules.

