# Excel import verification from an empty target

Verified on 3 October 2026 using the actual XLSX attachments in ServiceNow. The project target was backed up privately and reset through recoverable delete job DM0001001 before this sequence. It contained zero rows before the baseline. The private backup is excluded from the submission.

| Run | Import set | History | Rows | Inserts | Updates | Ignored | Errors |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Baseline XLSX | ISET0010007 | TH0001007 | 15 | 15 | 0 | 0 | 0 |
| Delta XLSX | ISET0010008 | TH0001008 | 4 | 2 | 2 | 0 | 0 |
| Repeat delta XLSX | ISET0010009 | TH0001009 | 4 | 0 | 0 | 4 | 0 |

All three histories completed with zero skipped rows and errors. The baseline snapshot matches all 75 source values in `Sample Spreadsheet.xlsx`. Both the delta and repeat snapshots match all 85 expected values in `Expected Final Target.csv`, with 17 records and 17 unique Employee IDs.

All 15 baseline record IDs were retained when the delta updated two employees and added two. All 17 delta record IDs were retained by the repeat. The repeat changed no values. These comparisons concern the new sequence; resetting the target created new record IDs, so the older snapshots describe historical records.

Department totals are ServiceNow 9 and Salesforce 8. Location totals sum to 17. History durations display 0 Seconds, which is insufficient to measure throughput.

## Evidence

The package contains screenshots 35-47 for the empty target, XLSX selection, staging, three transforms, final records, dashboard and mapping. `strict-target-after-baseline.json`, `strict-target-after-delta.json` and `strict-target-after-repeat.json` record values and record links captured from the UI. `strict-*-history.txt` records the history grids. The current `final-target-*` files describe the repeat result after TH0001009.

The original CSV histories TH0001001-TH0001003 and the earlier populated-target Excel replay TH0001004-TH0001006 remain as dated supplementary evidence. The supplied narrated video covers the original CSV demonstration; this later Excel sequence is documented here and in the six-phase report.

## Test summary and human review

All 23 recorded checks passed: 18 functional checks, one duration observation and four local source-preparation checks. The four negative checks use disposable local copies and do not establish automatic rejection rules inside ServiceNow.

The tester must inspect the final records, dashboard, demo and repository, then enter their real name, date and signature in Phase 5. The team lead must complete acceptance. Phase 4 records the shared project work period retrospectively as 29 September–3 October 2026, from the first implementation request through corrected technical publication. This covers five calendar dates inclusively and applies to all three work groups; it is not a record of individually timed sprints or five full working days. Original planned sprint deadlines and accepted points remain unrecorded. Faculty/reviewer approval and SkillWallet final acceptance remain separate requirements. The latest observed platform status is 90%, with nine tasks in Review.
