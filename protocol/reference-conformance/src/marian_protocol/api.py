# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Stateless v1.0 JSON request/response API for the M3b test harness.
All command outputs are deterministic JSON-compatible objects; offsets are strings.
"""
from __future__ import annotations
from .core import (CivilDate, MarianError, RULE_VERSION, derived, from_civil_object,
    from_ordinal_object, offset_to_civil, parse_civil, parse_ordinal,
    parse_nonnegative_decimal, parse_positive_decimal, ordinal_to_civil, year_profile)

ACTIONS = frozenset({"parse_civil","parse_ordinal","from_ordinal","from_offset",
                     "validate_civil_object","validate_ordinal_object","year_info","absolute_time"})

def _details(d: CivilDate) -> dict:
    return {"date": d.as_json(), "civil": d.canonical, "ordinal": d.ordinal_string,
            "ordinal_sol": d.ordinal, "offset_sols": str(d.offset), "derived": derived(d)}


def evaluate(request: object) -> dict:
    try:
        if not isinstance(request, dict) or set(request)-{"action","civil","ordinal","year","ordinal_sol","offset_sols","date"}:
            raise MarianError("SYNTAX_ERROR", "request must be a known JSON command object")
        action = request.get("action")
        if action not in ACTIONS:
            raise MarianError("SYNTAX_ERROR", "unknown action")
        expected = {"parse_civil":{"action","civil"},
                    "parse_ordinal":{"action","ordinal"},
                    "from_ordinal":{"action","year","ordinal_sol"},
                    "from_offset":{"action","offset_sols"},
                    "validate_civil_object":{"action","date"},
                    "validate_ordinal_object":{"action","date"},
                    "year_info":{"action","year"},
                    "absolute_time":{"action"}}[action]
        if set(request) != expected:
            raise MarianError("SYNTAX_ERROR", f"{action} requires exactly {','.join(sorted(expected))}")
        if action == "parse_civil": d = parse_civil(request["civil"])
        elif action == "parse_ordinal": d = parse_ordinal(request["ordinal"])
        elif action == "from_ordinal":
            d = ordinal_to_civil(parse_positive_decimal(request["year"]), request["ordinal_sol"])
        elif action == "from_offset":
            d = offset_to_civil(parse_nonnegative_decimal(request["offset_sols"]))
        elif action == "validate_civil_object": d = from_civil_object(request["date"])
        elif action == "validate_ordinal_object": d = from_ordinal_object(request["date"])
        elif action == "year_info":
            result = year_profile(parse_positive_decimal(request["year"]))
            return {"ok": True, "rule_version": RULE_VERSION, "data": result}
        else:
            raise MarianError("UNINSTANTIATED_EPOCH", "no authenticated MY1 epoch; absolute time conversion is unavailable")
        return {"ok": True, "rule_version": RULE_VERSION, "data": _details(d)}
    except MarianError as exc:
        return {"ok": False, "rule_version": RULE_VERSION,
                "error": {"code": exc.code, "message": str(exc)}}
    except (TypeError, ValueError, OverflowError) as exc:
        # Strict API input failure; never return a Python traceback for malformed requests.
        return {"ok": False, "rule_version": RULE_VERSION,
                "error": {"code": "SYNTAX_ERROR", "message": "invalid request value or type"}}
