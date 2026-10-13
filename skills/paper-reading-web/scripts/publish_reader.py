"""Publish verified standalone HTML; retain latest + 0/1/2 historical releases."""
from pathlib import Path
import json,re,os,hashlib,base64,base64
from datetime import datetime,timezone,timedelta

def atomic(path,data):
    tmp=path.with_suffix(path.suffix+'.tmp');tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf-8');os.replace(tmp,path)

def publish(root,source,title,desktop=None):
    root=Path(root).resolve();source=Path(source).resolve()
    policy=json.loads((root/'reader-settings.json').read_text('utf-8'))
    count=policy.get('backup_count');assert type(count) is int and count in (0,1,2),'Choose backup policy first'
    folder=root/'versions';folder.mkdir(exist_ok=True)
    manifest=root/'reader-versions.json';data=json.loads(manifest.read_text('utf-8')) if manifest.exists() else {'sequence':0,'releases':[]}
    seq=data['sequence']+1;stamp=datetime.now(timezone(timedelta(hours=8)))
    short=re.sub(r'[<>:"/\\|?*\x00-\x1f]','',title).strip()[:60] or '论文'
    name=f'{short}_v{seq}.0_{stamp:%Y-%m-%d_%H%M%S}.html'
    content=source.read_text('utf-8')
    pdf=root/'source-paper.pdf'
    if pdf.exists():content=content.replace('href="source-paper.pdf"','href="data:application/pdf;base64,'+base64.b64encode(pdf.read_bytes()).decode()+'" download="source-paper.pdf"')
    label=f'v{seq}.0 · {stamp:%Y-%m-%d %H:%M} 北京时间'
    content=re.sub(r' data-reader-release="[^"]*"','',content)
    content=content.replace('<body','<body data-reader-release="'+label+'"',1)
    dest=folder/name;dest.write_text(content,'utf-8')
    latest=root/'paper-reading.html';temp=root/'paper-reading.html.tmp';temp.write_text(content,'utf-8');os.replace(temp,latest)
    rows=data['releases']+[{'file':name,'version':f'v{seq}.0','time':stamp.isoformat(),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}]
    removed=rows[:max(0,len(rows)-count-1)];rows=rows[-(count+1):]
    atomic(manifest,{'sequence':seq,'releases':rows,'backup_count':count})
    for row in removed:
        target=(folder/row['file']).resolve()
        if target.parent==folder.resolve() and target.suffix=='.html' and target.is_file():target.unlink()
    if desktop:
        share=Path(desktop).expanduser().resolve();share.parent.mkdir(parents=True,exist_ok=True)
        temp=share.with_suffix('.html.tmp');temp.write_text(content,'utf-8');os.replace(temp,share)
    return dest

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--root',required=True);p.add_argument('--source',required=True);p.add_argument('--title',required=True);p.add_argument('--desktop',help='Fixed desktop latest HTML path; overwrite only this exact file');a=p.parse_args();print(publish(a.root,a.source,a.title,a.desktop))
