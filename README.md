# Import Data using Transform Maps (Spreadsheet)

**TNSDC / SkillWallet — Disney Antro J (team lead), Praveen N and Sibin P.**

This ServiceNow project imports employee spreadsheets, updates matching employees using Employee ID coalesce, and displays the results in three dashboard reports. All employee data is synthetic.

## Project files

| File | Purpose |
| --- | --- |
| [Project report — PDF](Transform_Maps_Six_Phase_Project_Documentation.pdf) | Six phases, implementation, test results and evidence |
| [Project report — editable DOCX](Transform_Maps_Six_Phase_Project_Documentation.docx) | Editable copy of the same report |
| [Baseline spreadsheet](Sample%20Spreadsheet.xlsx) | 15 employees for the first import |
| [Update spreadsheet](Updated%20Sample%20Spreadsheet.xlsx) | Two changes and two new employees |
| [Narrated demo — MP4](Transform_Maps_Project_Demo.mp4) | Downloadable project demonstration |
| [Complete project package — ZIP](Transform_Maps_Project_Package.zip) | All documents, source data, screenshots, guides and checks |

[Watch the demo online](https://drive.google.com/file/d/1gonx-uMMW-M-BO6GmONjhmYsgV-luIr7/view). The video demonstrates the original CSV imports; the later Excel attachment results are documented in the report and evidence.

The [supporting-files folder](supporting-files/) contains the setup guide, data notes, validation results and source-check script. These files have been grouped together, not removed. The complete ZIP preserves its original `docs/`, `data/`, `evidence/`, `demo/` and `qa/` structure. Its manifest records the hashes of the packaged files.

The original [baseline CSV](data/Sample%20Spreadsheet.csv) and [update CSV](data/Updated%20Sample%20Spreadsheet.csv) remain at their existing URLs for the ServiceNow HTTPS data sources.

## Verified Excel results — 3 October 2026

| Import | Inserts | Updates | Ignored | Errors |
| --- | ---: | ---: | ---: | ---: |
| Baseline — TH0001007 | 15 | 0 | 0 | 0 |
| Update — TH0001008 | 2 | 2 | 0 | 0 |
| Repeat update — TH0001009 | 0 | 0 | 4 | 0 |

The final target contains **17 employees with 17 unique IDs**, and **85/85 field values match** the expected result. The update preserved all 15 baseline record IDs; the repeat preserved all 17 resulting record IDs. The saved dashboard contains Department, Location and Employee List reports.

## Submission status

The last verified SkillWallet status was **90%, with all nine tasks in Review**. Human tester and team-lead signatures, genuine sprint records, and faculty/reviewer approval remain pending. Passed technical checks do not establish final platform acceptance.

[Open the live dashboard — ServiceNow sign-in required](https://dev230529.service-now.com/now/platform-analytics-workspace/dashboards/params/edit/false/sys-id/549ca1bac36f8b54c34b78cc05013131).
