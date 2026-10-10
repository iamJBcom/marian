# M2a — Structural mathematical verification

**Scope:** regular MY1+ integer-sol calendar, editor-approved Marian DOCX (Appendices A and D). The mathematical demonstrations below apply to the specified deterministic model, not independently to Mars astronomy.

## 1. Year and month templates (A.4–A.6)

For a common year, the repeated month template is `(56, 56, 55)` four times, so total length is `4 × (56 + 56 + 55) = 668` sols. Its 24 minths comprise 20 of 28 sols and four of 27, so `20 × 28 + 4 × 27 = 668`. A leap year adds one sol only at Month 12 / Week 8 / Day 7; hence nine 56-sol months and three 55-sol months total `669`, or 21 minths of 28 sols and three of 27. This simultaneously establishes the totals and the singular leap-position rule.

Every month has two minths, the first of length 28 and the second of length `month_length − 28`. Both begin on weekday position 1. Every regular month has exactly eight nominal civil week slots. In a 55-sol month the last slot has occupied positions 1–6; in a 56-sol month it has 1–7. This gives `8 × 12 = 96` **nominal weekly slots** per year; it does **not** imply 672 elapsed physical sols.

- Common: `92 × 7 + 4 × 6 = 668` and four shortened slots (Months 3, 6, 9, 12).
- Leap: `93 × 7 + 3 × 6 = 669` and three shortened slots (Months 3, 6, 9).

A shortened week is an omission of one **civil weekday label position**, not an omission of a physical sol. In the chronological sequence, a 55-sol month ends `W8 D6`, and the immediately following physical sol begins the next month `W1 D1`. This was checked at every month boundary across MY1–MY101.

## 2. Quarters and Sixths (A.8–A.9)

Quarters group consecutive triples of months. A common-year quarter is always `56+56+55=167`; Q1–Q3 remain 167 in leap years and Q4 grows to 168. Sixths group consecutive month pairs. Common year lengths are `(112,111,111,112,111,111)`; in a leap year S6 grows to 112. Quarters and Sixths are overlapping annual partitions, not serially nested units.

## 3. Leap count (A.11; D.17)

The leap predicate is `Y mod 100 ≠ 0 AND (Y mod 2 = 1 OR Y mod 10 = 0)` for positive integer years. For MY1–MY100, 50 years are odd; nine additional years among 10, 20, ..., 90 are leap; MY100 is excluded. Thus exactly `50 + 9 = 59` leap sols occur per century, and exactly `41 × 668 + 59 × 669 = 66,859` physical sols pass. The mean civil year is `66,859/100 = 668.590000` sols.

For a nonnegative integer N, the number of leap years in MY1 through MYN is:

`L(N) = floor((N+1)/2) + floor(N/10) − floor(N/100)`.

The terms count all odd years, then decennial years (none odd), then remove century years (all decennial), respectively. The start of MY Y in zero-based sols from the beginning of MY1 is therefore:

`start(Y) = 668×(Y−1) + L(Y−1)`.

The ledger and tests verified this equation against direct year-by-year accumulation across 1,000 years, including MY100, 200, 300 and MY1000 boundaries. Every 100-year block repeats the same 59/41 pattern under the specified rule.

## 4. Date mapping is one-to-one (D.9, D.13–D.19)

Within a valid month, map `(week,day)` to the 1-based physical position `P = 7×(W−1)+D`. Accepted dates require `1 ≤ P ≤ month_length`; hence nonexistent `W8 D7` of a 55-sol month is rejected. Conversely, any `P` in `1..length` maps uniquely to `W=floor((P−1)/7)+1`, `D=((P−1) mod 7)+1`. The two formulas are mutually inverse on the valid domain.

Each ordinal sol is the total length of preceding months plus P. As month lengths are positive, their ordinal intervals are disjoint, gapless and collectively cover exactly `1..year_length` for any regular year. The year start offsets are strictly increasing because each year has 668 or 669 sols. Therefore the composition of year-offset, month-prefix and weekday-position functions is a one-to-one correspondence between **nonnegative integer offsets from MY1** and **valid MY1+ civil dates**, assuming arbitrary-precision integer arithmetic and the frozen leap rule. (This is a structural proof, not a proof of physical UTC/TAI mapping.)

The reference offset inverse uses **integer-only exponential bracketing plus binary search** for the year, followed by exact ordinal-to-civil conversion; it does not rely on floating-point estimation. This retains exactness at very large year values; the book's optional floating-point shortcut is not required.

## 5. Executed checks

- 11 unit test methods: PASS (`reports/M2a-test-output.txt`).
- Exhaustive 66,859-row chronological enumeration of every valid physical sol from MY1–MY100: PASS in both conversion directions, including canonical and ordinal formatting/parsing.
- 1,212 month boundaries (MY1–MY101): PASS.
- All 64 selected positive/negative date fixtures: PASS; some strict parser formatting examples reflect the **audit implementation**, not an author-approved normative grammar policy.
- Ten consecutive 100-year blocks, MY1–MY1000: each 59 leap years, 66,859 physical sols: PASS.
- Large-integer offsets/y=10^15 spot tests: PASS.

## 6. Idealized fractional-year residual, not astronomy

Against a purely **assumed constant** target of exactly `668.590000` sols per year, the year-end cumulative civil difference is between `−0.72` and `+1.31` sols inside MY1–MY100, returning to exactly `0` sols at MY100. This can be derived by counting `(100 × cumulative_leaps − 59 × elapsed_years) / 100`. It does not reproduce a varying true `Ls=15°` recurrence and cannot substantiate real-world long-term accuracy or phase drift; that is M2b.
