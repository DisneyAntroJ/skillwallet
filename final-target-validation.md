# Final target data validation

All **85 of 85 field values** in the captured ServiceNow employee list match the expected final snapshot exactly. The capture contains **17 records with 17 unique employee IDs**, no missing or unexpected IDs, and no blank values.

The comparison matched each record by Employee ID and compared Employee ID, Employee Name, Email, Department, and Location. It confirms `SB-0004` has the name **Ajay**, `SB-0010` has the email `test18@example.com`, and the new records `SB-0016` and `SB-0017` are present.

Department totals are **ServiceNow 9** and **Salesforce 8**. Location totals are Chennai 4; Bengaluru, Coimbatore, and Madurai 2 each; and Erode, Hyderabad, Salem, Thanjavur, Tiruchirappalli, Tirunelveli, and Vellore 1 each.

Source: `final-target-ui-data.json`, captured by the browser workflow. The source arrays are ordered Department, Email, Employee ID, Employee Name, Location. The derived file `Actual Final Target (UI Verified).csv` uses the target field order and sorts by Employee ID. It is a transcription of captured UI values, not a native ServiceNow CSV export. The original JSON and expected CSV were unchanged.

`final-target-validation.json` records the verification time, exact comparison counts, and SHA256 hashes for reproducibility. Transform-history counts and repeated-import behavior are evidenced separately by the run screenshots.
