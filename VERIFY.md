# Reproduction and integrity checks (offline)

Run in the technical export root:

```sh
python protocol/tools/verify_release.py
python protocol/reference-conformance/tools/verify_checksums.py
PYTHONPATH=protocol/reference-conformance/src python -m unittest discover -s protocol/reference-conformance/tests -q
PYTHONPATH=protocol/reference-conformance/src python protocol/reference-conformance/conformance/verify_vectors.py
node protocol/reference-conformance/js/verify.mjs
python tools/verify_clean_export.py
```

`SHA256SUMS.txt` covers all export files except itself. The original frozen protocol maintains its own historical checksums independently.
