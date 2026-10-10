// SPDX-License-Identifier: Apache-2.0
// Copyright 2026 JB Bullock
// Standalone independent Node.js verification against the frozen M2a first-century oracle.
import {readFileSync} from 'node:fs';
import {resolve,dirname} from 'node:path';
import {fileURLToPath} from 'node:url';
import {strict as assert} from 'node:assert';
import * as m from './marian-core.mjs';
const root=resolve(dirname(fileURLToPath(import.meta.url)),'..');
const records=readFileSync(resolve(root,'fixtures/M2a-first-century-oracle.csv'),'utf8').trim().split(/\r?\n/);
assert.equal(records[0],'offset,year,month,week,day,ordinal,canonical_civil,canonical_ordinal');
let count=0;
for(const line of records.slice(1)) {
  const [offset,year,month,week,day,ordinal,civil,ords]=line.split(',');
  const o=BigInt(offset), y=BigInt(year), mm=Number(month), w=Number(week), d=Number(day);
  const result=m.offsetToCivil(o);
  assert.deepEqual(result,{y,m:mm,w,d});
  assert.equal(m.civilToOffset(y,mm,w,d),o);
  assert.equal(m.civilToOrdinal(y,mm,w,d),Number(ordinal));
  assert.equal(m.canonical(result),civil);
  assert.deepEqual(m.parseCivil(civil),result);
  assert.equal(`MY${year}-S${String(ordinal).padStart(3,'0')}`,ords);
  count++;
}
assert.equal(count,66859);
assert.equal(m.civilToOrdinal(42n,8,3,5),409);
for(const y of [1n,2n,99n,100n,101n,1000n,1000000000000000000n]) {
  assert.equal(m.startOffset(y+1n)-m.startOffset(y),BigInt(m.yearLength(y)));
  const start=m.startOffset(y), end=start+BigInt(m.yearLength(y))-1n;
  assert.equal(m.offsetToCivil(start).y,y);
  assert.equal(m.offsetToCivil(end).y,y);
}
for(const y of [1n,2n,100n,101n]) {
 for(const s of [1,100,m.yearLength(y)]) {
  const c=m.ordinalToCivil(y,s);
  assert.equal(m.civilToOrdinal(c.y,c.m,c.w,c.d),s);
 }
}
for(const [y,month] of [[1n,3],[2n,12],[100n,12]]) {
  assert.throws(()=>m.civilToOrdinal(y,month,8,7));
}
console.log(`PASS Node BigInt independent oracle: ${count} first-century sols; transitions, edge years and 10^18-year arithmetic`);
