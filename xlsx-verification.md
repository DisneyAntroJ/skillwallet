> Historical evidence: this populated-target replay preceded the recoverable reset. For the current empty-target XLSX baseline, delta and repeat, see [strict-xlsx-verification.md](strict-xlsx-verification.md).

# Excel import verification — 3 October 2026

The actual `.xlsx` workbooks were uploaded through ServiceNow **Load Data**, using File, Sheet 1 and header row 1. All three imports used the existing `u_employee_import` staging table and **Sample Spreadsheet Import** map into `u_employee_test`.

This was a replay against the 17 existing employees. The baseline restored two original values, the delta reapplied the two changes, and the repeated delta left the final data unchanged. No target records were deleted.

| Run | Import set | History | Total | Inserts | Updates | Ignored | Errors |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Baseline XLSX | ISET0010004 | TH0001004 | 15 | 0 | 2 | 13 | 0 |
| Delta XLSX | ISET0010005 | TH0001005 | 4 | 0 | 2 | 2 | 0 |
| Repeat XLSX | ISET0010006 | TH0001006 | 4 | 0 | 0 | 4 | 0 |

All three staging loads and transforms completed with zero errors. Final checks passed: **17 records, 17 unique IDs, 85/85 expected values and 17/17 original sys_id values retained**. SB-0004 is Ajay; SB-0010 is test18@example.com. Department totals remain ServiceNow 9 and Salesforce 8. Transform durations display 0 Seconds, so no precise throughput is claimed.

The separate original CSV histories demonstrate the initial 15 inserts, then 2 inserts and 2 updates, then zero duplicate inserts. The narrated video presents those original runs. The Excel results above supplement that recording; they are not described as fresh empty-table inserts.

## Evidence in the complete project package

- Screenshots 23–30: actual workbook selections, successful staging and three transform histories.
- Screenshot 31: final employee list. Screenshot 32: saved five-field map and Employee ID coalesce.
- Screenshot 33: the staging label corrected to Employee Import; the internal table remains u_employee_import.
- `xlsx-target-before.json`, `xlsx-target-after-baseline.json`, `xlsx-target-after-repeat.json`: UI-derived values and record URLs for independent identity comparison.
- `xlsx-verification.json`: reconciliation totals; `xlsx-*-history.txt`: captured history grid text.
- `negative-source-checks.json` and `.md`: four passed local source-preparation checks; invalid copies were never uploaded.

## Human verification before acceptance

1. In ServiceNow, open Employee Test and confirm 17 records, Ajay for SB-0004 and test18@example.com for SB-0010. Open the saved dashboard and check all three reports.
2. Play the submitted demo and open the GitHub PDF and workbooks. The video describes the original CSV demonstration; the report includes the later Excel attachment checks.
3. In Phase 5, the actual tester enters their name, verification date and signature. The team lead records acceptance only after reviewing the evidence.
4. In Phase 4, enter the real sprint dates and accepted points from team records. If those records do not exist, keep Not recorded and ask the faculty how they want the planning record completed. Do not invent retrospective dates or velocity.
5. Ask the assigned faculty or reviewer to review the nine SkillWallet items in Review and record their own approval. A submitted link or a passed technical check does not itself establish 100% platform acceptance.
