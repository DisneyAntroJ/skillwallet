"""Validate employee workbook inputs and demonstrate four pre-import checks.

Read-only for the supplied XLSX files. Invalid cases are disposable in-memory
copies and are never uploaded to ServiceNow.
"""
from pathlib import Path
from datetime import datetime, timezone
from copy import deepcopy
import argparse, collections, hashlib, json, re
from zipfile import ZipFile
from xml.etree import ElementTree as ET

HEADERS = ['Employee ID', 'Name', 'Email', 'Department', 'Location']
EXPECTED_MAP = {'Employee ID':'u_employee_id', 'Name':'u_employee_name',
                'Email':'u_email', 'Department':'u_department', 'Location':'u_location'}
NS = {'s':'http://schemas.openxmlformats.org/spreadsheetml/2006/main'}

def read_xlsx(path):
    with ZipFile(path) as z:
        shared=[]
        if 'xl/sharedStrings.xml' in z.namelist():
            shared=[''.join(t.text or '' for t in si.findall('.//s:t',NS)) for si in ET.fromstring(z.read('xl/sharedStrings.xml')).findall('s:si',NS)]
        sheet=ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        rows=[]
        for row in sheet.findall('.//s:sheetData/s:row',NS):
            cells={}
            for c in row.findall('s:c',NS):
                col=0
                for letter in re.match('[A-Z]+',c.attrib['r']).group(): col=col*26+ord(letter)-64
                raw=c.find('s:v',NS)
                value=raw.text if raw is not None else ''
                if c.get('t')=='s': value=shared[int(value)]
                if c.get('t')=='inlineStr': value=''.join(t.text or '' for t in c.findall('.//s:t',NS))
                cells[col-1]=value
            if cells and any(str(v).strip() for v in cells.values()):
                rows.append([cells.get(i,'') for i in range(max(5,max(cells)+1))])
    return rows

def validate(rows, field_map):
    errors=[]
    if not rows or rows[0]!=HEADERS:
        errors.append({'code':'HEADERS','message':'Expected the five headers in the agreed order.'})
        return errors
    seen={}
    for number,row in enumerate(rows[1:],2):
        if len(row)!=5: errors.append({'code':'ROW_WIDTH','row':number})
        for i,label in enumerate(HEADERS):
            if i>=len(row) or not str(row[i]).strip(): errors.append({'code':'REQUIRED_VALUE','row':number,'field':label})
        employee_id=str(row[0]).strip() if row else ''
        if employee_id and employee_id in seen:
            errors.append({'code':'DUPLICATE_ID','row':number,'first_row':seen[employee_id],'employee_id':employee_id})
        elif employee_id: seen[employee_id]=number
    for source,target in EXPECTED_MAP.items():
        if field_map.get(source)!=target:
            errors.append({'code':'FIELD_MAPPING','source':source,'expected_target':target,'actual_target':field_map.get(source)})
    return errors

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--data-dir',required=True,type=Path)
    parser.add_argument('--output-dir',required=True,type=Path)
    args=parser.parse_args()
    baseline=args.data_dir/'Sample Spreadsheet.xlsx'
    delta=args.data_dir/'Updated Sample Spreadsheet.xlsx'
    b=read_xlsx(baseline); u=read_xlsx(delta)
    assert len(b)==16 and len(u)==5
    controls=[]
    for path,rows in [(baseline,b),(delta,u)]:
        errors=validate(rows,EXPECTED_MAP)
        assert not errors,errors
        controls.append({'file':path.name,'rows':len(rows)-1,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'errors':errors,'status':'Pass'})
    tests=[]
    for code,label,mutation,expected in [
      ('NC01','Blank Employee ID',lambda rows,m:rows[1].__setitem__(0,''),'REQUIRED_VALUE'),
      ('NC02','Repeated source ID',lambda rows,m:rows[2].__setitem__(0,rows[1][0]),'DUPLICATE_ID'),
      ('NC03','Wrong required header',lambda rows,m:rows[0].__setitem__(1,'Full Name'),'HEADERS'),
      ('NC04','Missing Name mapping',lambda rows,m:m.pop('Name'),'FIELD_MAPPING')]:
        rows=deepcopy(b); mapping=dict(EXPECTED_MAP); mutation(rows,mapping)
        errors=validate(rows,mapping)
        assert len(errors)==1 and errors[0]['code']==expected,(code,errors)
        tests.append({'id':code,'scenario':label,'method':'Disposable in-memory copy; local pre-import validator','expected':expected,'detected':errors,'status':'Pass'})
    result={'verified_at_utc':datetime.now(timezone.utc).isoformat(),'scope':'Local source-preparation and mapping-contract checks. These are not ServiceNow server-side rejection tests.','controls':controls,'field_map_contract':EXPECTED_MAP,'negative_cases':tests,'negative_passed':len(tests),'negative_failed':0,'negative_not_run':0,'original_files_modified':False,'invalid_data_uploaded':False}
    args.output_dir.mkdir(parents=True,exist_ok=True)
    (args.output_dir/'negative-source-checks.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
    lines=['# Source preparation checks','', 'Executed on 3 October 2026 against the supplied Excel workbook data and the five-field mapping contract. Invalid inputs were created only as disposable in-memory copies.','', '| Case | Check | Actual result | Status |','| --- | --- | --- | --- |']
    for t in tests: lines.append(f"| {t['id']} | {t['scenario']} | Detected {t['expected']}; upload should be stopped until corrected | Pass |")
    lines+=['','Both original workbooks passed the same validator: 15 baseline rows and 4 update rows. Original files were not changed, and invalid data was not uploaded.','','These checks run before import. They do not establish an automatic rejection rule inside ServiceNow.','','From the extracted ZIP, run with Python 3:','','```text','python qa/validate_import_sources.py --data-dir data --output-dir evidence','```','']
    (args.output_dir/'negative-source-checks.md').write_text('\n'.join(lines),encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__': main()
