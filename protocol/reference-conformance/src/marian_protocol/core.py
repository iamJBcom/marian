# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Marian regular-year calendar core — v1.0 author-ratified implementation.

This code implements v1.0 ratified CORE-DATE semantics, MY1 and later only.
No Earth clock, astronomical ephemeris, landing epoch, or MY0 dates are assumed.
Author-ratified v1.0 core; the current package expressly licenses original code under Apache 2.0.
"""
from __future__ import annotations

from dataclasses import dataclass
import re

RULE_VERSION = "marian-civil-v1.0"
CYCLE_SOLS = 66859
CYCLE_YEARS = 100
WEEKDAY_NAMES = ("Monsol", "Tuesol", "Wedsol", "Thursol", "Frisol", "Satsol", "Sunsol")
DATE_RE = re.compile(r"MY([1-9][0-9]*)-([0-9]{2})-([0-9]{2})-([0-9]{2})\Z", re.ASCII)
ORDINAL_RE = re.compile(r"MY([1-9][0-9]*)-S([0-9]{3})\Z", re.ASCII)
UNPADDED_NONNEG = re.compile(r"(?:0|[1-9][0-9]*)\Z", re.ASCII)
UNPADDED_POS = re.compile(r"[1-9][0-9]*\Z", re.ASCII)

class MarianError(ValueError):
    """An error with a stable normative machine-readable identifier."""
    def __init__(self, code: str, message: str):
        self.code = code
        super().__init__(message)


def require_int(value: object, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise MarianError("INVALID_DATE", f"{name} must be an integer (not boolean)")
    return value


def require_year(year: object) -> int:
    y = require_int(year, "year")
    if y < 1:
        raise MarianError("UNSUPPORTED_YEAR", "regular Marian dates begin at MY1; MY0 is transitional")
    return y


def is_leap_year(year: int) -> bool:
    y = require_year(year)
    return y % 100 != 0 and (y % 2 == 1 or y % 10 == 0)


def year_length(year: int) -> int:
    return 669 if is_leap_year(year) else 668


def month_length(year: int, month: int) -> int:
    require_year(year)
    m = require_int(month, "month")
    if not 1 <= m <= 12:
        raise MarianError("INVALID_DATE", "month must be 1..12")
    return 55 if m in (3, 6, 9) or (m == 12 and not is_leap_year(year)) else 56


def minth_length(year: int, minth: int) -> int:
    require_year(year)
    n = require_int(minth, "minth")
    if not 1 <= n <= 24:
        raise MarianError("INVALID_DATE", "minth must be 1..24")
    return 28 if n % 2 else month_length(year, (n + 1) // 2) - 28


def leaps_in_first(n: int) -> int:
    require_int(n, "N")
    if n < 0:
        raise MarianError("INVALID_DATE", "N must be nonnegative")
    return (n + 1) // 2 + n // 10 - n // 100


def start_offset(year: int) -> int:
    y = require_year(year)
    return 668 * (y - 1) + leaps_in_first(y - 1)


def validate_date(year: int, month: int, week: int, day: int) -> None:
    require_year(year)
    for name, value, last in (("month", month, 12), ("week", week, 8), ("day", day, 7)):
        require_int(value, name)
        if not 1 <= value <= last:
            raise MarianError("INVALID_DATE", f"{name} must be 1..{last}")
    if (week - 1) * 7 + day > month_length(year, month):
        raise MarianError("INVALID_DATE", "this terminal Sunsol is absent from a 55-sol month")


@dataclass(frozen=True)
class CivilDate:
    year: int
    month: int
    week: int
    day: int

    def __post_init__(self):
        validate_date(self.year, self.month, self.week, self.day)

    @property
    def canonical(self) -> str:
        return f"MY{self.year}-{self.month:02d}-{self.week:02d}-{self.day:02d}"

    @property
    def ordinal(self) -> int:
        return civil_to_ordinal(self)

    @property
    def ordinal_string(self) -> str:
        return f"MY{self.year}-S{self.ordinal:03d}"

    @property
    def offset(self) -> int:
        return civil_to_offset(self)

    def as_json(self) -> dict:
        return {"calendar": "marian", "rule_version": RULE_VERSION,
                "year": str(self.year), "month": self.month, "week": self.week, "day": self.day}


def parse_civil(value: str) -> CivilDate:
    if not isinstance(value, str):
        raise MarianError("SYNTAX_ERROR", "civil date must be a string")
    m = DATE_RE.fullmatch(value)
    if not m:
        raise MarianError("SYNTAX_ERROR", "expected exact ASCII MY<year>-MM-WW-DD (unpadded year)")
    return CivilDate(*(int(s) for s in m.groups()))


def parse_ordinal(value: str) -> CivilDate:
    if not isinstance(value, str):
        raise MarianError("SYNTAX_ERROR", "ordinal date must be a string")
    m = ORDINAL_RE.fullmatch(value)
    if not m:
        raise MarianError("SYNTAX_ERROR", "expected exact ASCII MY<year>-SNNN (unpadded year)")
    return ordinal_to_civil(int(m.group(1)), int(m.group(2)))


def civil_to_ordinal(date: CivilDate) -> int:
    if not isinstance(date, CivilDate):
        raise MarianError("INVALID_DATE", "CivilDate instance required")
    return sum(month_length(date.year, m) for m in range(1, date.month)) + 7*(date.week-1) + date.day


def ordinal_to_civil(year: int, ordinal: int) -> CivilDate:
    y = require_year(year)
    n = require_int(ordinal, "ordinal")
    if not 1 <= n <= year_length(y):
        raise MarianError("INVALID_DATE", f"ordinal must be 1..{year_length(y)} for MY{y}")
    for m in range(1, 13):
        length = month_length(y, m)
        if n <= length:
            return CivilDate(y, m, (n - 1)//7+1, (n - 1)%7+1)
        n -= length
    raise AssertionError("ordinal calculation invariant violated")


def civil_to_offset(date: CivilDate) -> int:
    return start_offset(date.year) + civil_to_ordinal(date) - 1


def offset_to_civil(offset: int) -> CivilDate:
    o = require_int(offset, "offset")
    if o < 0:
        raise MarianError("NEGATIVE_OFFSET", "regular offset must be >= 0; MY0 has no regular offsets")
    # Exact 100-year decomposition. Each complete block consists of 66,859 sols.
    # Search only within the remaining 100 years; no floating-point calendar math.
    whole_cycles, _ = divmod(o, CYCLE_SOLS)
    base = whole_cycles * CYCLE_YEARS + 1
    low, high = base, base + CYCLE_YEARS
    while low + 1 < high:
        middle = (low + high) // 2
        if start_offset(middle) <= o:
            low = middle
        else:
            high = middle
    return ordinal_to_civil(low, o - start_offset(low) + 1)


def derived(date: CivilDate) -> dict:
    pos = 7*(date.week-1)+date.day
    return {"minth": 2*date.month - (1 if pos<=28 else 0),
            "quarter": (date.month-1)//3+1,
            "sixth": (date.month-1)//2+1,
            "nominal_week_of_year": 8*(date.month-1)+date.week,
            "position_in_month": pos,
            "weekday_name_english": WEEKDAY_NAMES[date.day-1]}


def year_profile(year: int) -> dict:
    y = require_year(year)
    return {"year": str(y), "is_leap": is_leap_year(y), "length_sols": year_length(y),
            "start_offset": str(start_offset(y)),
            "month_lengths": [month_length(y, m) for m in range(1,13)],
            "minth_lengths": [minth_length(y, n) for n in range(1,25)],
            "quarter_lengths": [sum(month_length(y,m) for m in range(3*q+1,3*q+4)) for q in range(4)],
            "sixth_lengths": [sum(month_length(y,m) for m in range(2*s+1,2*s+3)) for s in range(6)],
            "nominal_weeks":96, "short_terminal_weeks": 4-int(is_leap_year(y))}


def parse_positive_decimal(s: str, name: str="year") -> int:
    if not isinstance(s,str) or not UNPADDED_POS.fullmatch(s):
        raise MarianError("SYNTAX_ERROR", f"{name} must be an unpadded positive ASCII decimal string")
    return int(s)


def parse_nonnegative_decimal(s: str, name: str="offset") -> int:
    if not isinstance(s,str) or not UNPADDED_NONNEG.fullmatch(s):
        raise MarianError("SYNTAX_ERROR", f"{name} must be an unpadded nonnegative ASCII decimal string")
    return int(s)


def from_civil_object(obj: object) -> CivilDate:
    if not isinstance(obj,dict) or set(obj) != {"calendar","rule_version","year","month","week","day"}:
        raise MarianError("SYNTAX_ERROR", "civil object requires exactly calendar,rule_version,year,month,week,day")
    if obj["calendar"] != "marian" or obj["rule_version"] != RULE_VERSION:
        raise MarianError("UNSUPPORTED_PROFILE", "calendar or rule_version unsupported")
    return CivilDate(parse_positive_decimal(obj["year"]),obj["month"],obj["week"],obj["day"])


def from_ordinal_object(obj: object) -> CivilDate:
    if not isinstance(obj,dict) or set(obj) != {"calendar","rule_version","year","ordinal_sol"}:
        raise MarianError("SYNTAX_ERROR", "ordinal object requires exactly calendar,rule_version,year,ordinal_sol")
    if obj["calendar"] != "marian" or obj["rule_version"] != RULE_VERSION:
        raise MarianError("UNSUPPORTED_PROFILE", "calendar or rule_version unsupported")
    return ordinal_to_civil(parse_positive_decimal(obj["year"]),obj["ordinal_sol"])


def uninstantiated_epoch(*_args, **_kwargs):
    raise MarianError("UNINSTANTIATED_EPOCH", "no authenticated MY1 epoch certificate exists; absolute timestamp conversions disabled")
