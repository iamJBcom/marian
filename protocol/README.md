# Marian Protocol v1.0 — Author-Ratified Normative Freeze

**Work:** *Marian: An Operating Calendar for Human Mars*  
**Author:** JB Bullock  
**Author ratification:** 8 October 2026, D01–D10 approved unchanged  
**Civil rule ID:** `marian-civil-v1.0`  
**Clock profile ID:** `MARIAN-AIRY-AMT-MARS24-2025-01-07-v1`  
**Status:** **AUTHOR-RATIFIED / NORMATIVELY FROZEN**. No external repository upload, Zenodo deposit, ORCID work record, DOI or institutional adoption is asserted.

## Main documents

- `spec/MARIAN-PROTOCOL-v1.0.md` — complete 20-section normative protocol, including the exact civil-year and machine-interface rules plus future-epoch conventions.
- `author/AUTHOR-RATIFICATION.md` and `.json` record — attributable, unsigned conversational approval of all 10 M3c decisions.
- `governance/VERSIONING-AND-CHANGE-CONTROL.md` — three-layer versioning of civil rules, clock profile and future epoch certificate.
- `reference-conformance/` — Python + independent Node/BigInt date implementation, schema and exact test vectors.
- `evidence/M3c-final-test-report.md` — actual frozen-package test results and limits.
- `LICENSES/README.md` — explicit per-path CC BY 4.0 vs Apache-2.0 grants and exclusion of the book.
- `MANIFEST.json`, `SHA256SUMS.txt` — final integrity/provenance data.

## Independent local reproduction

```sh
cd reference-conformance
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python conformance/verify_vectors.py
node js/verify.mjs
python tools/verify_checksums.py
```

**CORE-DATE** can be implemented and tested today. **EPOCH-ADAPTER** has an author-ratified mathematical convention and versioned AMT clock definition but remains **uninstantiated** pending a historical first human step and authenticated epoch certificate. The `absolute_time` command deliberately reports `UNINSTANTIATED_EPOCH`.

The claim of 668.590000 sols refers to the exact *civil mean*; archaeological, scientific and astronomical realisations are separate. M2b/M2c1 analytically corroborated the approximate seasonal recurrence, but **no independent SPICE-kernel verification was completed**.

The all-rights-reserved literary book, cover and illustrations are not distributed in this package. Publication to GitHub or Zenodo is a later distinct action.
