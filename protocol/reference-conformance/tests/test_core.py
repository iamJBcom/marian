# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Source-anchored M3b unit, interoperability and negative tests (stdlib unittest)."""
import csv
import hashlib
import json
import subprocess
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from marian_protocol import (CivilDate, MarianError, evaluate, is_leap_year, year_length,
   month_length, minth_length, start_offset, offset_to_civil, parse_civil, parse_ordinal,
   ordinal_to_civil, derived, from_civil_object, from_ordinal_object)

VECTORS=json.loads((ROOT/'fixtures/M3b-conformance-vectors.json').read_text())
M3A=json.loads((ROOT/'fixtures/M3a-golden-vectors.json').read_text())

class TestMarianM3bCore(unittest.TestCase):
    def test_01_leap_golden_years(self):
        for y,expected in M3A['leap_years'].items():
            self.assertIs(is_leap_year(int(y)),expected)
    def test_02_leap_exact_every_century(self):
        for first in (1,101,901,1001,10**6+1,10**12+1):
            self.assertEqual(sum(is_leap_year(y) for y in range(first,first+100)),59)
            self.assertEqual(sum(year_length(y) for y in range(first,first+100)),66859)
    def test_03_offsets_from_prior_goldens(self):
        for y,offset in M3A['year_start_offsets'].items():
            self.assertEqual(start_offset(int(y)),offset)
    def test_04_all_year_templates(self):
        for y in (1,2,99,100,101):
            ml=[month_length(y,m) for m in range(1,13)]
            self.assertEqual(sum(ml),year_length(y))
            self.assertEqual(ml[2],55);self.assertEqual(ml[5],55);self.assertEqual(ml[8],55)
            self.assertEqual(ml[11],56 if is_leap_year(y) else 55)
            self.assertEqual(sum(minth_length(y,m) for m in range(1,25)),year_length(y))
    def test_05_derived_partition_tables(self):
        for y in (1,2):
            d=__import__('marian_protocol').year_profile(y)
            self.assertEqual(d['quarter_lengths'],[167,167,167,168] if y==1 else [167]*4)
            self.assertEqual(d['sixth_lengths'],[112,111,111,112,111,112] if y==1 else [112,111,111,112,111,111])
            self.assertEqual(d['nominal_weeks'],96)
            self.assertEqual(d['short_terminal_weeks'],3 if y==1 else 4)
    def test_06_absent_terminal_sunsols(self):
        for y in (1,2,100,101):
            for m in (3,6,9):
                with self.assertRaises(MarianError): CivilDate(y,m,8,7)
                self.assertEqual(CivilDate(y,m,8,6).day,6)
            if is_leap_year(y): self.assertEqual(CivilDate(y,12,8,7).ordinal,669)
            else:
                with self.assertRaises(MarianError): CivilDate(y,12,8,7)
    def test_07_source_example(self):
        d=parse_civil('MY42-08-03-05')
        self.assertEqual(d.ordinal_string,'MY42-S409')
        self.assertEqual(parse_ordinal('MY42-S409'),d)
        self.assertEqual(derived(d)['minth'],15)
    def test_08_source_boundary_examples(self):
        for left,right in M3A['boundary_pairs']:
            self.assertEqual(parse_civil(left).offset+1,parse_civil(right).offset)
    def test_09_every_month_ends_without_gaps(self):
        for y in (1,2,99,100,101,1000):
            for m in range(1,13):
                last=ordinal_to_civil(y,sum(month_length(y,j) for j in range(1,m+1)))
                next_d=offset_to_civil(last.offset+1)
                expected=CivilDate(y,m+1,1,1) if m<12 else CivilDate(y+1,1,1,1)
                self.assertEqual(next_d,expected)
    def test_10_prior_independent_century_oracle(self):
        source=ROOT/'fixtures/M2a-first-century-oracle.csv'
        self.assertEqual(hashlib.sha256(source.read_bytes()).hexdigest(),VECTORS['source_sha256'])
        count=0
        with source.open(newline='') as fh:
            for row in csv.DictReader(fh):
                o=int(row['offset'])
                d=offset_to_civil(o)
                self.assertEqual(d.canonical,row['canonical_civil'])
                self.assertEqual(d.ordinal_string,row['canonical_ordinal'])
                self.assertEqual(d.offset,o)
                count+=1
        self.assertEqual(count,66859)
    def test_11_large_years_and_precision(self):
        for y in (10**6,10**12,10**18,10**55):
            for p in ((1,1,1),(3,8,6),(12,8,6)):
                d=CivilDate(y,*p)
                self.assertEqual(offset_to_civil(d.offset),d)
                self.assertGreaterEqual(d.offset,0)
    def test_12_century_endpoints(self):
        for y in (1,2,99,100,101,200,1000,1001,10**18):
            a=offset_to_civil(start_offset(y))
            b=offset_to_civil(start_offset(y+1)-1)
            self.assertEqual(a,CivilDate(y,1,1,1))
            self.assertEqual(b.year,y)
            self.assertEqual(b.ordinal,year_length(y))
    def test_13_parse_valid_golden(self):
        for s in M3A['valid_dates']:self.assertEqual(parse_civil(s).canonical,s)
    def test_14_parse_invalid_golden(self):
        for s in M3A['invalid_dates']+M3A['invalid_canonical_syntax']:
            with self.assertRaises(MarianError): parse_civil(s)
    def test_15_error_vectors(self):
        for c in VECTORS['negative']:
            r=evaluate(c['request'])
            self.assertEqual(r.get('error',{}).get('code'),c['error'],c)
    def test_16_positive_vectors_all_routes(self):
        for v in VECTORS['positive']:
            for action,k in (('parse_civil','civil'),('parse_ordinal','ordinal'),('from_offset','offset_sols')):
                got=evaluate({'action':action,k:v[k]})
                self.assertTrue(got['ok'],(v,got))
                self.assertEqual(got['data']['civil'],v['civil'])
                self.assertEqual(got['data']['ordinal'],v['ordinal'])
                self.assertEqual(got['data']['offset_sols'],v['offset_sols'])
    def test_17_json_interchange(self):
        d=CivilDate(1000000000000000001,12,8,7)
        self.assertEqual(from_civil_object(d.as_json()),d)
        ordinal={'calendar':'marian','rule_version':'marian-civil-v1.0',
                'year':str(d.year),'ordinal_sol':d.ordinal}
        self.assertEqual(from_ordinal_object(ordinal),d)
        self.assertIsInstance(d.as_json()['year'],str)
        self.assertIsInstance(evaluate({'action':'parse_civil','civil':d.canonical})['data']['offset_sols'],str)
    def test_18_reject_bool_and_floats(self):
        for bad in (True,False,1.0,'1'):
            with self.assertRaises(MarianError):CivilDate(bad,1,1,1)
            with self.assertRaises(MarianError):offset_to_civil(bad)
        for bad in (True, 1.0):
            with self.assertRaises(MarianError):CivilDate(1,bad,1,1)
    def test_19_fails_closed_on_epoch(self):
        r=evaluate({'action':'absolute_time'})
        self.assertEqual(r['error']['code'],'UNINSTANTIATED_EPOCH')
        self.assertFalse(r['ok'])
    def test_20_cli_jsonl(self):
        commands='\n'.join(json.dumps(x) for x in [
            {'action':'parse_civil','civil':'MY42-08-03-05'},
            {'action':'parse_civil','civil':'MY2-03-08-07'},
            {'action':'absolute_time'}])+'\n'
        env=__import__('os').environ.copy();env['PYTHONPATH']=str(ROOT/'src')
        p=subprocess.run([sys.executable,'-m','marian_protocol'],input=commands,text=True,capture_output=True,env=env)
        self.assertEqual(p.returncode,2,p.stderr)
        results=[json.loads(x) for x in p.stdout.splitlines()]
        self.assertEqual(len(results),3)
        self.assertEqual(results[0]['data']['ordinal'],'MY42-S409')
        self.assertEqual([x.get('error',{}).get('code') for x in results[1:]],['INVALID_DATE','UNINSTANTIATED_EPOCH'])
    def test_21_no_unsafe_epoch_data(self):
        template=json.loads((ROOT/'schemas/marian-epoch-certificate-UNINSTANTIATED-template.json').read_text())
        self.assertIsNone(template['MY1_first_AMT_midnight']['instant_jd_tt'])
        self.assertIsNone(template['recognised_first_human_step']['instant_jd_tt'])
    def test_22_schema_loads_and_accepts_valid_objects(self):
        civil=json.loads((ROOT/'schemas/marian-civil-date.schema.json').read_text())
        ordinal=json.loads((ROOT/'schemas/marian-ordinal-date.schema.json').read_text())
        self.assertEqual(civil['properties']['year']['type'],'string')
        self.assertEqual(ordinal['properties']['year']['type'],'string')
        try: import jsonschema
        except ImportError:return
        jsonschema.Draft202012Validator.check_schema(civil)
        jsonschema.Draft202012Validator.check_schema(ordinal)
        jsonschema.validate(CivilDate(1,12,8,7).as_json(),civil)
    def test_23_requests_whitelist_and_errors(self):
        for req in ({}, {'action':'year_info','year':'1','extra':'hack'},
                    {'action':'year_info'}, {'action':'parse_civil','civil':False},
                    {'action':'parse_civil','civil':'MY1-01-01-01','ordinal':'MY1-S001'}):
            self.assertFalse(evaluate(req)['ok'])
    def test_24_no_week_continuity_claim(self):
        a=CivilDate(2,3,8,6); b=offset_to_civil(a.offset+1)
        self.assertEqual(derived(a)['weekday_name_english'],'Satsol')
        self.assertEqual(derived(b)['weekday_name_english'],'Monsol')
        self.assertEqual(b.offset,a.offset+1)

if __name__=='__main__':unittest.main()
