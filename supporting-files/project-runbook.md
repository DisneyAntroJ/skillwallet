# ServiceNow Transform Maps — setup and reproduction guide

Project: Import Data using Transform Maps (Spreadsheet). Team: Disney Antro J, Praveen N and Sibin P.

Use the complete `Transform_Maps_Project_Package.zip` for the definitive folder structure. Extract it, open its README, and keep `docs`, `data`, `evidence`, and `demo` together. This guide records the implemented configuration and explains how to reproduce it; it is not a one-click instance installer or a configuration export.

## Environment and prerequisites

Recorded environment: ServiceNow Zurich, Global scope, `dev230529.service-now.com`. Use an authorized instance account with access to project tables, import sets, transform maps and Platform Analytics. PDI availability and account access are separate from this offline package.

Inspect existing objects and project data before creating or rerunning anything. Reuse suitable project objects. The baseline's 15-insert result assumes an initially empty project target; later reruns against existing rows can produce different update/ignored counts. Do not delete unrelated data to reproduce a count.

## 1. Inspect the spreadsheet

`data/Sample Spreadsheet.xlsx` contains 15 synthetic employees, IDs SB-0001 through SB-0015. `data/Updated Sample Spreadsheet.xlsx` is a separate four-row delta. Both use Sheet1, headers in row 1 and values from row 2. Keep IDs as text; verify five headers, no blank required values and unique IDs within each source. The included CSV files contain the same values.

## 2. Configure the target table

Table label: **Employee Test**. Internal name: `u_employee_test`, Global scope. All five fields are String.

| Source header | Target label | Target internal name | Length | Coalesce |
| --- | --- | --- | ---: | --- |
| Employee ID | Employee ID | u_employee_id | 40 | Yes |
| Name | Employee Name | u_employee_name | 100 | No |
| Email | Email | u_email | 100 | No |
| Department | Department | u_department | 100 | No |
| Location | Location | u_location | 100 | No |

## 3. Load the source into staging

Open **System Import Sets → Load Data**. Select **File** and upload `Sample Spreadsheet.xlsx`, with Sheet number **1** and Header row **1**. Choose the existing **Employee Import [u_employee_import]** table. On a fresh instance, create the staging table with that label and internal name. Inspect the loaded rows before running the saved map. For the update and repeat, select `Updated Sample Spreadsheet.xlsx` and reuse the same table and map.

Actual XLSX uploads from an empty target were verified on 3 October 2026 as ISET0010007–ISET0010009. The earlier populated-target replay ISET0010004–ISET0010006 and the original CSV-over-HTTPS demonstration are retained as historical evidence.

Inspect staging separately from the target. The recorded baseline staging load processed and inserted 15 rows with zero errors. Staging inserts do not prove a target transform succeeded.

## 4. Configure the Transform Map

Map name: **Sample Spreadsheet Import**. Source: `u_employee_import`; target: `u_employee_test`. Create or inspect all five mappings above. Map Name to Employee Name explicitly and enable coalesce only on Employee ID. Inspect generated source field names in the actual instance. The sample uses direct String mappings and does not require a transform script.

## 5. Transform the baseline

Run the map on the baseline import set and inspect history plus target data. Recorded XLSX TH0001007: total 15, inserted 15, updated 0, ignored 0, errors 0. The target began empty and all 75 baseline values matched the workbook. Capture the actual result of any reproduction rather than assuming the recorded counts.

## 6. Apply the delta

Load the four-row delta into the same staging table, then use the same map. SB-0004 changes Ajay Kumar to Ajay; SB-0010 changes email to test18@example.com; SB-0016 and SB-0017 are new IDs. Recorded XLSX TH0001008: total 4, inserted 2, updated 2, ignored 0, errors 0. The final project target contained 17 unique IDs.

Retain target sys_id values before and after the update. The delta preserved all 15 baseline record identities. `evidence/strict-target-after-baseline.json` and `evidence/strict-target-after-delta.json` show the comparisons. The earlier `xlsx-target-*.json` files describe the separate populated-target replay before the recoverable reset and contain historical record IDs.

## 7. Repeat and reconcile

Load and transform the delta again. Require zero duplicate inserts and unchanged final values. Recorded XLSX TH0001009: total 4, inserted 0, updated 0, ignored 4, errors 0. All 17 delta record IDs and every value were retained. Compare all five fields against `data/Expected Final Target.csv` by Employee ID. The fresh UI JSON and UI-derived CSV agree with all 85 expected values across 17 employees. The expected CSV is a fixture; the actual CSV is a UI transcription, not a native ServiceNow export.

## 8. Build the reports

Use Employee Test for all three saved Platform Analytics visualizations: Employees by Department (pie, Count, Department), Employees by Location (vertical bar, Count, Location), and Employee List Report (the five employee columns, maximum 20 rows, no grouping). Add all three to **Employee Analytics Dashboards**. Department counts are ServiceNow 9 and Salesforce 8; all location counts total 17. If unrelated records later appear, apply and document a consistent project filter.

## 9. Review the evidence and submission

Read the consolidated six-phase document, `evidence/README.md` and `evidence/strict-xlsx-verification.md`. Screenshots 35–47 show the final empty-target XLSX sequence, including uploads, staging, 15 baseline inserts, 2 delta inserts and 2 updates, 4 ignored repeat rows, final records, dashboard and map. Screenshots 08–14 show the original CSV demonstration; 19–22 recheck its configuration; 23–34 show the earlier populated-target Excel replay. Screenshots 02 and 06 show historical pre-import states only.

The final XLSX sequence began after the 17 project records were backed up privately and removed through recoverable job DM0001001. TH0001007 inserted 15 rows, TH0001008 inserted 2 and updated 2, and TH0001009 ignored all 4 unchanged rows. Every run had zero skipped rows and errors. Baseline reconciliation passed for 75/75 values, and both delta and repeat passed for 85/85 values. All 15 baseline IDs survived the delta and all 17 delta IDs survived the repeat. Private backup and working files are excluded from the public package.

The earlier Excel replay started with 17 employees. TH0001004 processed 15 rows: 0 inserts, 2 updates and 13 ignored. TH0001005 processed 4 rows: 0 inserts, 2 updates and 2 ignored. TH0001006 processed 4 rows: 0 inserts, 0 updates and 4 ignored. Each had zero errors. Its record IDs are historical after the reset; its evidence remains in `evidence/xlsx-verification.md`. The 29 September CSV snapshots are archived in `evidence/historical-csv-2026-09-29/`.

Four local source checks passed: blank ID, duplicate ID, wrong header and omitted Name mapping. Run `python qa/validate_import_sources.py --data-dir data --output-dir evidence` from the extracted package to reproduce them. The original workbooks are read-only; invalid copies stay in memory. No ServiceNow rejection rule is implied.

SkillWallet was observed at 90% with all nine tasks in Review. All 23 recorded checks passed: 18 functional checks, one duration observation and four local source checks. Human acceptance is separate. The narrated original CSV demonstration is `demo/Transform_Maps_Project_Demo.mp4`, available at https://drive.google.com/file/d/1gonx-uMMW-M-BO6GmONjhmYsgV-luIr7/view. The report includes the later Excel verification.

The human tester must inspect the final records and dashboard, play the demo, check repository files, then enter their own name, date and signature in Phase 5. The team lead must record their own acceptance; the faculty/reviewer must record their own approval. Phase 4 records the shared project work period retrospectively as 29 September–3 October 2026, from the first implementation request through corrected technical publication. This covers five calendar dates inclusively and applies to all three work groups; it is not a record of individually timed sprints or five full working days. Original planned sprint deadlines and accepted points remain unrecorded. Keep the missing planned deadlines and accepted points as Not recorded unless confirmed from genuine team records. Do not substitute this retrospective work period for an original sprint plan, or planning points for accepted results. Use the final checklist in `evidence/strict-xlsx-verification.md`.
