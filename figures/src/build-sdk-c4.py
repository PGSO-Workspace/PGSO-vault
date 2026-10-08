"""Render the C4 source snapshot through PhDude, using installed local tools."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys

manifest = json.loads(Path('data/pgso-c4-sdk-20261008.json').read_text())
for name, item in manifest['files'].items():
    if hashlib.sha256(Path(name).read_bytes()).hexdigest() != item['sha256']:
        raise SystemExit(f'Source changed: register the updated snapshot first: {name}')
cli = sys.argv[1]
subprocess.run(['node', cli, 'validate', 'figures/src/c4'], check=True)
subprocess.run(['node', cli, 'export', 'json', '-o', 'figures/src/c4/model.json', 'figures/src/c4'], check=True)
model = json.loads(Path('figures/src/c4/model.json').read_text())
for view, name in [('c1_context', 'pgso-c1-context'), ('c2_containers', 'pgso-c2-containers'), ('c3_components', 'pgso-c3-components')]:
    assert model['views'][view]['nodes'], view
    subprocess.run([sys.executable, 'figures/src/render-c4.py', 'figures/src/c4/model.json', f'figures/out/{name}.svg', view], check=True)
    subprocess.run(['rsvg-convert', '-w', '1400', '-o', f'figures/out/{name}.png', f'figures/out/{name}.svg'], check=True)
