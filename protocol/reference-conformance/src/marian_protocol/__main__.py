# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Command line interface: one request JSON per line or one inline request."""
import argparse
import json
import sys
from .api import evaluate
from .core import RULE_VERSION

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Marian Protocol v1.0 CORE-DATE JSON command tool")
    parser.add_argument("--request", help="one JSON request object; omit for JSONL stdin streaming")
    args = parser.parse_args(argv)
    values = [args.request] if args.request is not None else sys.stdin
    found_error = False
    for raw in values:
        if not raw.strip():
            continue
        try:
            req = json.loads(raw)
            result = evaluate(req)
        except (json.JSONDecodeError, ValueError):
            result = {"ok": False, "rule_version":RULE_VERSION,
                      "error":{"code":"SYNTAX_ERROR","message":"invalid JSON request"}}
        found_error = found_error or not result["ok"]
        print(json.dumps(result, separators=(",",":"),ensure_ascii=True,sort_keys=True))
    return 2 if found_error else 0

if __name__ == "__main__":
    sys.exit(main())
