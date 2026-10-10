#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
from pathlib import Path
import hashlib, json
R=Path(__file__).resolve().parents[1]
manifest=R/'SHA256SUMS.txt'
entries={}
for row in manifest.read_text().splitlines():
  sha,path=row.split('  ',1)
  assert path not in entries
  entries[path]=sha
actual={p.relative_to(R).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in R.rglob('*') if p.is_file() and p!=manifest and '.git' not in p.parts and '__pycache__' not in p.parts and p.suffix!='.pyc'}
assert actual==entries, f'Clean-export file inventory mismatch: {set(actual)^set(entries)}'
proto=json.loads((R/'protocol/MANIFEST.json').read_text());assert proto
assert len([p for p in (R/'protocol').rglob('*') if p.is_file() and p.suffix!='.pyc'])==59
assert len(list((R/'companions').glob('*.md')))==3
print('PASS clean-export manifest:',len(entries),'checksummed files; unchanged 59-file frozen protocol; 3 companions')
