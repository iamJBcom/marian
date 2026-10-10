# Marian Protocol v1.0 — Reference CORE-DATE implementation

**Work:** *Marian: An Operating Calendar for Human Mars*, JB Bullock  
**Normative document:** `../spec/MARIAN-PROTOCOL-v1.0.md`  
**Civil-rule identifier:** `marian-civil-v1.0`  
**State:** **AUTHOR-RATIFIED / NORMATIVELY FROZEN**, 8 October 2026. **Not publicly published, institutionally adopted or independently certified.**

Python 3.10+ and independent Node.js `BigInt` implementations of Marian's calendar; source-locked 66,859-row MY1–MY100 M2a oracle; 81 positive and 24 negative interchange vectors; schemas, JSONL API, tests, and a GitHub Actions workflow **not yet run remotely**. The Python core uses only the standard library (optional `jsonschema` validates schemas).

## Reproduce locally

```sh
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python conformance/verify_vectors.py
node js/verify.mjs
python tools/verify_checksums.py
```

## API example

```sh
PYTHONPATH=src python -m marian_protocol --request '{"action":"parse_civil","civil":"MY42-08-03-05"}'
PYTHONPATH=src python -m marian_protocol < examples/requests.jsonl
```

The command returns MY42-S409 and an exact zero-based sol offset. Years and offsets are unpadded ASCII decimal **strings** in JSON; smaller subdivisions are JSON integers. A nonexistent terminal Sunsol is rejected. The exposed machine wire version is `marian-civil-v1.0`.

The CLI's `absolute_time` action must return `UNINSTANTIATED_EPOCH`, not invent a founding timestamp. The author-ratified AMT reference-profile **definition** does not amount to historical instantiation or a certified, executable real-epoch adapter.

## Evidence, permissions and limitations

- Source-locked core mathematics exact (M2a); independently written Python and JavaScript oracle verifiers agree in local tests.
- Astronomical support conditional (Mars24 and Moshier models); no independent SPICE kernel execution.
- No recognised future first human step (H), Ls=15° crossing (C) or MY1 midnight (E) currently exists.
- Author expressly ratified D01–D10 on 8 October 2026, including the CC BY 4.0 technical-documentation and Apache-2.0 original-code permissions. Exact directory/file scope in `../LICENSES/README.md`.
- Literary book/illustrations remain all-rights-reserved and are not distributed here.
- Historical M3b results are archived at `../evidence/m3b-historical/` and describe their *original* draft stage; do not mistake them for current approval status.

See `docs/API.md`, `docs/CONFORMANCE.md` and `docs/RATIFICATION.md`.
