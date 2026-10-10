# M3b source and test traceability

| Implemented functionality | M3a governing clause | Original manuscript | Reproducible evidence |
|---|---|---|---|
| Leap predicate & 59/100 | §§4,12 | Appendix A, C, D | M2a oracle; Python test 01–03; Node verifier |
| 12 months, 24 minths | §§5–6 | Appendix A/B | Python test 04–05 |
| Nominal weeks, absent D7 | §7 | Appendix A, Ch.12, Appendix D | Python test 06, 09, 24; 66,859 sol oracle |
| Quarters, Sixths, derived fields | §§8,13 | Appendix A/B | Python test 05; source example |
| Civil/ordinal date representation | §§9–11 | Appendix D | M2a oracle; tests 07, 13–16 |
| Whole-sol offset algorithms | §12 | Appendix D | M2a oracle; Python + JavaScript; tests 10–12 |
| Canonical JSON shapes | §17 **ratified D05–D08** | Appendix D numerical identity | tests 15–18, 22–23; draft schemas |
| Error classes | §17 **ratified D05–D08** | Derived interoperability design | negative vectors; tests 15, 20, 23 |
| MY0 and clock gating | §§14–15 **ratified D01–D04/D06** | Appendix C/D | Python tests 19, 21; uninstantiated JSON template |
| Astronomical rationale | §16 **conditional** | Chapter 13–14, Appendix C | M2b/M2c1 scientific records; not M3b core proof |

## Provenance priority

1. Editor-approved source: `Marian - Calendar v06F - 2_10_2026.docx` supplied by author; book copyright reserved.
2. M2a independent structural audit, including original `M2a-first-century-oracle.csv` (copied unchanged into this package).
3. M3a normative specification **draft**, `MARIAN-PROTOCOL-v1.0-DRAFT.md` (not amended or ratified here).
4. M2c2 epoch-clock candidate (subsequently author ratified 2026-10-08); no real historical epoch.
5. M3b reference implementations and test vectors: implementation evidence, not a new authority on the calendar rules.

The `M3a` and `M2a` sources were used as local, verified inputs. Full copyrighted book text is deliberately absent from this author-frozen archive.
