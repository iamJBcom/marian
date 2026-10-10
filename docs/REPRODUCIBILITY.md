# Reproducibility and integrity

There are two independent integrity scopes:

1. `protocol/SHA256SUMS.txt` records the **exact frozen** author-ratified v1.0 source files; all those bytes are preserved inside this M4b repository candidate.
2. Root `SHA256SUMS.txt` records **all M4b packaged content**, including unratified explanatory documentation. New root checksums do not modify the frozen protocol's recorded hashes.

Prerequisites: a compatible Python 3 installation, Node.js and the Python packages `jsonschema` and `PyYAML`. In a connected test environment install with `python -m pip install 'jsonschema>=4.21,<5' 'PyYAML>=6,<7'`; once installed, the verification itself requires no network. The prepared CI workflow installs them but has no deployment steps.

Run the complete checks from the repository root:

```sh
python protocol/tools/verify_release.py
cd protocol/reference-conformance
python tools/verify_checksums.py
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python conformance/verify_vectors.py
node js/verify.mjs
cd ../..
python scripts/verify_repository.py
```

Tests available offline: 29 Python tests, 66,859 first-century date-oracle records, 81 positive and 24 negative conformance vectors, an independently written Node.js implementation, file hashes and Markdown/document-catalogue checks.

**Scope:** these are calendar and packaging tests. They do **not** verify actual future epoch timestamps, JPL SPICE data, Mars photometry, observed mean-solar rotation or civil-adoption claims. `research/` holds selected original M2 historical reports, clearly designated non-normative and model-specific.

See [full source evidence chain](../protocol/governance/SOURCE-EVIDENCE-CHAIN.md), [freeze verification](../protocol/evidence/M3c-final-test-report.md) and [the conformance guide](../protocol/reference-conformance/docs/CONFORMANCE.md).
