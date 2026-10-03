# Current final target verification

Verified on 3 October 2026 after the XLSX repeat transform TH0001009. The current UI snapshot contains 17 employees and 17 unique Employee IDs. All 85 values across Employee ID, Employee Name, Email, Department and Location match [Expected Final Target.csv](Expected%20Final%20Target.csv). No missing IDs, unexpected IDs, blank values or differences were found.

The baseline XLSX produced 15 records matching all 75 source values. The delta retained all 15 baseline record IDs, added two records and updated two values. The repeat retained all 17 resulting record IDs and changed no values. The new record IDs are recorded in `final-target-ui-data.json` and the three `strict-target-after-*.json` files.

Department counts are ServiceNow 9 and Salesforce 8. Location counts total 17. See [strict-xlsx-verification.md](strict-xlsx-verification.md) for the three actual XLSX histories and evidence details.

[Actual Final Target (UI Verified).csv](Actual%20Final%20Target%20%28UI%20Verified%29.csv) is derived from captured UI values, not a native ServiceNow CSV export. The expected CSV is a comparison fixture. The original 29 September snapshots are historical and remain in `historical-csv-2026-09-29/` within the package.
