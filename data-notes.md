# Employee import data

These synthetic records support the SkillWallet project **Import Data using Transform Maps (Spreadsheet)**. They are practice data, not a real employee roster. All email addresses use `example.com`, including `test18@example.com` in place of the tutorial's Gmail example.

## Files and import order

| File | Purpose | Data rows |
| --- | --- | ---: |
| `Sample Spreadsheet.xlsx` | First import into an empty employee target table | 15 |
| `Updated Sample Spreadsheet.xlsx` | Second import: two existing employees and two new employees | 4 |
| `Sample Spreadsheet.csv` | CSV equivalent of the first workbook | 15 |
| `Updated Sample Spreadsheet.csv` | CSV equivalent of the second workbook | 4 |
| `Expected Final Target.csv` | Expected target snapshot after both imports, for comparison only | 17 |
| `Actual Final Target (UI Verified).csv` | Actual values transcribed from the captured ServiceNow UI and verified against the expected snapshot | 17 |

Each workbook has one worksheet, `Sheet1`, with the five column headers in row 1 and data starting in row 2. The CSV versions contain the same source values. `Expected Final Target.csv` is the modeled result. `Actual Final Target (UI Verified).csv` contains the values captured from the ServiceNow UI, sorted by Employee ID; it is not a native ServiceNow CSV export. Use the import sequence documented in the project runbook.

## Transform mapping

| Source spreadsheet header | Target field label | Coalesce |
| --- | --- | --- |
| Employee ID | Employee ID | Yes |
| Name | Employee Name | No |
| Email | Email | No |
| Department | Department | No |
| Location | Location | No |

Map `Name` to `Employee Name` explicitly if Auto Map Matching Fields does not match them. Keep employee IDs as text and enable coalesce on Employee ID only. Keep all five mappings on both imports. All IDs and email addresses are nonblank and unique within each source file.

## Expected behavior

1. Starting with an empty target table, the first import inserts `SB-0001` through `SB-0015`: 15 records.
2. The second import changes `SB-0004` from **Ajay Kumar** to **Ajay**, changes `SB-0010` from `ravi.teja@example.com` to `test18@example.com`, and adds `SB-0016` and `SB-0017`. Expected result: two updated records, two inserted records, and 17 total target records.
3. Reimport the same four-row second file using the same coalescing map. It matches the four existing IDs, inserts zero new records, and leaves 17 target records with the same field values. ServiceNow may report matched rows as updated or ignored depending on its transform settings; verify zero inserts, unique IDs, and the final values.

The source row counts, required fields, unique keys, two-update/two-insert case, and repeat-import model were verified locally. An independent comparison of `final-target-ui-data.json` with the expected snapshot also confirmed that all 85 captured final field values match exactly, with 17 records and 17 unique IDs. See `final-target-validation.md` and `.json` for the comparison and provenance. Live transform-history screenshots are separate evidence of the import runs.

Requirements source: [SkillWallet project](https://myskillwallet.ai/dashboard/skillwallet/module/servicenow-system-administrator-nm-eng-6a69e3438beabdd402737035/group-projects/6a96be465827789d637561a8/Import-Data-using-Transform-Maps-Spreadsheet--6ab4cf5ba238dc999eb59656?tab=2), as reviewed for this project.
