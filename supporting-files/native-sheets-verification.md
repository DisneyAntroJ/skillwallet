# Native Google Sheets and Excel export verification

Verified on 3 October 2026. Native Google Sheets were created from the existing project workbooks, then downloaded in Excel format. The original workbooks actually used in ServiceNow were preserved without modification.

| Source | Owner-only native Sheet | Data rows | Native cells matched | Export cells matched |
| --- | --- | ---: | ---: | ---: |
| Baseline | [Sample Spreadsheet](https://docs.google.com/spreadsheets/d/1lErJU_Qs1nby-30jVSWxLws-y7H7LLkAV9IZOknm2P4/edit) | 15 | 75/75 | 75/75 |
| Delta | [Updated Sample Spreadsheet](https://docs.google.com/spreadsheets/d/1K9lTCijrxN4YIwR-ToZZ0WEp5LYWSp3Y3T78TslKgnE/edit) | 4 | 20/20 | 20/20 |

Both header rows match: Employee ID, Name, Email, Department and Location. All 95 data cells match the originals in both native readback and the downloaded Google Excel exports. Browser inspection confirmed that both native sheets display correctly; screenshots 48 and 49 are included in the project ZIP.

The Sheets remain owner-only and their sharing permissions were unchanged. Reviewers can read the original XLSX workbooks in the public repository. The ZIP also includes the verified Google exports separately in `data/google-sheets-export/`, with a README explaining their provenance. These exports have different file hashes because Google generated new XLSX files, but their headers and data match exactly.

The native Sheets and exports were created after the recorded ServiceNow import runs. They do not retrospectively establish Google Sheets as the source of those runs. The primary source workbooks retain these SHA-256 hashes:

| Original workbook used for import | SHA-256 |
| --- | --- |
| Sample Spreadsheet.xlsx | dbe30ef5a6429084b9cdb2c8cf16bddcaa9c0eae1c18f827e98b70bf5722c05c |
| Updated Sample Spreadsheet.xlsx | 3842d1338f7d11932f41af7023d20239c35fdee5fdbddc2beb5d220c0e73027f |

See `native-sheets-verification.json` for creation timestamps, export hashes and the full comparison results. The final ServiceNow XLSX baseline, delta and repeat are documented in [strict-xlsx-verification.md](strict-xlsx-verification.md).
