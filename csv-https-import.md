# CSV import through an HTTPS File data source

Historical note: the following guide records the original CSV demonstration. The final XLSX sequence from an empty target was verified on 3 October 2026 as TH0001007–TH0001009; see strict-xlsx-verification.md.

This approved alternative to the blocked local file selector was used successfully. Both synthetic source CSVs are published in the linked public GitHub repository and were retrieved through ServiceNow's normal data-source UI. Baseline, delta and repeat transformations completed with no errors. The original XLSX workbooks remain project deliverables; the CSV files contain the same source values.

## Verified publication and baseline load

| Item | Verified value |
| --- | --- |
| Baseline published file | [data/Sample Spreadsheet.csv](https://github.com/DisneyAntroJ/skillwallet/blob/main/data/Sample%20Spreadsheet.csv) |
| Baseline publication commit | [9a24c7f0acde456ffacf28d5bcdcd916f5a71a16](https://github.com/DisneyAntroJ/skillwallet/commit/9a24c7f0acde456ffacf28d5bcdcd916f5a71a16) |
| Delta published file | [data/Updated Sample Spreadsheet.csv](https://github.com/DisneyAntroJ/skillwallet/blob/main/data/Updated%20Sample%20Spreadsheet.csv) |
| Delta publication commit | [a92bf12](https://github.com/DisneyAntroJ/skillwallet/commit/a92bf12) |
| Baseline HTTPS data source | `ec4ee1bec36f8b54c34b78cc050131b8` |
| Loaded staging table | `u_employee_import` |
| Baseline staging result | 15 processed, 15 inserts, 0 updates, 0 errors, 0 ignored |
| Evidence | `evidence/08-baseline-staging-load.png` in the complete project ZIP |

These 15 inserts are staging records, not target employee records. The separate verified target runs are **TH0001001** (15 inserts), **TH0001002** (2 inserts and 2 updates), and **TH0001003** (0 inserts, 0 updates, 4 ignored). Each has 0 errors. The final target has 17 unique employees and [85/85 field matches](final-target-validation.md).

## Supported ServiceNow route

Zurich supports CSV File data sources and HTTPS retrieval. Its File data source form separates the server from the file path, provides a CSV delimiter field, and automatically URL-encodes HTTP/HTTPS paths. Do not pre-encode spaces in the File path. [File type data sources](https://www.servicenow.com/docs/r/zurich/integrate-applications/system-import-sets/r_FileTypeDataSource.html), [Create a File type data source](https://www.servicenow.com/docs/r/zurich/integrate-applications/system-import-sets/create-file-type-data-source.html).

1. Verify each published file's exact repository path, branch or commit, contents, headers, and row count. Use a URL that returns the raw CSV, not the GitHub HTML file-view page. Publication of these files does not complete the full project repository or SkillWallet submission.
2. Open **System Import Sets → Administration → Data Sources → New**, or inspect a suitable existing source. Configure the values below through the form.
3. Save, reopen, and use the data source's **Load All Records** action. Inspect the new import set, loaded rows, and load errors before running the Transform Map. The documented UI sequence separates loading from **Run Transform → Transform**. [Official load/transform sequence](https://www.servicenow.com/docs/r/zurich/environmental-social-governance/import-a-formula-into-a-cmd.html).
4. Use the verified staging table in `Sample Spreadsheet Import`, preserving all five mappings and Employee ID coalesce. Run the same baseline, delta, and repeat acceptance tests in [the project runbook](project-runbook.md).

| Form field | Project setting |
| --- | --- |
| Name | A clear project data-source name, recorded in the live ledger |
| Import set table label/name | Employee Import / verified `u_employee_import`; reuse this staging table |
| Type | File |
| Format | CSV |
| File retrieval method | HTTPS |
| Server | `raw.githubusercontent.com` |
| Port | 443 if the form requires an explicit HTTPS port |
| File path | `/<owner>/<repository>/<verified-ref>/<exact-published-file-path>`; leading slash, no scheme or hostname, no pre-encoded spaces |
| CSV delimiter | Comma |
| Zipped | Off for the plain CSV files |
| Username / Password | Blank for the approved public files |
| Optional Properties | `charset=utf-8`, if needed and available on the form |

The published `main` file paths for the ServiceNow File path field are `/DisneyAntroJ/skillwallet/main/data/Sample Spreadsheet.csv` and `/DisneyAntroJ/skillwallet/main/data/Updated Sample Spreadsheet.csv`. Enter spaces directly in this field. The GitHub raw links returned by the repository listing encode spaces for ordinary URL use: [baseline raw CSV](https://raw.githubusercontent.com/DisneyAntroJ/skillwallet/main/data/Sample%20Spreadsheet.csv) and [delta raw CSV](https://raw.githubusercontent.com/DisneyAntroJ/skillwallet/main/data/Updated%20Sample%20Spreadsheet.csv). Preserve the actual saved data-source settings in the evidence ledger rather than inferring every optional field from the successful load.

For the delta and repeated delta, retain the **same verified staging table**. Reuse the source with a documented File path change, or configure a second source against that same staging table if the UI permits it. Do not silently switch to a newly generated table name, which would require a different source-table mapping.

## Reusing an existing source from Load Data

The Load Data form also offers **Data source** under **Source of the import**, allowing an existing source/file to be selected from the instance. Select the saved source and the intended staging table where offered, then inspect the resulting import set. The exact controls must be checked in this PDI. Directly using the saved source's Load All Records action is another documented route. [Zurich Upload Excel Files documentation](https://www.servicenow.com/docs/r/zurich/employee-service-management/indoor-mapping/upload-excel-files.html).

## Evidence to record

- Verified public file URLs and publication commit; baseline has 15 rows, delta has 4.
- Saved data-source IDs, HTTPS settings, and actual staging-table identifier.
- Each load's import set ID, row count, and errors; each separate transform run and its actual results.
- Baseline 15 records from an empty project target, delta final 17 unique IDs, and repeat zero new inserts, once demonstrated.

The original runs in this guide used CSV retrieved over HTTPS. The later empty-target Excel sequence is documented in strict-xlsx-verification.md. Loading a file into staging does not itself validate target data, coalesce behavior, or dashboard counts.
