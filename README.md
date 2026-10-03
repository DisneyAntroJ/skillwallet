# Import Data using Transform Maps (Spreadsheet)

**TNSDC / SkillWallet — Disney Antro J (team lead), Praveen N and Sibin P.**

This ServiceNow Zurich project imports synthetic employee data into **Employee Test**, updates matching employees through **Employee ID coalesce**, and presents the final records in three dashboard reports.

## Project documentation

The single six-phase document covers Ideation, Requirement Analysis, Project Design, Project Planning, Project Development, and Project Documentation. Read the [PDF](Transform_Maps_Six_Phase_Project_Documentation.pdf) or download the [editable DOCX](Transform_Maps_Six_Phase_Project_Documentation.docx). The [owner's editable Google Doc copy](https://docs.google.com/document/d/1LFzab42jFeOn9L5nKm1muUL8pDDFKQp9AvjMeIc7vPs/edit) is saved in the owner's Drive and requires Drive permission; reviewers can use the repository PDF/DOCX without requesting that access.

Download and extract the [complete project package](Transform_Maps_Project_Package.zip) to preserve the `docs/`, `data/`, `evidence/`, and `demo/` folders and view the screenshots and demo offline. Start with the [setup and reproduction guide](project-runbook.md).

| Artifact | Contents |
| --- | --- |
| [Baseline workbook](Sample%20Spreadsheet.xlsx) | 15 synthetic employees, five source columns |
| [Delta workbook](Updated%20Sample%20Spreadsheet.xlsx) | Two changes and two new employees |
| [Data notes](data-notes.md) | Mapping, import order and source provenance |
| [Expected final target](Expected%20Final%20Target.csv) | Modeled comparison fixture |
| [Actual final target](Actual%20Final%20Target%20%28UI%20Verified%29.csv) | Verified UI transcription; not a native export |
| [Validation](final-target-validation.md) | Field-by-field reconciliation and limitations |
| [Excel verification](xlsx-verification.md) | Actual XLSX uploads, repeat check and retained record IDs |
| [Source checks](negative-source-checks.md) | Four passed local preparation checks |
| [HTTPS CSV import guide](csv-https-import.md) | Historical route used for the original demonstration |

The original CSV sources remain in [data/Sample Spreadsheet.csv](data/Sample%20Spreadsheet.csv) and [data/Updated Sample Spreadsheet.csv](data/Updated%20Sample%20Spreadsheet.csv). Their values match the supplied XLSX workbooks exactly. `package-manifest.json` records SHA-256 hashes for the structured files inside the ZIP.

## Original demonstration results — CSV sources

| Transform history | Rows | Inserted | Updated | Ignored | Errors |
| --- | ---: | ---: | ---: | ---: | ---: |
| Baseline — TH0001001 | 15 | 15 | 0 | 0 | 0 |
| Delta — TH0001002 | 4 | 2 | 2 | 0 | 0 |
| Repeat — TH0001003 | 4 | 0 | 0 | 4 | 0 |

The final target contains **17 records and 17 unique Employee IDs**, with **85/85 field values matching** the expected result. Department totals are ServiceNow 9 and Salesforce 8. The saved **Employee Analytics Dashboards** displays Department, Location and Employee List visualizations. The package includes the transform histories, final employee list, dashboard and current configuration screenshots.

Target: `u_employee_test`. Staging: **Employee Import** (`u_employee_import`). Transform Map: `Sample Spreadsheet Import`. All five fields map explicitly, including source **Name → Employee Name**; only Employee ID coalesces.

## Excel attachment verification — 3 October 2026

Both original `.xlsx` workbooks were uploaded through **Load Data → File**, using Sheet 1 and header row 1. This replay used the existing 17 target employees, so the counts differ from the original empty-target demonstration above.

| Actual XLSX run | Import set | History | Rows | Inserts | Updates | Ignored | Errors |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: |
| Baseline | ISET0010004 | TH0001004 | 15 | 0 | 2 | 13 | 0 |
| Update | ISET0010005 | TH0001005 | 4 | 0 | 2 | 2 | 0 |
| Repeat update | ISET0010006 | TH0001006 | 4 | 0 | 0 | 4 | 0 |

The final table still has **17 unique employees**, **85/85 expected values** and **17/17 original record IDs retained**. The four local negative checks also passed: blank ID, repeated ID, incorrect header and missing Name mapping. Invalid copies stayed in memory and were not uploaded. These are pre-import checks, not ServiceNow rejection rules. Read the [full verification and human checklist](xlsx-verification.md).

## Submission status and scope

SkillWallet was observed at **90% with all nine tasks in Review**. Final platform completion is not confirmed. The project demo link opens the finished narrated video.

[Watch the project demo](https://drive.google.com/file/d/1gonx-uMMW-M-BO6GmONjhmYsgV-luIr7/view). The **2 minute 20 second video** includes English captions and the team lead's recorded narration, explaining the configuration, imports, coalesce checks and dashboard using project screenshots. A [1080p MP4 copy](Transform_Maps_Project_Demo.mp4) is included for download. The original video is available through the viewing link.

The video presents the original CSV demonstration; the later Excel attachment results are in the report and verification evidence. **All 19 recorded technical cases passed.** Human tester/team-lead signatures, genuine sprint records and faculty/reviewer acceptance remain outstanding. Transform-history durations round to zero and do not establish performance throughput.

All sample employees are synthetic and all sample email addresses use `example.com`. No login credentials are included.

## Links

- [Project demo video](https://drive.google.com/file/d/1gonx-uMMW-M-BO6GmONjhmYsgV-luIr7/view)
- [GitHub repository](https://github.com/DisneyAntroJ/skillwallet)
- [Live dashboard — ServiceNow sign-in required](https://dev230529.service-now.com/now/platform-analytics-workspace/dashboards/params/edit/false/sys-id/549ca1bac36f8b54c34b78cc05013131)
- [Project template folder](https://drive.google.com/drive/folders/1m_vXdKkujfkVq1x57h6bZ3Kj_07hdh4T)
