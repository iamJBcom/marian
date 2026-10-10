# Marian Protocol v1.0 — versioning and change control

Three separately identified layers are established:

1. **Civil rules:** `marian-civil-v1.0`, exact year/date arithmetic, immutable 59/100 intercalation, date grammar, error vocabulary and JSON interchange.
2. **Reference clock profile:** `MARIAN-AIRY-AMT-MARS24-2025-01-07-v1`, reproducible, TT-based Airy Mean Time definition. Author ratification does **not** imply a future measured Mars rotation series.
3. **Epoch certificate:** a distinct, authenticated future record supplying first step H, qualifying Ls=15° crossing C and initial MY1 midnight E. **No certificate exists today.**

A revision affecting canonical date semantics or epoch choice MUST introduce a new versioned identity with migration and conformance proof; must not silently relabel existing archived dates. Minor editorial errata MAY be announced separately without changing the normative v1.0 artifact. Reproduce the ZIP SHA-256 and file manifest before every republication; derived distributions must indicate modifications as applicable under their respective licenses.

This author-ratified document is **not** Martian governmental adoption, a published DOI, or a future authority's epoch certificate. `M2c1` SPICE verification remains an optional future precision improvement, not a retroactive completed proof.
