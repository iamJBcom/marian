# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Verify the frozen Marian v1.0 release SHA256SUMS from repository root."""
from pathlib import Path
import hashlib
import sys
ROOT=Path(__file__).resolve().parents[1]
manifest=ROOT/'SHA256SUMS.txt'
files=[]
for line in manifest.read_text().splitlines():
 if not line: continue
 expected,name=line.split('  ',1)
 path=ROOT/name
 if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:
  raise SystemExit(f'FAIL: {name}')
 files.append(name)
print(f'PASS: {len(files)} v1.0 release file checksums')
