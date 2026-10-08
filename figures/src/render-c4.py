import json,sys,html,textwrap
src,out,view=sys.argv[1],sys.argv[2],sys.argv[3]
v=json.load(open(src))['views'][view]
W,H=v['bounds']['width'],v['bounds']['height']
P=[f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="-24 -24 {W+48} {H+48}" width="{W+48}" height="{H+48}" font-family="Helvetica, Arial, sans-serif">',
   f'<rect x="-24" y="-24" width="{W+48}" height="{H+48}" fill="white"/>',
   '<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
   '<path d="M0,1 L9,5 L0,9 z" fill="#1a1a1a"/></marker></defs>']
def txt(s):
    if isinstance(s,dict): return s.get('txt') or s.get('md') or ''
    return s or ''
def esc(s): return html.escape(txt(s))
for n in sorted(v['nodes'],key=lambda z:z['level']):
    x,y,w,h=n['x'],n['y'],n['width'],n['height']
    grp = bool(n.get('children'))
    if grp:
        P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="4" fill="#FAFAFA" stroke="#9a9a9a" stroke-width="1.2" stroke-dasharray="6 4"/>')
        P.append(f'<text x="{x+w-14}" y="{y+26}" text-anchor="end" font-size="17" font-weight="bold" fill="#333">{esc(n.get("title"))}</text>')
        continue
    kind=n.get('kind')
    ext = kind in ('external','person')
    P.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="3" fill="{"#F2F2F2" if ext else "white"}" '
             f'stroke="#1a1a1a" stroke-width="{1.0 if ext else 1.4}" {"stroke-dasharray=\"5 3\"" if ext else ""}/>')
    lines=textwrap.wrap(txt(n.get("description")),38)
    assert len(lines) <= 6, f'Description too long: {n["id"]}'
    technology=txt(n.get('technology'))
    blk=26+len(lines)*22+(20 if technology else 0)
    top=y+(h-blk)/2+20
    P.append(f'<text x="{x+w/2}" y="{top}" font-size="19" font-weight="bold" text-anchor="middle" fill="#111">{esc(n.get("title"))}</text>')
    if technology:
        P.append(f'<text x="{x+w/2}" y="{top+22}" font-size="13" text-anchor="middle" fill="#555">{esc(technology)}</text>')
        top+=20
    for i,line in enumerate(lines):
        P.append(f'<text x="{x+w/2}" y="{top+26+i*22}" font-size="15" text-anchor="middle" fill="#444">{esc(line)}</text>')
for e in v['edges']:
    pts=e.get('points') or []
    if len(pts)<2: continue
    d='M '+' L '.join(f'{p[0]},{p[1]}' for p in pts)
    P.append(f'<path d="{d}" fill="none" stroke="#1a1a1a" stroke-width="1.5" marker-end="url(#a)"/>')
    b=e.get('labelBBox')
    if b and txt(e.get('label')):
        for i,line in enumerate(textwrap.wrap(txt(e.get('label')),30)):
            P.append(f'<text x="{b["x"]}" y="{b["y"]+14+i*19}" font-size="15" fill="#222">{esc(line)}</text>')
P.append('</svg>')
open(out,'w').write('\n'.join(P))
print(out,'|',len('\n'.join(P)),'bytes |',W,'x',H)
