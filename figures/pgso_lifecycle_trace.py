"""PhDude figure generator: recorded lifecycle traces, not an emotion measurement."""
import json
import os
import sys
import tarfile
from pathlib import Path

root = Path(os.environ["PHDUDE_WORKSPACE"])
archive = root / "data/pgso-lifecycle-reference-090fcd8.tar"
with tarfile.open(archive) as tar:
    episodes = {e["id"]: e for e in json.load(tar.extractfile("episodes.json"))}
    outputs = {o["id"]: o for o in json.load(tar.extractfile("pgso-outputs.json"))}

# The reference run's engine configuration, from the lifecycle_comparison example.
PRIOR, DELTA, CONF, HYST = 0.5, 0.3, 0.5, 3
PANELS = [
    ("sustained_and_recovery", "A. An accepted reading below the band retires the restriction"),
    ("low_confidence_holds_active", "B. The same value, not accepted, does not retire it"),
]
W, H = 1040, 700
X0, XW, VH = 120, 720, 120
TOOLS = ["quote", "human"]

svg = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" '
       'role="img" aria-labelledby="title desc">',
       '<title id="title">Recorded PGSO lifecycle traces for two contract episodes</title>',
       '<desc id="desc">Two recorded episodes at prior 0.5, deviation threshold 0.3, confidence threshold 0.5 '
       'and persistence 3. In both, three consecutive accepted readings at 0.95 put the quote tool out of the '
       'served catalog while human stays served throughout. In A a reading of 0.5 at confidence 0.9 is accepted '
       'and quote returns. In B a reading of the same value at confidence 0.49 abstains, and quote stays blocked. '
       'The values, confidences and allow or block actions are recorded; the run counter shown under each '
       'reading is derived by applying the documented persistence rule, and it agrees with the recorded '
       'transitions. These are governance transitions on authored episodes, not emotion accuracy.</desc>',
       f'<rect width="{W}" height="{H}" fill="white"/>', '<g font-family="Arial,sans-serif" fill="#222">',
       '<text x="40" y="36" font-size="22">Recorded lifecycle: what retires a restriction is an accepted reading</text>',
       f'<text x="40" y="60" font-size="13">Prior {PRIOR}, deviation threshold {DELTA}, confidence threshold '
       f'{CONF}, persistence {HYST}. Authored episodes; no human labels.</text>']

for panel, (eid, caption) in enumerate(PANELS):
    top = 108 + panel * 278
    obs = [e for e in episodes[eid]["events"] if e["kind"] == "observation"]
    times = sorted({e["timestamp_ms"] for e in episodes[eid]["events"]})
    step = XW / max(len(times) - 1, 1)
    xof = {t: X0 + i * step for i, t in enumerate(times)}
    svg.append(f'<text x="40" y="{top-12}" font-size="16">{caption}</text>')
    # accepted band and prior
    band_hi, band_lo = top + VH * (1 - (PRIOR + DELTA)), top + VH * (1 - (PRIOR - DELTA))
    svg.append(f'<rect x="{X0-30}" y="{band_hi}" width="{XW+60}" height="{band_lo-band_hi}" fill="#f0f4f8"/>')
    svg.append(f'<text x="{X0+XW+36}" y="{(band_hi+band_lo)/2+4}" font-size="11" fill="#667">within {DELTA}</text>')
    svg.append(f'<line x1="{X0-30}" y1="{top+VH*0.5}" x2="{X0+XW+30}" y2="{top+VH*0.5}" stroke="#889" '
               'stroke-width="1" stroke-dasharray="5 4"/>')
    svg.append(f'<text x="{X0-40}" y="{top+VH*0.5+4}" font-size="11" text-anchor="end" fill="#667">prior {PRIOR}</text>')
    for tick in (0.0, 0.5, 1.0):
        svg.append(f'<text x="{X0-40}" y="{top+VH*(1-tick)+4}" font-size="11" text-anchor="end" fill="#999">{tick:.1f}</text>')
    # observation trace
    pts, run, governed = [], 0, False
    for o in obs:
        x, y = xof[o["timestamp_ms"]], top + VH * (1 - o["value"])
        accepted = o["confidence"] >= CONF
        pts.append((x, y, accepted))
        if accepted:
            run = run + 1 if abs(o["value"] - PRIOR) >= DELTA else 0
            governed = run >= HYST
        label = "abstains" if not accepted else ("run %d" % run if run else "nominal")
        svg.append(f'<text x="{x}" y="{top+VH+22}" font-size="11" text-anchor="middle" '
                   f'fill="{"#888" if not accepted else "#333"}">{label}</text>')
        svg.append(f'<text x="{x}" y="{top+VH+38}" font-size="10" text-anchor="middle" fill="#999">'
                   f'q={o["confidence"]}</text>')
    line = " ".join(f'{"M" if i == 0 else "L"}{x},{y}' for i, (x, y, _) in enumerate(pts))
    svg.append(f'<path d="{line}" fill="none" stroke="#0072b2" stroke-width="1.6"/>')
    for x, y, accepted in pts:
        svg.append(f'<circle cx="{x}" cy="{y}" r="5.5" fill="{"#0072b2" if accepted else "white"}" '
                   f'stroke="{"#0072b2" if accepted else "#999"}" stroke-width="1.6"/>')
    # served-tool rows
    acts = {(r["timestamp_ms"], r["tool"]): r["action"] for r in outputs[eid]["outputs"]}
    for i, tool in enumerate(TOOLS):
        ry = top + VH + 68 + i * 34
        svg.append(f'<text x="{X0-40}" y="{ry+4}" font-size="12" text-anchor="end">{tool}</text>')
        svg.append(f'<line x1="{X0-30}" y1="{ry}" x2="{X0+XW+30}" y2="{ry}" stroke="#e6e6e6" stroke-width="1"/>')
        for t in times:
            action = acts.get((t, tool))
            if action is None:
                continue
            x = xof[t]
            if action == "block":
                svg.append(f'<rect x="{x-7}" y="{ry-7}" width="14" height="14" fill="#333"/>')
            else:
                svg.append(f'<circle cx="{x}" cy="{ry}" r="6" fill="white" stroke="#333" stroke-width="1.5"/>')
    for t in times:
        svg.append(f'<text x="{xof[t]}" y="{top+VH+126}" font-size="11" text-anchor="middle" fill="#666">{t} ms</text>')

svg += [f'<g transform="translate(40,{H-34})" font-size="12">',
        '<circle cx="6" cy="-4" r="6" fill="white" stroke="#333" stroke-width="1.5"/>'
        '<text x="20" y="0">served</text>',
        '<rect x="96" y="-11" width="14" height="14" fill="#333"/><text x="118" y="0">out of the served catalog</text>',
        '<circle cx="290" cy="-4" r="5.5" fill="#0072b2"/><text x="303" y="0">accepted reading</text>',
        '<circle cx="440" cy="-4" r="5.5" fill="white" stroke="#999" stroke-width="1.6"/>'
        '<text x="453" y="0">abstained: state and restriction both held</text>', '</g>',
        '</g></svg>']

out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "figures/out/pgso-lifecycle-trace-v1.svg"
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(svg) + "\n")
