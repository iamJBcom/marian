// SPDX-License-Identifier: Apache-2.0
// Copyright 2026 JB Bullock
// Marian v1.0 M3b CORE-DATE independent BigInt verification port.
// Draft only; not an epoch/astronomy implementation or ratified standard.
export const RULE_VERSION = 'marian-civil-v1.0';
const CENTURY_SOLS = 66859n;
const digits = /^[1-9][0-9]*$/;
function year(y) {
  if (typeof y !== 'bigint' || y < 1n) throw new RangeError('year must be BigInt >= 1');
  return y;
}
export function leap(y) {
  year(y);
  return y % 100n !== 0n && (y % 2n === 1n || y % 10n === 0n);
}
export function yearLength(y) { return leap(y) ? 669 : 668; }
export function monthLength(y,m) {
  year(y);
  if (!Number.isInteger(m) || m < 1 || m > 12) throw new RangeError('invalid month');
  if (m % 3 === 0 && (m !== 12 || !leap(y))) return 55;
  return 56;
}
export function startOffset(y) {
  year(y);
  const n=y-1n;
  const leaps=(n+1n)/2n+n/10n-n/100n;
  return n*668n+leaps;
}
export function civilToOrdinal(y,m,w,d) {
  if (!Number.isInteger(w) || w<1 || w>8 || !Number.isInteger(d) || d<1 || d>7) throw new RangeError('invalid week/day');
  let position=(w-1)*7+d;
  if (position>monthLength(y,m)) throw new RangeError('absent Sunsol');
  let previous=0;
  for(let j=1;j<m;j++) previous+=monthLength(y,j);
  return previous+position;
}
export function civilToOffset(y,m,w,d) {return startOffset(y)+BigInt(civilToOrdinal(y,m,w,d)-1);}
export function ordinalToCivil(y,ordinal) {
  year(y);
  if (!Number.isInteger(ordinal)||ordinal<1||ordinal>yearLength(y)) throw new RangeError('invalid ordinal');
  let r=ordinal;
  for(let m=1;m<=12;m++) {
    const ml=monthLength(y,m);
    if(r<=ml) return {y,m,w:Math.floor((r-1)/7)+1,d:(r-1)%7+1};
    r-=ml;
  }
  throw new Error('calendar invariant broken');
}
export function offsetToCivil(offset) {
  if(typeof offset!=='bigint'||offset<0n) throw new RangeError('nonnegative BigInt offset required');
  const cycles=offset/CENTURY_SOLS;
  const base=100n*cycles+1n;
  let lo=base,hi=base+100n;
  while(hi-lo>1n) {
    const mid=(lo+hi)/2n;
    if(startOffset(mid)<=offset)lo=mid;else hi=mid;
  }
  return ordinalToCivil(lo,Number(offset-startOffset(lo)+1n));
}
export function parseCivil(text) {
  if(typeof text!=='string')throw new RangeError('expected date string');
  const m=/^MY([1-9][0-9]*)-([0-9]{2})-([0-9]{2})-([0-9]{2})$/.exec(text);
  if(!m || m[0] !== text)throw new RangeError('invalid canonical date syntax');
  let out={y:BigInt(m[1]),m:Number(m[2]),w:Number(m[3]),d:Number(m[4])};
  civilToOrdinal(out.y,out.m,out.w,out.d);
  return out;
}
export function canonical({y,m,w,d}) {
  return `MY${year(y)}-${String(m).padStart(2,'0')}-${String(w).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
}
