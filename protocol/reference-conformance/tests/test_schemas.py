# SPDX-License-Identifier: Apache-2.0
# Copyright 2026 JB Bullock
"""Self-contained schema and value/semantic validation tests."""
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'src'))
from marian_protocol import CivilDate,evaluate

class TestPortableSchemas(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.schemas={p.name.removesuffix('.schema.json'):json.loads(p.read_text()) for p in (ROOT/'schemas').glob('*.schema.json')}
        try:import jsonschema
        except ImportError:cls.jsonschema=None
        else:cls.jsonschema=jsonschema
    def test_25_all_four_schemas_are_json(self):
        self.assertEqual(len(self.schemas),4)
        for name,doc in self.schemas.items():
            self.assertEqual(doc['$schema'],'https://json-schema.org/draft/2020-12/schema')
    def test_26_request_schema_is_self_contained(self):
        self.assertIn('civilDate',self.schemas['marian-api-request']['$defs'])
        self.assertIn('ordinalDate',self.schemas['marian-api-request']['$defs'])
    def test_27_all_good_requests_and_responses_pass_schema(self):
        if not self.jsonschema:self.skipTest('optional jsonschema not installed')
        request_schema=self.schemas['marian-api-request']
        response_schema=self.schemas['marian-api-response']
        for req in [
          {'action':'parse_civil','civil':'MY42-08-03-05'},
          {'action':'parse_ordinal','ordinal':'MY42-S409'},
          {'action':'from_offset','offset_sols':'27821'},
          {'action':'from_ordinal','year':'42','ordinal_sol':409},
          {'action':'year_info','year':'42'},
          {'action':'absolute_time'},
          {'action':'validate_civil_object','date':CivilDate(1,1,1,1).as_json()},
          {'action':'validate_ordinal_object','date':{'calendar':'marian','rule_version':'marian-civil-v1.0','year':'2','ordinal_sol':668}}
        ]:
            self.jsonschema.validate(req,request_schema)
            self.jsonschema.validate(evaluate(req),response_schema)
    def test_28_shape_can_pass_but_calendar_can_fail(self):
        if not self.jsonschema:self.skipTest('optional jsonschema not installed')
        bad=CivilDate(2,3,8,6).as_json();bad['day']=7
        self.jsonschema.validate(bad,self.schemas['marian-civil-date'])
        response=evaluate({'action':'validate_civil_object','date':bad})
        self.assertEqual(response['error']['code'],'INVALID_DATE')
    def test_29_javascript_port_newline_is_invalid(self):
        import subprocess
        # A newline after a valid wire-date cannot be silently accepted.
        script="import {parseCivil} from './js/marian-core.mjs'; try{parseCivil('MY1-01-01-01\\n'); process.exit(3)}catch(e){console.log('OK strict terminal syntax')}"
        p=subprocess.run(['node','--input-type=module','-e',script],cwd=ROOT,text=True,capture_output=True)
        self.assertEqual(p.returncode,0,p.stderr)

if __name__=='__main__':unittest.main()
