# Marian Protocol v1.0 — Reproducible CORE-DATE conformance procedure

**Claim permitted after passing:** "Marian Protocol v1.0 CORE-DATE reference conformance tests passed (suite and revision identified)."  
**Claims not permitted:** "official MY1 epoch", "astronomically SPICE-verified", or "UTC timestamps can be computed."

## Test evidence hierarchy

1. **Frozen independent known-answer oracle:** the verbatim M2a `M2a-first-century-oracle.csv`, SHA-256 embedded in `M3b-conformance-vectors.json`, with every sequential sol from MY1-S001 through MY100-S668. It was created at M2a, before the M3b implementations. Its evidence is independent of both M3b Python and JavaScript source code.
2. **Finite test vectors:** 81 positive cases derived only from the frozen M2a oracle, plus 24 negative/error cases based on the ratified v1.0 interchange grammar and validity rules. `conformance/build_m3b_vectors.py` documents construction, and `conformance/verify_vectors.py` does not regenerate the values when testing.
3. **Python independent checks:** `tests/test_core.py`, including leap-year distributions across multiple centuries, rollover, 100-year whole-ledger enumeration, very large years, type rejection, schema checks, JSON CLI and uninstantiated epoch handling.
4. **Independent language:** `js/marian-core.mjs` uses `BigInt` for exact year and offset arithmetic, independently written from the draft equations. `js/verify.mjs` consumes the pre-existing M2a oracle and checks all 66,859 records.

## Standard reproduction commands

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python conformance/verify_vectors.py
node js/verify.mjs
python tools/verify_checksums.py
```

Expected core result: every test passes, and every one of the 66,859 first-century records agrees. Separate clocks and astronomical ephemerides must not be inferred from these tests.

## Mandatory coverage

- Century leap frequency 59/100, exact 66,859-sol block, and cyclic year-100 exception.
- Common and leap templates, minth splitting, quarters/Sixths crosscutting, 96 nominal week slots.
- Absent terminal D7 in 55-sol months, continuous physical-sol count, identical weekday labels for valid recurring dates.
- 1-based year-local ordinal to civil and reverse; 0-based absolute ordinal-sol offset to civil and reverse.
- Exact month and year rollovers, including MY100→MY101.
- MY1, MY2, MY10, MY50, MY99, MY100, MY101, MY1000 and large year identifiers (>2^53).
- Strict v1.0 interchange syntax; valid/invalid and schema-versus-semantic-validity distinctions.
- No silent absolute timestamps; `UNINSTANTIATED_EPOCH` for requested real absolute-time conversion.

## Out-of-scope matters

No SPICE kernel execution, Ls=15° high-precision crossing determination, human-first-step historical evidence, MY0 subsol civil-date system, TT/TDB conversion, future UTC rule, or institutional adoption. These remain separate proof obligations. The prepared GitHub workflow has not been executed; passing local tests does not prove CI performance on GitHub hosts.

## Independent test integrity

- Do **not** regenerate oracle expectations from the software under test; keep prior frozen M2a oracle byte-for-byte.
- If changing any fixture, assign a new fixture version, rerun both language tests, and preserve prior checksum/provenance.
- Do **not** infer the calendar's real astronomical drift from comparison of an arithmetic 668.590000-sol century cycle with a constant idealised year.
- Neither a future version number nor a schema success alone should confer ratified conformity.
