# External authorities and technical source references

This bibliography identifies public standards and published equations used in the *technical discussion*, **not** scientific endorsement or an authorization to redistribute third-party content. The frozen normative Marian v1.0 package is unchanged. The URLs below were examined for this M4b audit on **8 October 2026**; online availability may later change.

| Source | Relevant use | Evidence/limits |
|---|---|---|
| [NASA GISS Mars24: Algorithm and Worked Examples](https://www.giss.nasa.gov/tools/mars24/help/algorithm.html) (document updated 2025-01-07) | Mars24 mean-time reference and analytic Mars solar-longitude calculation | Provides published equations and verification examples; **not** an independent Marian ephemeris certification. |
| [NAIF SPICE Toolkit documentation](https://naif.jpl.nasa.gov/naif/toolkit.html) | Future independently reproducible high-precision solar-longitude study | SPICE kernel-backed Marian crossings **were not executed**; M2c1 preparation does not count as observational verification. |
| [Citation File Format schema guide v1.2.0](https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md) | Root `CITATION.cff` metadata contract | Top-level `type` is `software` or `dataset`; a standard may be represented as `preferred-citation` with `type: standard`. |
| [GitHub citation-file documentation](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-citation-files) | Future citation-display compatibility | Merely preparing `CITATION.cff` does **not** constitute a publication. |
| [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/legalcode) | Identified author-owned technical documents | Grants cover designated works, not the separate book, artwork or third-party scientific sources. |
| [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) | Identified original code and workflow files | Does not license other copyrighted works or guarantee third-party rights. |

### Scientific evidence hierarchy

The M2b NASA Mars24 and M2c1c Swiss/Moshier numerical results are documented in the [science limitations](SCIENCE-AND-UNCERTAINTY.md), [research provenance](RESEARCH-PROVENANCE.md) and their intact historical reports. They are model comparisons over a specified historical interval, not independent JPL SPICE-kernel results, proof of long-term drift, or an actual future founding epoch.

Citation records in this repository do **not** invent author ORCID identifiers, publication years, DOIs, institutional affiliations or public repository URLs. The 2026-10-08 date describes author ratification and internal preparation, not publication.
