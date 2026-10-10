# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Derive expected first-century examples ONLY from the frozen pre-M3b M2a oracle.
Does not import the M3b implementation; not intended to manufacture test passes.
"""
from __future__ import annotations
import csv, hashlib, json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root/'fixtures/M2a-first-century-oracle.csv'
selected={0,1,6,7,27,28,54,55,56,111,166,167,334,667,668,669,1336,1337,66858}
# Include first and last sol of representative years, all month boundaries and 100-year blocks.
rows=[]
with source.open(newline='') as fh:
    rd=csv.DictReader(fh)
    for row in rd:
        off=int(row['offset'])
        if off in selected or int(row['year']) in (1,2,10,42,99,100) and (
            int(row['ordinal']) in (1,28,29,55,56,57,111,167,168,408,409,668,669)):
            rows.append({'offset_sols':row['offset'], 'civil':row['canonical_civil'],
                         'ordinal':row['canonical_ordinal'],
                         'year':row['year'], 'month':int(row['month']),
                         'week':int(row['week']), 'day':int(row['day']),
                         'ordinal_sol':int(row['ordinal'])})

negative=[
  {'request':{'action':'parse_civil','civil':'MY2-03-08-07'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_civil','civil':'MY2-12-08-07'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_civil','civil':'MY1-03-08-07'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_civil','civil':'MY42-13-01-01'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_civil','civil':'MY042-08-03-05'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'parse_civil','civil':'my42-08-03-05'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'parse_civil','civil':'MY42-8-03-05'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'parse_civil','civil':'MY42-08-03-5'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'parse_civil','civil':'MY0-01-01-01'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'parse_civil','civil':'MY42-08-03-０５'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'parse_ordinal','ordinal':'MY2-S669'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_ordinal','ordinal':'MY42-S000'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_ordinal','ordinal':'MY42-S670'},'error':'INVALID_DATE'},
  {'request':{'action':'parse_ordinal','ordinal':'MY042-S409'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'from_offset','offset_sols':'-1'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'from_offset','offset_sols':'01'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'from_offset','offset_sols':1},'error':'SYNTAX_ERROR'},
  {'request':{'action':'from_ordinal','year':'0','ordinal_sol':1},'error':'SYNTAX_ERROR'},
  {'request':{'action':'from_ordinal','year':'2','ordinal_sol':669},'error':'INVALID_DATE'},
  {'request':{'action':'year_info','year':'0002'},'error':'SYNTAX_ERROR'},
  {'request':{'action':'absolute_time'},'error':'UNINSTANTIATED_EPOCH'},
  {'request':{'action':'validate_civil_object','date':{'calendar':'marian','rule_version':'wrong','year':'1','month':1,'week':1,'day':1}},'error':'UNSUPPORTED_PROFILE'},
  {'request':{'action':'validate_civil_object','date':{'calendar':'marian','rule_version':'marian-civil-v1.0','year':'2','month':3,'week':8,'day':7}},'error':'INVALID_DATE'},
  {'request':{'action':'validate_civil_object','date':{'calendar':'marian','rule_version':'marian-civil-v1.0','year':'1','month':True,'week':1,'day':1}},'error':'INVALID_DATE'},
]
fixture={
 'status':'Marian Protocol v1.0 AUTHOR-RATIFIED — frozen conformance vectors',
 'source':'Frozen M2a-first-century-oracle.csv, independently generated in M2a; negative cases are author-ratified v1.0 grammar/validity rules',
 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
 'positive':rows,'negative':negative,
 'identity_example':{'civil':'MY42-08-03-05','ordinal':'MY42-S409'},
 'notes':'These fixtures prove integer-date behaviour, not astronomy or a historical epoch.'}
(root/'fixtures/M3b-conformance-vectors.json').write_text(json.dumps(fixture,ensure_ascii=False,indent=2)+'\n')
print('positive',len(rows),'negative',len(negative),'source_sha256',fixture['source_sha256'])
