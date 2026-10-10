# Marian and Darian: A Serious Comparative Evaluation
## What Marian adds, what it gives up, and the best objections to its adoption

**About this technical companion.** This author-approved explanatory article is subordinate to Marian Protocol v1.0. Original technical prose is designated for CC BY 4.0 release; the literary book and illustrations remain all rights reserved.

### Two serious calendars, much shared inheritance

The Darian Calendar is not an inferior preliminary attempt awaiting Marian's correction. Gangale's design solves a clearly stated Martian civil-time problem: preserve short month-like operating periods, stable dates and a predictable recurring calendar across a 668/669-sol year. Darian's 24 primary months normally last 28 sols, with three or four 27-sol intervals. Its selected terminal weeks omit the seventh weekday label so the next month starts consistently on weekday 1. It uses the northern spring equinox, **Ls = 0°**, as the annual reference. The mechanism predates Marian. The earlier Levitt calendar already offered 12 months arranged **56–56–55** and a shortened terminal-week device. Marian's central claim is *architectural composition*—a defensible way to organise two useful temporal scales—rather than discovery of either arithmetic pattern.

### The central choice: keep either twelve or twenty-four? Marian keeps both.

Darian calls the near-four-week division a **month**. That protects duration familiar to an Earth-born resident. It also means there are twenty-four primary month positions in one Martian year, so terms like 'the third month' and 'twelve months into the year' no longer carry the familiar fraction of the annual cycle. This can be learned; it is not a logical failure. But it is a real design trade.

Marian instead supplies **twelve 55/56-sol months** as a stable macro-level annual map and **twenty-four 27/28-sol minths** as a formal short-cycle cadence. Both are first-class *structural identities*, although they have different civic purposes. A Marian calendar can therefore answer 'Which of twelve annual positions?' and 'Which of twenty-four four-week-like operating periods?' without making one label serve both jobs. It does not pretend its 56-sol month feels like an Earth month; that work is assigned to the minth. In common years, the 24 minths consist of 20 intervals of 28 sols and four of 27, just as the familiar Darian-like short-duration layer would suggest. Darian proponents should recognise this as a shared arithmetic foundation, not a dismissal of their achievement.

### A stronger middle scale

An Earth quarter is both approximately thirteen weeks and one fourth of the terrestrial year. On Mars those roles separate. Marian retains four quarters as annual fractions—167 sols in a common year—and also establishes six **Sixths**, each two months / four minths / about 111–112 sols, for medium-horizon institutional planning. Darian can always define equivalent groupings mathematically, but Marian makes those groupings explicit and interoperable in its protocol. The strength is an optional *common vocabulary* of planning periods, not a proof that every Martian organisation would use Sixths.

### A year that belongs to Mars but has a deliberate Earth-facing orientation

Darian begins at **Ls = 0°**, the northern vernal equinox: a scientifically recognisable, defensible and easy-to-describe seasonal origin. Marian begins at **Ls = 15°**, also a Martian seasonal coordinate, but chosen to place the annual origin near Earth's **Gregorian-New-Year heliocentric direction** around the envisaged founding-era reference. These New Years are *not simultaneous*, and a Marian year is much longer than an Earth year. The advantage is a broadly compatible **twelve-position annual mental map**, not a shared clock or common date.

This is a genuine design differentiator. It accepts a less symbolically obvious Martian New Year in exchange for an additional Earth–Mars wayfinding property, potentially valuable in a settlement that remains institutionally connected to Earth. The Ls = 15° rationale is era-sensitive and model-dependent, not an astronomical theorem that always outperforms an equinox-based calendar.

### The communications heuristic is a bonus, not magic

The September 2026 Marian preprint evaluates the *circular gap* between contemporaneous Gregorian and synthetic Marian month numbers (0–6) against modelled heliocentric phase and **Earth–Mars one-way light time (OWLT)**. Across **32,872 simulated daily observations in 2031–2120**, it reports Spearman **ρ ≈ 0.9403** for month gap versus OWLT; category medians rise from about **5.21 minutes** at gap 0 to **20.98 minutes** at gap 6. The study reports comparable relationships within **41 complete synodic cycles** and an independent analytical planetary-position cross-check.

That is evidence of a useful *coarse mental orientation* in the tested model. It is emphatically **not** evidence that a month number accurately predicts real-time link delay or conjunction blackouts. The gap categories overlap, orbital distances depend on eccentricity, and precise mission communication uses ephemerides and line-of-sight models. The research is also based on a synthetic Marian epoch—not a historically realised one. Marian's explanatory advantage survives these qualifications: a person may gain some intuition from ordinary civil dates without ever treating the calendar as an operational communications instrument. Darian's Ls = 0° design was not, on the evidence reviewed, explicitly optimised for this particular civil-phase metric; that does **not** mean a Darian variant could never provide a comparable heuristic.

### Openness as an implementation advantage, not a historical put-down

Marian Protocol v1.0 has a formally author-ratified specification and reproducible tests, plus proposed publication of its **original technical text under CC BY 4.0** and **reference Python/JavaScript code under Apache 2.0**. That would allow anyone to inspect, adapt, translate and implement the named open components under clear per-file terms. Open conformance tests, schemas, historical verification records and version identifiers reduce uncertainty for a third-party implementer.

It would be misleading to assert that 'Darian is proprietary', 'Darian cannot be implemented' or 'there is no open Darian code'. Darian has extensive public descriptions and independent software implementations. The comparative claim we can safely make is narrower: **Marian is planned as a unified versioned, openly licensed and test-backed reference release with explicit normative authority and machine conformance materials.** A genuine apples-to-apples openness benchmark against particular Darian implementations would need a separate license and conformance audit. Public availability of a Darian paper, including a copyright notice, is not itself proof of the rights status of every Darian implementation.

### Names and adoption: lower ambiguity, not proven superiority

Darian's original primary month names drew on alternating Latin and Sanskrit zodiac nomenclature; multiple alternatives and translations have been proposed. This provides a rich cultural frame, but a new settler might face learning twenty-four primary proper names before navigating the annual calendar. Marian's **canonical machine identity is numeric**, with 12 numbered months, 24 numbered minths and an A–X shorthand for minths; human-facing names are optional and localisable. Familiar Monsol-to-Sunsol weekday names are offered as a recommended interface, not fixed cultural commandments. Short, reusable number forms can simplify cross-language documentation and technical onboarding.

This is a **testable usability hypothesis**, not a measured fact. Some communities may prefer Darian's explicit cultural names; some may find the word *minth* or the added *Sixth* alien. The stronger Marian argument is architectural: institutions can communicate precise dates now without requiring global agreement on the eventual poetic naming layer. And future Martians have genuine room to ratify the names of months and minths themselves, rather than inheriting a complete human vocabulary from Earth designers.

## The most serious objections—and Marian's strongest answers

**Objection 1: “Marian interrupts the seven-day week, which is unacceptable.”** This is serious and not refuted by calendar arithmetic. Darian makes substantially the *same* choice: a short final civil week preserves recurring dates by omitting one weekday label. Marian does **not** eliminate Darian's social cost. The defence is conscious design: dates carry stable weekday positions, monthly layouts repeat, and no *physical* sol vanishes. Communities requiring continuous seven-sol religious or industrial counting can maintain it as a separate elapsed cycle. People may still reject this compromise; that remains a legitimate reason to prefer another calendar.

**Objection 2: “Why invent minths when Darian already has 24 months?”** Because an approximately four-week period and one-twelfth of a planetary year are both useful and now diverge. Marian retains Darian-like near-four-week cadence **without giving up** a twelve-month annual coordinate. The question is whether two clearly assigned labels cost less than forcing one label to carry two incompatible functions. Marian's case is strong for institutions with multi-horizon planning, though the extra vocabulary is a real cost.

**Objection 3: “This is just Levitt with Darian months inside it.”** The ancestry is essentially right at the level of the 668-sol partition, and Marian should say so. The more relevant test is whether the *explicit layered operating architecture*—twelve annual months, 24 minths, six Sixths, canonical data identities, interplanetary phase orientation and a full open conformance record—forms a usable and independently implementable civil system. Combining and evaluating prior ideas can be an original contribution without claiming novelty for each ingredient.

**Objection 4: “Ls = 0° is a more natural Martian New Year.”** It is a perfectly sound candidate. Marian favours Ls = 15° because its intended design brief includes an early Earth-connected society, for which a near-common heliocentric annual direction offers an additional heuristic. That pragmatic advantage must be weighed against the explanatory simplicity and astronomical symbolism of an equinox; it is not objectively superior for every future Mars.

**Objection 5: “The month-gap light-time story is misleading.”** It would be if offered as a flight-operations number. The evidence establishes an approximate *distributional* monotone association in the synthetic model; neighbouring categories overlap substantially. Marian's published text should lead with those constraints, avoid exact predictions, and always defer operations to ephemeris-based OWLT. The defensible added value is a mental model, not precision.

**Objection 6: “The calendar is harder to teach because it adds terms.”** It adds two useful terms and avoids making 'month' and 'quarter' do two unrelated jobs. Its numeric identities and optional culturally selected names can make the formal system easy to translate and inspect. This is plausible, not experimentally proven; a future Mars usability study should compare Darian and Marian learning time, error rate, scheduling comprehension and user preference directly.

**Objection 7: “Darian already works. Openness cannot make another calendar better.”** Correct that openness cannot change astronomical arithmetic or human taste. It **can** reduce legal and technical barriers to building interoperable software, checking compatibility and revising errors. Marian should be judged on the combination of operating architecture and verifiable implementation, not on an unsupported claim that no one has made open Darian software.

## Comparative summary

| Question | Darian | Marian | Fair assessment |
|---|---|---|---|
| Primary annual divisions | 24 short months | 12 months plus 24 formal minths | Marian exposes both scales; Darian protects shorter primary month duration |
| Typical short operating period | 27–28 sol month | 27–28 sol minth | Similar underlying scale |
| Intermediate planning coordinate | Derivable from month groups | Six formally defined Sixths | Explicit Marian addition, value untested |
| Quarter fraction | Derivable | Four protocol-defined quarters | Marian gives visible 12-month grouping |
| Weekday labels | Selected short terminal weeks | Selected short terminal weeks | **Neither** solves continuous named-week objections |
| Annual reference | Ls = 0° | Ls = 15° | Different design brief, not universal win |
| Cross-world month-gap heuristic | Not primary original design objective | Explicitly examined in synthetic model | Real but approximate and era-dependent |
| Naming | Multiple historic month-name systems | Canonical numeric identities; optional human labels | Marian may be easier to localise; no user-study proof |
| Release/licensing in this project | Public Darian literature and independent implementations exist | Versioned CC BY technical standard + Apache reference code planned | Compare particular artifacts, not caricatures |
| Human cultural ownership | Naming variants exist | Explicit permission for future local names | Both have adaptability; Marian formalises decoupled IDs |

## Conclusion: the affirmative case for Marian

The strongest case for Marian is not 'Darian got Mars wrong'. Darian helped establish that Martian civil time can have perpetually aligned dates and short recurring periods; its legacy is part of the foundation. **Marian asks a broader operating question:** can the same annual sequence simultaneously provide a twelve-month annual map, a twenty-four-period short cadence, a meaningful mid-range scale, transparent machine identities and a modest Earth-facing orientation advantage—while remaining reproducible, openly specified and adaptable to future Martian language?

On the current evidence, **yes by construction for the structural properties**; **yes conditionally, in the tested model, for coarse orbital-phase legibility**; and **plausibly, but not yet proven, for easier adoption and institutional use**. That is a substantial and defensible argument for Marian as a serious successor architecture in the Levitt–Darian lineage, without denying the genuine costs of its interrupted civil week or appropriating the cultural choices of people who do not yet live on Mars.

### Sources and pending checks

- JB Bullock, *The Marian Calendar: Design and Evaluation of a Civil Time Architecture for Mars*, September 2026 author preprint, especially §§2.3–2.4, 6.4, 7.5–7.7 and 8.1–8.9. **Private source reference; not a claim of journal acceptance.**
- Ratified *Marian Protocol v1.0*, integer audit and research provenance (private M6a baseline).
- Thomas Gangale, *The Darian Calendar* (1998), https://marspapers.org/paper/MAR98095.pdf (reviewed primary description; copyright notice retained).
- Thomas Gangale, *Expanding the Cultural Relevance of the Darian Calendar of Mars to East Asia* (2025), publication copy and copyright to be verified before final citation.
- Additional peer-review check: Darian’s current licence map, month naming alternatives and external code conformance have not been exhaustively audited. Do not claim otherwise.

---

### M6c source verification notes (editorial annex)

These notes document source provenance and do not alter the author-approved analysis. The normative Marian Protocol v1.0 is held in the separate, frozen technical repository; the link must be set to the real public URL at release. The following primary and official sources were checked for the specific facts attributed to them:

- Thomas Gangale, *The Darian Calendar* (1998), [original proposal](https://marspapers.org/paper/MAR98095.pdf): 24 months, 27/28-sol variation and shortened terminal weeks.
- Thomas Gangale, *The Architecture of Time, Part 2: The Darian System for Mars* (2006), [SAE technical paper](https://doi.org/10.4271/2006-01-2249): publication and system overview.
- Josef Šurán, *A Calendar for Mars* (1997), [journal record](https://doi.org/10.1016/S0032-0633(97)00033-0): leap/skip-day and leap/skip-week approaches.
- NASA GISS, [Mars24 calculation documentation](https://www.giss.nasa.gov/tools/mars24/help/algorithm.html), updated 2025: official mean-sol and seasonal-coordinate reference.
- Thomas Gangale, [Darian adaptations for East Asian cultural nomenclature](https://www.researchgate.net/publication/390729531_Expanding_the_Cultural_Relevance_of_the_Darian_Calendar_of_Mars_to_East_Asia) (2025): additional names should not be misrepresented as nonexistent.

**Source limitation:** the 1954 Levitt work is credited through the author's research preprint and historical discussion rather than a newly inspected 1954 scan. The 2031–2120 Earth–Mars OWLT figures come from JB Bullock's archived September 2026 research preprint; M6c reconciles the quotations against that manuscript but does not rerun its 32,872-observation simulation or make the preprint public. External re-evaluation requires release or equivalent reproduction of the corresponding research methods/data. None of these limitations alters the verified integer-calendar rules.

