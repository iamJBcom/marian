# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Run M3b immutable M2a oracle and finite vectors using only the Python standard library.
Invoke from any current directory: python conformance/verify_vectors.py
"""
import csv
import hashlib
import json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from marian_protocol import CivilDate, evaluate, offset_to_civil, civil_to_offset, civil_to_ordinal


def main():
    vectors=json.loads((ROOT/'fixtures/M3b-conformance-vectors.json').read_text())
    oracle=ROOT/'fixtures/M2a-first-century-oracle.csv'
    assert hashlib.sha256(oracle.read_bytes()).hexdigest()==vectors['source_sha256']
    assert len(vectors['positive'])>=50, 'insufficient finite vectors'
    for item in vectors['positive']:
        d=CivilDate(int(item['year']),item['month'],item['week'],item['day'])
        assert (d.canonical,d.ordinal_string,str(d.offset),d.ordinal)==(item['civil'],item['ordinal'],item['offset_sols'],item['ordinal_sol']),item
        for action,key in [('parse_civil','civil'),('parse_ordinal','ordinal'),('from_offset','offset_sols')]:
            response=evaluate({'action':action,key:item[key]})
            assert response['ok'] and response['data']['civil']==item['civil'],response
    for item in vectors['negative']:
        response=evaluate(item['request'])
        assert not response['ok'] and response['error']['code']==item['error'],(item,response)
    count=0
    with oracle.open(newline='') as fh:
        for row in csv.DictReader(fh):
            o=int(row['offset'])
            d=offset_to_civil(o)
            assert (d.canonical,d.ordinal_string,d.ordinal)==(row['canonical_civil'],row['canonical_ordinal'],int(row['ordinal'])),o
            assert civil_to_offset(d)==o
            assert civil_to_ordinal(d)==int(row['ordinal'])
            count+=1
    assert count==66859
    print(f'PASS M3b conformance: {count} independent M2a oracle sols; {len(vectors["positive"])} finite positive and {len(vectors["negative"])} error vectors')
    return 0

if __name__=='__main__':sys.exit(main())
