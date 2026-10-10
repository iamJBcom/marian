# Marian Protocol v1.0 — Final author-freeze acceptance test record

**Evidence date:** 8 October 2026  
**Record type:** Local reproducible software test evidence. No independent certification or remote GitHub Actions run.

| Check | Actual result |
|---|---|
| Python `unittest` suite | **29 / 29 PASS** |
| Frozen M2a oracle | **66,859 / 66,859 records PASS**, `MY1` through `MY100` |
| Finite conformance vectors | **81 positive + 24 negative cases PASS** |
| Independent Node.js BigInt oracle | **PASS**, all 66,859 first-century records; year boundaries and 10^18-year arithmetic |
| Frozen oracle unchanged | **PASS**, SHA-256 `22ab9b1384a23aea8d386e35eade49d0789e13f19740d9eb298e2efd52244c69` |
| Canonical wire ID | **PASS**, Python + JavaScript + JSON schemas use `marian-civil-v1.0` |
| Author D01–D10 register | **PASS**, ten approvals reflected; no historic H/C/E fabricated |
| License texts and scope | **PRESENT**, CC BY 4.0 and Apache-2.0 full texts plus path mapping |

No tests in this package constitute independent high-precision SPICE ephemeris proof, demonstration of Mars's future rotational clock accuracy, or real-time MY1 epoch bridge conformance. Prior synthetic M2c2 tests verified the candidate algorithm before its author ratification; no authenticated future H, C or E exists yet.

## Exact program outputs

```text
python -m unittest discover -s tests -v: EXIT 0; OK
python conformance/verify_vectors.py: EXIT 0; PASS M3b conformance: 66859 independent M2a oracle sols; 81 finite positive and 24 error vectors
node js/verify.mjs: EXIT 0; PASS Node BigInt independent oracle: 66859 first-century sols; transitions, edge years and 10^18-year arithmetic
```

The original M3b draft reports are preserved under `evidence/m3b-historical/` with their historical state unmodified. See the final checksums/ZIP verification record for archive-level evidence.
