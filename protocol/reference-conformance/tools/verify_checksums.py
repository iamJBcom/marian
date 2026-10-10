# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Verify SHA256SUMS.txt relative to this package root; skips manifest itself."""
from pathlib import Path
import hashlib,sys
root=Path(__file__).resolve().parents[1]
manifest=root/'SHA256SUMS.txt'
if not manifest.exists():
    print('MISSING checksum manifest')
    sys.exit(1)
count=0
for line in manifest.read_text().splitlines():
    if not line.strip():continue
    try: digest,name=line.split('  ',1)
    except ValueError:raise SystemExit('Malformed checksum line')
    path=root/name
    if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=digest:
        raise SystemExit(f'FAIL SHA256 {name}')
    count+=1
print(f'PASS {count} M3b content-file SHA256 checks')
