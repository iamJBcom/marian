# M2a — Findings, issues and specification-closure register

**Verdict:** **PASS** for the regular-year integer structure and tested conversions; **NOT a PASS** for the astronomical/epoch or publication system.

## Verified technical properties

The calendar structure in Appendix A and the integer algorithms in Appendix D agree for the tested MY1+ domain. In particular: 59 leap/100; terminal W8 D7 present in M12 only in leap years, absent in M3/6/9 every year; no physical sol skipped; start offsets continuous and invertible; same month/week/day coordinate has the same weekday position when valid; civil dates cover 668 or 669 physical sols according to year type. The example `MY42-08-03-05 = MY42-S409` passed.

## Explicit source and implementation gaps — do not silently change canon

| ID | Priority | Finding | Suggested closure |
|---|---|---|---|
| M2a-01 | MEDIUM | Appendix D.14 inverse ordinal pseudocode does not explicitly reject `Y < 1` before checking year length; Appendix D.11 does reject it for civil validation. | Add an explicit MY1+ domain precondition to every public integer function; keep MY0 separate. |
| M2a-02 | MEDIUM | Appendix D.19 proposes `floor(offset/668.59)+1` as an **initial estimate**, corrected by exact civil boundaries. Floating-point conversion can lose precision/overflow for sufficiently large offsets and is unnecessary. | Specify integer-only inverse as recommended or normative algorithm; leave floating estimation non-normative only if explicitly bounded. |
| M2a-03 | MEDIUM | The positive year syntax does not prescribe whether `MY042` is accepted as an alias for `MY42` or rejected as noncanonical; semantics and error taxonomy are not fully defined. | M3 decision: define strict canonical serialization (suggest no padded year), optional lenient input parsing and explicit error classes. **Our fixture policy is provisional**. |
| M2a-04 | MEDIUM | MY0 has no regular 12-month/24-minth template and no defined public date string. Its future physical start depends on an unspecified recognized first-step event, so integer date conversion MUST reject MY0 regular tuples. | Treat MY0 encoding and mapping to absolute chronology as a separate future-epoch issue; never fabricate a date or epoch. |
| M2a-05 | HIGH (outside M2a) | The astronomical estimate ~668.590 sols and asserted physical tracking at `Ls=15°` are not verified by integer arithmetic; 100-year idealized offset of zero is **not** a real ephemeris result. | M2b: authoritative ephemeris model/timebase, solar-longitude definition, epoch placement, long-range uncertainty, drift / phase analysis. |
| M2a-06 | HIGH (outside M2a) | Absolute conversion to UTC, TAI, MSD, Gregorian dates cannot be tested without instantiated MY1 and defined Martian timebase/sol boundaries. | M2b/M2c: explicit epoch adapter contract and synthetic-epoch tests only. |
| M2a-07 | LOW | Appendix D.1 claims MY0 is treated in `D.18`, while the explicit MY0 section is `D.20`; D.18 instead defines the epoch-sol offset. | Correct the editorial cross-reference in future publication text, subject to author approval. |
| M2a-08 | LOW | Some cross-references in Appendix D describe Chapter 14 as the chapter defining canonical identities; Chapter 15 appears to be intended. | Editorial cross-reference review during M5; do not modify master DOCX silently. |
| M2a-09 | LOW | Source prose uses “96 nominal week positions”, which may be mistaken for 96 seven-sol elapsed weeks or 96 weekday labels. | Normative terminology: 96 **nominal weekly slots**, 92/93 complete 7-sol weeks and 4/3 six-position terminal weeks. Maintain explicit physical-sol vs civil-label distinction throughout AI and technical outputs. |
| M2a-10 | MEDIUM | The source allows a future rare long-period correction only through an explicitly versioned extension; no such correction is presently defined. | Keep v1.0 integer rules exact; any future correction requires separate versioned rules and conformance suite, not a hidden change to leap predicate. |

## Coverage limitations

The 66,859-row pass is exhaustive only for the **first century**. The leap pattern's century periodicity is separately demonstrated and exercised through MY1000; extremely large offsets were spot-tested rather than exhaustively enumerated. The mathematical bijection proof depends on arbitrary-precision exact integer arithmetic, stable rule version, and no pre-MY1 extension. Tests do not validate human social outcomes, comparative advantages over Darian, original-contribution priority or peer-reviewed publication status.

## Outcome for larger workflow

**M2a / integer architecture: PASSED.** Remaining items do not require changing the canonical week/intercalation architecture. Next precise operation is **M2b astronomical and epoch assumptions**, followed by normative closure of the M3 grammar/error details. The resulting technical specification may cite these test data only with the explicit scope limits above.
