# Marian Protocol v1.0 — CORE-DATE Machine API

## Overview

The reference Python implementation is importable as `marian_protocol`. `CivilDate(Y,M,W,D)` is an immutable, validated value. `CivilDate.canonical` returns `MY42-08-03-05`; `.ordinal_string` returns `MY42-S409`; `.offset` returns a Python exact integer. `evaluate(request)` is a stateless JSON-compatible command API and never returns floating-point sol offsets.

The author-ratified v1.0 wire identifier is `marian-civil-v1.0`. All request objects are exact shape: extra fields are rejected. JSON Lines mode reads one command per nonblank line and emits one reply per line. Always inspect `ok` before reading `data`.

### Operations

| `action` | Required fields | `data` / behaviour |
|---|---|---|
| `parse_civil` | `civil` string | date/ordinal/offset/derived fields |
| `parse_ordinal` | `ordinal` string | same |
| `from_ordinal` | `year` decimal string; `ordinal_sol` integer | same |
| `from_offset` | `offset_sols` decimal string | same |
| `validate_civil_object` | `date` civil JSON object | same |
| `validate_ordinal_object` | `date` ordinal JSON object | same |
| `year_info` | `year` decimal string | leap status, counts, 12/24/4/6 partitions |
| `absolute_time` | no additional fields | `UNINSTANTIATED_EPOCH` (always; real bridge not yet defined) |

### Successful example

Request:

```json
{"action":"parse_civil","civil":"MY42-08-03-05"}
```

Response (pretty-printed; key order is not part of the protocol):

```json
{
  "ok": true,
  "rule_version": "marian-civil-v1.0",
  "data": {
    "date": {"calendar":"marian","rule_version":"marian-civil-v1.0","year":"42","month":8,"week":3,"day":5},
    "civil": "MY42-08-03-05",
    "ordinal": "MY42-S409",
    "ordinal_sol": 409,
    "offset_sols": "27821",
    "derived": {"minth":15,"quarter":3,"sixth":4,"nominal_week_of_year":59,"position_in_month":19,"weekday_name_english":"Frisol"}
  }
}
```

### Rejection example

```json
{"action":"parse_civil","civil":"MY2-03-08-07"}
```

```json
{"ok":false,"rule_version":"marian-civil-v1.0","error":{"code":"INVALID_DATE","message":"this terminal Sunsol is absent from a 55-sol month"}}
```

The `message` text is for people and may evolve; the normative `code` is the stable machine discriminator if ratified. Normative v1.0 error identifiers include `SYNTAX_ERROR`, `INVALID_DATE`, `UNSUPPORTED_YEAR`, `NEGATIVE_OFFSET`, `UNINSTANTIATED_EPOCH`, `UNRATIFIED_CLOCK_PROFILE`, `UNCERTAIN_BOUNDARY`, and `UNSUPPORTED_PROFILE`. Some are reserved for future clock implementations and are not emitted by this integer-only CLI.

### Numerical safety

The JSON year field is a **string**, not a JSON integer. Long offsets are also strings. A JavaScript consumer MUST convert to `BigInt`, not `Number`. The reference Python code avoids floating point altogether. Runtime-specific resource limits for exceptionally long input strings are implementation limits, not calendar limits.

A JSON Schema shape is **not** a date-validity algorithm. A well-formed `MY2-03-08-07` can satisfy a basic schema while still being a nonexistent Marian date. A parser and semantic validator are required to check weekday positions and leap years.

### Errors and scope

- An invalid canonical string receives `SYNTAX_ERROR` (e.g. padded year or lowercase prefix).
- A valid string describing a nonexistent date receives `INVALID_DATE` (e.g. missing Sunsol).
- A regular date with year zero is not supported. In canonical strings `MY0` is rejected at syntax level; in Python numeric constructors it is `UNSUPPORTED_YEAR`.
- Negative Python sol offsets receive `NEGATIVE_OFFSET`. Negative offset strings are not canonical and are rejected with `SYNTAX_ERROR` by the JSON interface.
- Actual Gregorian/UTC/TT timestamp requests return `UNINSTANTIATED_EPOCH`. No synthetic epoch is an official timestamp.

### API stability

This is the **author-ratified Marian v1.0 CORE-DATE wire profile**, frozen on 8 October 2026. Backward-incompatible future changes require a new identifier. This CLI does not implement the real-time EPOCH-ADAPTER, because no authenticated future founding epoch currently exists.
