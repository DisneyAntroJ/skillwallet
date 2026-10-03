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

Use System Import Sets and the project staging table `u_employee_import`. Actual execution used CSV retrieved through an HTTPS File data source. See `docs/csv-https-import.md` in the extracted package. The original XLSX files remain included as deliverables; do not describe the recorded runs as an XLSX attachment import.

Inspect staging separately from the target. The recorded baseline staging load processed and inserted 15 rows with zero errors. Staging inserts do not prove a target transform succeeded.

## 4. Configure the Transform Map

Map name: **Sample Spreadsheet Import**. Source: `u_employee_import`; target: `u_employee_test`. Create or inspect all five mappings above. Map Name to Employee Name explicitly and enable coalesce only on Employee ID. Inspect generated source field names in the actual instance. The sample uses direct String mappings and does not require a transform script.

## 5. Transform the baseline

Run the map on the baseline import set and inspect history plus target data. Recorded TH0001001: total 15, inserted 15, updated 0, ignored 0, errors 0. Capture the actual result of any reproduction rather than assuming the historical counts.

## 6. Apply the delta

Load the four-row delta into the same staging table, then use the same map. SB-0004 changes Ajay Kumar to Ajay; SB-0010 changes email to test18@example.com; SB-0016 and SB-0017 are new IDs. Recorded TH0001002: total 4, inserted 2, updated 2, ignored 0, errors 0. The final project target contained 17 unique IDs.

For stronger evidence in a fresh reproduction, retain target sys_id values before and after the update. These snapshots were not retained for the recorded run; its update evidence is transform history plus final values.

## 7. Repeat and reconcile

Load and transform the delta again. Require zero duplicate inserts and unchanged final values. Recorded TH0001003: total 4, inserted 0, updated 0, ignored 4, errors 0. Compare all five fields against `data/Expected Final Target.csv` by Employee ID. The captured UI JSON and UI-derived CSV agree with all 85 expected values across 17 employees. The expected CSV is a fixture; the actual CSV is a UI transcription, not a native ServiceNow export.

## 8. Build the reports

Use Employee Test for all three saved Platform Analytics visualizations: Employees by Department (pie, Count, Department), Employees by Location (vertical bar, Count, Location), and Employee List Report (the five employee columns, maximum 20 rows, no grouping). Add all three to **Employee Analytics Dashboards**. Department counts are ServiceNow 9 and Salesforce 8; all location counts total 17. If unrelated records later appear, apply and document a consistent project filter.

## 9. Review the evidence and submission

Read the consolidated six-phase document, `evidence/README.md` and `evidence/final-target-validation.md`. Screenshots 08–14 show the recorded imports and final dashboard; screenshots 19–22 recheck the current dashboard, map and histories. Earlier screenshots 02 and 06 show historical pre-import states only.

SkillWallet was observed at 90% with all nine tasks in Review. Review status is separate from verified configuration and test results. The completed narrated video is included as `demo/Transform_Maps_Project_Demo.mp4`. Watch it at https://drive.google.com/file/d/1gonx-uMMW-M-BO6GmONjhmYsgV-luIr7/view. Formal UAT signoff and four supplementary negative source-preparation cases remain pending.
