# Getting started with Marian CORE-DATE

No astronomic data or internet access is required to compute valid regular Marian dates for **MY1+**. Use Python 3.10+ and/or a modern Node.js installation. These commands are relative to this repository candidate's root.

The JSON Schema and repository metadata checkers use Python packages `jsonschema` and `PyYAML` respectively. Install these before running the complete suite (`python -m pip install 'jsonschema>=4.21,<5' 'PyYAML>=6,<7'`), or use an environment that already includes them. These dependency installs are not part of Marian's calendar mathematics.

## Run tests

```sh
cd protocol/reference-conformance
PYTHONPATH=src python -m unittest discover -s tests -v
PYTHONPATH=src python conformance/verify_vectors.py
node js/verify.mjs
python tools/verify_checksums.py
```

## Try the JSON Lines API

From `protocol/reference-conformance/`:

```sh
printf '%s\n' '{"action":"parse_civil","civil":"MY42-08-03-05"}' | PYTHONPATH=src python -m marian_protocol
```

The response has `ok: true`, `rule_version: "marian-civil-v1.0"`, an ordinal `MY42-S409`, and decimal-string `offset_sols: "27821"`. If trying `MY2-03-08-07`, expect `ok: false`, `INVALID_DATE` because the final Sunsol does not occur in a 55-sol month.

For **year** and **absolute sol offset** values in JSON, use *canonical decimal strings*, not JavaScript floating-point numbers. The separately written JavaScript implementation uses `BigInt`.

## Understand the boundary

The `absolute_time` action is intentionally **not enabled**: it returns `UNINSTANTIATED_EPOCH`. The rule for the future MY1 epoch is author-ratified, but the necessary first human step has not occurred. A real Earth-time conversion requires an authenticated epoch certificate plus appropriate clock/time-scale handling.

Next: [API reference](../protocol/reference-conformance/docs/API.md) · [Conformance](../protocol/reference-conformance/docs/CONFORMANCE.md) · [full specification](../protocol/spec/MARIAN-PROTOCOL-v1.0.md).
