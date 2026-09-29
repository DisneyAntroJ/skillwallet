# Import Data using Transform Maps (Spreadsheet)

A TNSDC ServiceNow project. **All nine tasks are implemented; SkillWallet shows all nine in Review and 90% overall, pending platform review.**

The Zurich implementation loads synthetic employee data into `u_employee_import`, then uses **Sample Spreadsheet Import** to map five String fields into `u_employee_test`. Source **Name** maps to **Employee Name**, and **Employee ID alone coalesces**. Department pie, Location bar, and Employee List reports appear on **Employee Analytics Dashboards**.

| Verified transform | Total | Inserts | Updates | Ignored | Errors |
| --- | ---: | ---: | ---: | ---: | ---: |
| TH0001001 — baseline | 15 | 15 | 0 | 0 | 0 |
| TH0001002 — delta | 4 | 2 | 2 | 0 | 0 |
| TH0001003 — repeated delta | 4 | 0 | 0 | 4 | 0 |

Final validation: **17 records, 17 unique Employee IDs, 85/85 exact field matches**, with no missing IDs or mismatches. Repeating the delta created no duplicates.

- [Live dashboard demo — ServiceNow sign-in required](https://dev230529.service-now.com/now/platform-analytics-workspace/dashboards/params/edit/false/sys-id/549ca1bac36f8b54c34b78cc05013131)
- [Baseline CSV — 15 employees](https://github.com/DisneyAntroJ/skillwallet/blob/main/data/Sample%20Spreadsheet.csv)
- [Update CSV — two updates and two additions](https://github.com/DisneyAntroJ/skillwallet/blob/main/data/Updated%20Sample%20Spreadsheet.csv)

All data is synthetic; email addresses use `example.com`. Execution used the approved HTTPS CSV data-source route. Original XLSX workbooks, project documents, and captured evidence are prepared in the delivery package. The demo is a live authenticated dashboard, not a video. Platform review/acceptance has not been confirmed.
