#!/usr/bin/env python3
"""Sequence diagram for the invocation protocol of Runtime::call.

Read from crates/pgso-actuator-http/src/runtime.rs at the pinned revision: the
check order is host clock, session, token consumption, permission ceiling,
governed catalog, binding, schema, then step-up. The recorded reason in the
right-hand column is the ExecutionReason variant that request produces.
"""
import sys

LANES = [("Agent", 120), ("PGSO runtime", 430), ("Trusted host", 700), ("Tool binding\n(sandbox)", 905)]
RX = 1085                     # left edge of the recorded-reason column
W, TOP, DY = 1410, 108, 41

# (kind, src, dst, label, recorded reason or None)
STEPS = [
    ("msg", 0, 1, "call(tool, arguments, session, token?)", None),
    ("msg", 1, 2, "read trusted monotonic clock", None),
    ("guard", 1, 1, "clock moved backwards  →  revoke every outstanding approval", "ClockRollback"),
    ("guard", 1, 1, "session matches the runtime session", "WrongSession"),
    ("self", 1, 1, "consume the presented token\n(single-use, even if the call is denied below)", None),
    ("guard", 1, 1, "tool within the host permission ceiling  Lₜ", "PermissionDenied"),
    ("guard", 1, 1, "tool within the governed catalog  Cₜ", "ToolUnavailable"),
    ("guard", 1, 1, "a binding is registered for the identifier", "UnknownTool"),
    ("guard", 1, 1, "arguments validate against the registered schema", "InvalidArguments"),
    ("self", 1, 1, "if the tool is marked for step-up:", None),
    ("guard", 1, 1, "a token was presented", "ConfirmationMissing"),
    ("guard", 1, 1, "token binds this tool, these exact arguments and the\ncurrent policy revision, and has not expired", "InvalidOrExpiredConfirmation"),
    ("msg", 1, 3, "run the handler inside the authorization operation", None),
    ("guard", 1, 1, "the callback neither panicked nor returned an error", "CallbackPanicked / CallbackFailed"),
    ("ret", 3, 1, "value", None),
    ("ret", 1, 0, "receipt  { outcome, bounded reason }", None),
]

def main(out):
    H = TOP + len(STEPS) * DY + 132
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
         'font-family="Helvetica, Arial, sans-serif"><rect width="100%" height="100%" fill="white"/>',
         '<defs><marker id="h" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
         'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="#1a1a1a"/></marker>'
         '<marker id="g" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" '
         'orient="auto-start-reverse"><path d="M0,1 L9,5 L0,9 z" fill="#8a8a8a"/></marker></defs>']
    bot = TOP + len(STEPS) * DY + 24
    # reason column
    p.append(f'<line x1="{RX-16}" y1="{TOP-46}" x2="{RX-16}" y2="{bot}" stroke="#d0d0d0" stroke-width="1"/>')
    p.append(f'<text x="{RX}" y="{TOP-52}" font-size="12" font-weight="bold" fill="#555">recorded reason on denial</text>')
    # lifelines
    for name, x in LANES:
        lines = name.split("\n")
        bh = 30 + (len(lines) - 1) * 16
        p.append(f'<rect x="{x-94}" y="{TOP-36-bh}" width="188" height="{bh}" fill="white" stroke="#1a1a1a" stroke-width="1.3"/>')
        for i, ln in enumerate(lines):
            p.append(f'<text x="{x}" y="{TOP-38-bh+21+i*16}" font-size="13" font-weight="bold" text-anchor="middle" fill="#111">{ln}</text>')
        p.append(f'<line x1="{x}" y1="{TOP-34}" x2="{x}" y2="{bot}" stroke="#9a9a9a" stroke-width="1" stroke-dasharray="5 4"/>')
    # activation bar: the whole authorization operation holds the runtime
    rx = LANES[1][1]
    p.append(f'<rect x="{rx-7}" y="{TOP+DY-14}" width="14" height="{13*DY}" fill="#EDEDED" stroke="#8a8a8a" stroke-width="0.9"/>')
    for i, (kind, s, d, label, reason) in enumerate(STEPS):
        y = TOP + i * DY
        xs, xd = LANES[s][1], LANES[d][1]
        if kind in ("msg", "ret"):
            dash = ' stroke-dasharray="6 4"' if kind == "ret" else ""
            x1, x2 = (xs + 8, xd - 8) if xd > xs else (xs - 8, xd + 8)
            p.append(f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="#1a1a1a" stroke-width="1.4" marker-end="url(#h)"{dash}/>')
            p.append(f'<text x="{(x1+x2)/2}" y="{y-8}" font-size="12.5" text-anchor="middle" fill="#111">{label}</text>')
        else:
            col = "#8a8a8a" if kind == "guard" else "#1a1a1a"
            p.append(f'<path d="M{xs+8},{y-9} h30 a7,7 0 0 1 0,14 h-30" fill="none" stroke="{col}" stroke-width="1.1" marker-end="url(#g)"/>')
            for j, ln in enumerate(label.split("\n")):
                p.append(f'<text x="{xs+52}" y="{y-6+j*15}" font-size="12.5" fill="{"#333" if kind=="guard" else "#111"}"'
                         f'{" font-weight=\"bold\"" if kind=="self" else ""}>{ln}</text>')
        if reason:
            p.append(f'<text x="{RX}" y="{y+4}" font-size="12" fill="#444" font-style="italic">{reason}</text>')
    note = ("Every check is a conjunction, so the reason recorded is the first one that fails, in this order. "
            "approve() runs the same checks, so no approval can be issued for a call that would be denied anyway. "
            "The callback executes inside the authorization operation, under the shared runtime lock, so no "
            "separately checked permit is handed to the caller for later use.")
    import textwrap
    for j, ln in enumerate(textwrap.wrap(note, 150)):
        p.append(f'<text x="26" y="{bot+34+j*17}" font-size="12" fill="#555">{ln}</text>')
    p.append('</svg>')
    open(out, "w").write("\n".join(p))
    print(out, "|", W, "x", H)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "figures/out/pgso-invocation-protocol-v1.svg")
