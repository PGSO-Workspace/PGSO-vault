#!/usr/bin/env python3
"""Local reader for the vault: paper, matrices and figures, with hot reload.

Not part of the research record. Renders markdown through pandoc and serves
PDFs to the browser; nothing here writes to the workspace.

    python3 serve.py [port]      ->  http://127.0.0.1:8733
"""
import html, mimetypes, subprocess, sys
from functools import partial
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8733

SECTIONS = ["abstract", "introduction", "methods", "results", "discussion", "conclusions"]
NAV = [
    ("Paper (PDF, inglés)", "raw/handoff/paper/paper1-review-2026-09-16.pdf"),
    ("Paper (PDF, español)", "raw/handoff/paper/paper1-es-2026-09-16.pdf"),
    *[(f"§ {s}", f"md/manuscript/{s}.md") for s in SECTIONS],
    ("Matriz de auditoría de citas", "md/handoff/checks/citation-audit-matrix-2026-09-17.md"),
    ("Matriz de papers candidatos", "md/handoff/checks/candidate-paper-matrix-2026-09-19.md"),
    ("Recomendaciones de citación", "md/handoff/checks/citation-review-recommendations.md"),
    ("Figuras", "figs"),
]

CSS = """
:root{--bg:#fff;--fg:#1a1a1a;--mut:#666;--line:#e3e3e3;--accent:#0b5fff}
@media(prefers-color-scheme:dark){:root{--bg:#141414;--fg:#e8e8e8;--mut:#9a9a9a;--line:#333;--accent:#7aa2ff}}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);
font:15px/1.65 -apple-system,Segoe UI,Roboto,sans-serif;display:flex;min-height:100vh}
nav{width:270px;flex:0 0 270px;border-right:1px solid var(--line);padding:18px 14px;
overflow:auto;position:sticky;top:0;height:100vh}
nav h1{font-size:13px;letter-spacing:.08em;text-transform:uppercase;color:var(--mut);margin:0 0 14px}
nav a{display:block;padding:6px 9px;border-radius:6px;color:var(--fg);text-decoration:none;font-size:14px}
nav a:hover{background:var(--line)}nav a.on{background:var(--accent);color:#fff}
main{flex:1;min-width:0;padding:30px 44px;max-width:900px}
iframe{width:100%;height:calc(100vh - 60px);border:1px solid var(--line);border-radius:8px}
table{border-collapse:collapse;width:100%;margin:14px 0;font-size:13.5px;display:block;overflow-x:auto}
th,td{border:1px solid var(--line);padding:6px 9px;text-align:left;vertical-align:top}
th{background:var(--line)}code{background:var(--line);padding:1px 5px;border-radius:4px;font-size:.9em}
pre{background:var(--line);padding:12px;border-radius:8px;overflow-x:auto}
img{max-width:100%;border:1px solid var(--line);border-radius:8px;margin:10px 0}
blockquote{border-left:3px solid var(--accent);margin:12px 0;padding:2px 14px;color:var(--mut)}
h1,h2,h3{line-height:1.25}h2{margin-top:30px;border-bottom:1px solid var(--line);padding-bottom:5px}
.stamp{color:var(--mut);font-size:12px;margin-bottom:18px}
"""

RELOAD = """<script>
let seen=null;
setInterval(async()=>{try{
  const t=await (await fetch('/mtime/'+PATH,{cache:'no-store'})).text();
  if(seen!==null&&t!==seen)location.reload(); seen=t;
}catch(e){}},1000);
</script>"""


def shell(page, path, body):
    links = "".join(
        f'<a href="/{h}" class="{"on" if h == page else ""}">{html.escape(t)}</a>' for t, h in NAV
    )
    return (f"<!doctype html><meta charset=utf-8><title>PGSO</title><style>{CSS}</style>"
            f"<nav><h1>PGSO · vault</h1>{links}</nav><main>{body}</main>"
            f"<script>const PATH={path!r};</script>{RELOAD}").encode()


class H(BaseHTTPRequestHandler):
    def log_message(self, *a): pass

    def send(self, data, ctype="text/html; charset=utf-8", code=200):
        self.send_response(code); self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(data)))
        self.send_header("Cache-Control", "no-store"); self.end_headers()
        self.wfile.write(data)

    def safe(self, rel):
        p = (ROOT / unquote(rel)).resolve()
        return p if ROOT in p.parents and p.is_file() else None

    def do_GET(self):
        route = urlparse(self.path).path.lstrip("/")
        kind, _, rel = route.partition("/")
        if route in ("", "index.html"):
            return self.send(shell("", "", "<h1>PGSO · lector local</h1>"
                                   "<p class=stamp>Elige algo en la izquierda. La página se recarga sola "
                                   "cuando el archivo cambia en disco.</p>"))
        if kind == "figs":
            imgs = sorted((ROOT / "handoff/paper/figure-drafts").glob("*.png"))
            body = "<h1>Figuras</h1>" + "".join(
                f"<h2>{html.escape(p.stem)}</h2><img src='/raw/handoff/paper/figure-drafts/{p.name}'>"
                for p in imgs)
            return self.send(shell("figs", "handoff/paper/figure-drafts", body))
        p = self.safe(rel)
        if not p:
            return self.send(b"<h1>404</h1>", code=404)
        if kind == "md":
            out = subprocess.run(["pandoc", "-f", "gfm", "-t", "html", str(p)],
                                 capture_output=True, text=True)
            stamp = f"<p class=stamp>{html.escape(rel)}</p>"
            return self.send(shell(route, rel, stamp + out.stdout))
        if kind == "mtime":
            return self.send(str(p.stat().st_mtime).encode(), "text/plain")
        if kind == "raw":
            ctype = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
            if ctype == "application/pdf" and "embed" not in urlparse(self.path).query:
                return self.send(shell(route, rel, f"<iframe src='/raw/{rel}?embed'></iframe>"))
            return self.send(p.read_bytes(), ctype)
        return self.send(b"<h1>404</h1>", code=404)


if __name__ == "__main__":
    print(f"http://127.0.0.1:{PORT}   (ctrl-c para parar)")
    ThreadingHTTPServer(("127.0.0.1", PORT), H).serve_forever()
