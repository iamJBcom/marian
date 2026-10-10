# M3b verification report — 8 October 2026

**Milestone:** Marian Protocol v1.0 reference implementation and machine-readable conformance suite, **DRAFT**.  
**Calendar:** *Marian: An Operating Calendar for Human Mars* (JB Bullock).

## Local evidence — executed

| Check | Result | Recorded output |
|---|---|---|
| Python `unittest` core + API + schema tests | **PASS: 29/29** | `reports/M3b-python-tests.txt` |
| Python first-century M2a frozen-oracle verification | **PASS: 66,859 / 66,859** | `reports/M3b-oracle-test.txt` |
| Finite positive machine vectors | **PASS: 81** | `reports/M3b-oracle-test.txt` |
| Negative/error vectors | **PASS: 24** | `reports/M3b-oracle-test.txt` |
| Independent Node.js `BigInt` first-century M2a frozen-oracle verifier | **PASS: 66,859 / 66,859** | `reports/M3b-node-oracle-test.txt` |
| Long integer year/sol offsets (`10^18` and higher) | **PASS in Python and Node** | Python tests 11/12; Node verifier |
| Strict schema/request/response and invalid year-specific dates | **PASS** | Python tests 22, 25–29 |
| Python offline package wheel construction/local isolated installation | **PASS** | `reports/M3b-local-install-test.txt` |
| Real absolute-time conversion | **Safely unavailable**: `UNINSTANTIATED_EPOCH` | Python tests 19,21 |

The prior independent M2a oracle was **copied byte-for-byte**, its SHA-256 frozen in the M3b finite vectors. It was not generated from either M3b implementation. The Python and JavaScript implementations are distinct source-code paths and both read the prior M2a ledger.

## Limits of what was proven

Passing these tests supports candidate **CORE-DATE integer and wire-format implementation**, not a claim of official institutional adoption or astronomical completeness. No JPL SPICE kernel result, official future first human step `H`, future Ls crossing `C`, or actual Airy-0 epoch `E` was introduced. The four M2c2 proposed conventions and M3a API/rights decisions remain pending ratification. The clock adapter is not activated in this package.

A Python 3.13 and Node 22 runtime were used in the local execution. Additional CI matrix versions appear only in the **unexecuted** draft GitHub Actions workflow. Local independent installation does not establish PyPI publication, GitHub CI execution, or future production readiness.

The final distribution archive undergoes a separate clean-extract rerun before handoff; its result is recorded in the accompanying final delivery answer, not retroactively asserted here.
