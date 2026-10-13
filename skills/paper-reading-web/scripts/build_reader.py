"""Assemble paper content with fixed reader components. Python standard library."""
from pathlib import Path
from html import escape
from html.parser import HTMLParser
import argparse
class Check(HTMLParser):
    def __init__(self): super().__init__(); self.ids=[]; self.links=[]; self.sections=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if a.get('id'): self.ids.append(a['id'])
        if tag=='a' and a.get('href','').startswith('#'): self.links.append(a['href'][1:])
        if tag=='section' and 'data-section' in a: self.sections+=1
p=argparse.ArgumentParser();p.add_argument('--content',type=Path,required=True);p.add_argument('--paper-id',required=True);p.add_argument('--out',type=Path,required=True);args=p.parse_args()
a=Path(__file__).resolve().parents[1]/'assets/reader-components';content=args.content.read_text('utf-8');c=Check();c.feed(content)
if not c.sections or len(c.ids)!=len(set(c.ids)) or set(c.links)-set(c.ids): raise SystemExit('Content requires sections, unique ids, and valid internal links')
s=(a/'shell.html').read_text('utf-8').replace('replace-with-unique-paper-id',escape(args.paper_id,quote=True))
s=s.replace('<!--由论文内容替换：section[data-section]与稳定id；图文面板按components.md生成-->',content)
s=s.replace('<link rel="stylesheet" href="reader.css">','<style>'+(a/'reader.css').read_text('utf-8')+'</style>')
s=s.replace('<script src="reader.js"></script>','<script>'+(a/'reader.js').read_text('utf-8')+'</script>')
c=Check();c.feed(s)
if len(c.ids)!=len(set(c.ids)): raise SystemExit('Content collides with component ids')
args.out.parent.mkdir(parents=True,exist_ok=True);args.out.write_text(s,'utf-8');print(args.out)
