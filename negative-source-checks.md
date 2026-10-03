# Source preparation checks

Executed on 3 October 2026 against the supplied Excel workbook data and the five-field mapping contract. Invalid inputs were created only as disposable in-memory copies.

| Case | Check | Actual result | Status |
| --- | --- | --- | --- |
| NC01 | Blank Employee ID | Detected REQUIRED_VALUE; upload should be stopped until corrected | Pass |
| NC02 | Repeated source ID | Detected DUPLICATE_ID; upload should be stopped until corrected | Pass |
| NC03 | Wrong required header | Detected HEADERS; upload should be stopped until corrected | Pass |
| NC04 | Missing Name mapping | Detected FIELD_MAPPING; upload should be stopped until corrected | Pass |

Both original workbooks passed the same validator: 15 baseline rows and 4 update rows. Original files were not changed, and invalid data was not uploaded.

These checks run before import. They do not establish an automatic rejection rule inside ServiceNow.

Reproduce with Python 3 from the extracted project ZIP:

```text
python qa/validate_import_sources.py --data-dir data --output-dir evidence
```

From the flat GitHub repository folder instead:

```text
python validate_import_sources.py --data-dir . --output-dir evidence
```
