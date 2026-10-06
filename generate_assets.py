#!/usr/bin/env python3
"""
Generates the animated SVG assets used by README.md
Run:  python3 generate_assets.py     (writes into ./assets)

Edit the DATA section below, re-run, commit the assets folder.
"""
import os
import re
import math
from xml.sax.saxutils import escape as esc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "'JetBrains Mono','Fira Code','SFMono-Regular',Consolas,'Liberation Mono','Courier New',monospace"

CYAN, VIOLET, PINK, ORANGE, GREEN, YELLOW = "#00f7ff", "#7b2ff7", "#ff4ecd", "#ff6b35", "#2ee59d", "#ffd24a"
BG, PANEL = "#0b1020", "#10172a"

# ───────────────────────── DATA (edit me) ─────────────────────────
BANNER_LINES = [
    "Building scalable AI systems",
    "Cognitive AI  ·  NeuroTrackAI",
    "Making medical documents human  ·  MedRx",
    "AI interview practice  ·  ENROLE",
    "Exploring 6G + Machine Learning",
]

# (file, emoji, name, tagline lines, chips, status, accent, link)
GH = "https://github.com/Code-AkarshMishra"
PROJECTS = [
    ("enrole", "🎤", "ENROLE",
     ["AI-powered interview simulator"],
     ["AI", "Python", "Interview Prep"], "In Development", CYAN, f"{GH}/ENROLE"),
    ("medrx", "🏥", "MedRx",
     ["AI that turns medical reports into", "patient-friendly explanations"],
     ["AI / NLP", "HealthTech", "JavaScript"], "In Development", PINK, f"{GH}/MedRx"),
    ("neurotrackai", "🧠", "NeuroTrackAI",
     ["Cognitive load detector", "powered by machine learning"],
     ["Machine Learning", "Python", "Research"], "Research", VIOLET, f"{GH}?tab=repositories&q=neuro"),
    ("weathergpt", "🌦️", "WeatherGPT",
     ["Conversational AI weather assistant"],
     ["LLM", "API", "JavaScript"], "Project", ORANGE, f"{GH}/WeatherGPT"),
    ("prepbot", "🤖", "PrepBot.AI",
     ["Hyper-personalized learning platform"],
     ["EdTech", "Adaptive AI", "JavaScript"], "Project", GREEN, f"{GH}/Prepbot.ai"),
    ("mahakal", "🕉️", "Mahakal Swarn Builder",
     ["Open-source project built", "with and for the community"],
     ["Open Source", "Community"], "Open Source", YELLOW, f"{GH}?tab=repositories&q=mahakal"),
    ("sparsh", "🛒", "Sparsh Trading",
     [".shop  ·  open-source storefront"],
     ["Open Source", "E-Commerce", "TypeScript"], "Open Source", "#4da3ff", f"{GH}/Sparsh-Trading"),
]

SECTIONS = [  # (file, emoji, title, subtitle)
    ("whoami", "⌨️", "whoami", "who is behind the commits"),
    ("now", "📡", "Right Now", "what I'm up to these days"),
    ("journey", "🛤️", "My Journey", "from first commit to shipping products"),
    ("stack", "🛠️", "Tech Arsenal", "the tools I build with"),
    ("projects", "🔥", "Featured Projects", "things I've built and am building"),
    ("stats", "📊", "GitHub Stats", "numbers, streaks and languages"),
    ("snake", "🐍", "Contribution Snake", "eating my commits one square at a time"),
    ("activity", "📈", "Activity Graph", "the last 31 days of work"),
    ("analytics", "🔬", "Deep Analytics", "how and when I code"),
    ("achievements", "🏆", "Achievements", "badges and milestones"),
    ("coding", "🧩", "Competitive Coding", "problem solving on the side"),
    ("blog", "✍️", "Latest Writing", "fresh from dev.to"),
    ("connect", "🌐", "Let's Connect", "say hi, collaborate, or book a call"),
]


# ───────────────────────── helpers ─────────────────────────
def write(name, w, h, defs, body):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{esc(name)}">\n<defs>\n{defs}\n</defs>\n{body}\n</svg>\n'
    )
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)


def sweep_gradient(gid, c1, c2, dur=4, extra=""):
    """Linear gradient whose position slides, giving an animated border/line."""
    return (
        f'<linearGradient id="{gid}" x1="0" y1="0" x2="1" y2="0" gradientUnits="objectBoundingBox" {extra}>'
        f'<stop offset="0" stop-color="{c1}"/><stop offset="0.5" stop-color="{c2}"/><stop offset="1" stop-color="{c1}"/>'
        f'<animateTransform attributeName="gradientTransform" type="translate" from="-1 0" to="1 0" dur="{dur}s" repeatCount="indefinite"/>'
        f"</linearGradient>"
    )


def keytimes_cycle(i, n, fade=0.03):
    t0 = i / n
    t1 = t0 + fade
    t2 = (i + 1) / n - fade
    t3 = (i + 1) / n
    pts = [(t0, 0), (t1, 1), (t2, 1), (t3, 0)]
    if t0 > 0:
        pts.insert(0, (0, 0))
    if t3 < 1:
        pts.append((1, 0))
    kt = ";".join(f"{p[0]:.4f}" for p in pts)
    vals = ";".join(str(p[1]) for p in pts)
    return kt, vals


# ───────────────────────── 1. BANNER ─────────────────────────
def banner():
    W, H = 1200, 440
    defs = f"""
<linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
  <stop offset="0" stop-color="#070b18"/><stop offset="0.5" stop-color="#0f2740"/><stop offset="1" stop-color="#2a1668"/>
</linearGradient>
<linearGradient id="nm" x1="0" y1="0" x2="1" y2="0">
  <stop offset="0" stop-color="#ffffff"/><stop offset="0.55" stop-color="#9ffaff"/><stop offset="1" stop-color="#c9a8ff"/>
</linearGradient>
<radialGradient id="g1"><stop offset="0" stop-color="{CYAN}" stop-opacity=".45"/><stop offset="1" stop-color="{CYAN}" stop-opacity="0"/></radialGradient>
<radialGradient id="g2"><stop offset="0" stop-color="{VIOLET}" stop-opacity=".55"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></radialGradient>
<pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse">
  <path d="M48 0H0V48" fill="none" stroke="{CYAN}" stroke-opacity=".10" stroke-width="1"/>
  <animateTransform attributeName="patternTransform" type="translate" from="0 0" to="48 48" dur="5s" repeatCount="indefinite"/>
</pattern>
<filter id="glow" x="-20%" y="-50%" width="140%" height="200%"><feGaussianBlur stdDeviation="9" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>
{sweep_gradient("bar", "#0000", CYAN, 3.5)}
<linearGradient id="bar2" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>
<clipPath id="r"><rect width="{W}" height="{H}" rx="0"/></clipPath>
"""
    floaters = ""
    syms = [("{ }", 90, 120, 60), ("</>", 1060, 90, 56), ("AI", 170, 350, 54), ("01", 1010, 330, 54), ("6G", 600, 60, 46), ("λ", 330, 70, 50), ("#", 880, 290, 48)]
    for k, (s, x, y, size) in enumerate(syms):
        d = 4 + k * 0.7
        floaters += (
            f'<text x="{x}" y="{y}" font-family="{MONO}" font-size="{size}" fill="{CYAN}" fill-opacity=".16" font-weight="700">{esc(s)}'
            f'<animateTransform attributeName="transform" type="translate" values="0 0;0 -18;0 0" dur="{d}s" repeatCount="indefinite"/></text>'
        )
    cyc = ""
    n = len(BANNER_LINES)
    for i, line in enumerate(BANNER_LINES):
        kt, vals = keytimes_cycle(i, n)
        cyc += (
            f'<text x="{W/2}" y="326" text-anchor="middle" font-family="{MONO}" font-size="32" font-weight="700" fill="{CYAN}" opacity="{1 if i == 0 else 0}">'
            f'<tspan fill="{PINK}">❯ </tspan>{esc(line)}'
            f'<animate attributeName="opacity" values="{vals}" keyTimes="{kt}" dur="{n*3.4}s" repeatCount="indefinite"/></text>'
        )
    chips = ["4th Year CSE @ SRMU", "HackWithUP '25 Finalist", "Lucknow, India"]
    cx, chip_svg = 0, ""
    widths = [len(c) * 11.6 + 44 for c in chips]
    total = sum(widths) + 20 * (len(chips) - 1)
    x = (W - total) / 2
    for c, w in zip(chips, widths):
        chip_svg += (
            f'<rect x="{x:.1f}" y="364" width="{w:.1f}" height="42" rx="21" fill="#ffffff" fill-opacity=".07" stroke="{CYAN}" stroke-opacity=".45"/>'
            f'<text x="{x + w/2:.1f}" y="391" text-anchor="middle" font-family="{SANS}" font-size="19" fill="#d7e6ff">{esc(c)}</text>'
        )
        x += w + 20
    body = f"""
<g clip-path="url(#r)">
<rect width="{W}" height="{H}" fill="url(#bg)"/>
<rect width="{W}" height="{H}" fill="url(#grid)"/>
<circle cx="180" cy="120" r="260" fill="url(#g1)"><animate attributeName="cx" values="180;260;180" dur="9s" repeatCount="indefinite"/></circle>
<circle cx="1040" cy="330" r="300" fill="url(#g2)"><animate attributeName="cx" values="1040;940;1040" dur="11s" repeatCount="indefinite"/></circle>
{floaters}
<text x="{W/2}" y="152" text-anchor="middle" font-family="{SANS}" font-size="94" font-weight="800" fill="url(#nm)" filter="url(#glow)" letter-spacing="1">Akarsh Mishra</text>
<text x="{W/2}" y="214" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="500" fill="#cfe3ff">Full-Stack Developer  ·  AI/ML Engineer  ·  Open Source Builder</text>
<rect x="{W/2-150}" y="238" width="300" height="3" rx="1.5" fill="url(#bar2)"/>
{cyc}
{chip_svg}
<rect x="0" y="{H-5}" width="{W}" height="5" fill="#ffffff" fill-opacity=".05"/>
<rect x="0" y="{H-5}" width="{W}" height="5" fill="url(#bar)"/>
</g>
"""
    write("banner", W, H, defs, body)


# ───────────────────────── 2. SECTION HEADERS ─────────────────────────
def headers():
    for name, emoji, title, sub in SECTIONS:
        W, H = 1000, 130
        defs = f"""
<linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#8ef9ff"/></linearGradient>
<linearGradient id="sw" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}" stop-opacity="0"/><stop offset=".5" stop-color="{CYAN}"/><stop offset="1" stop-color="{VIOLET}" stop-opacity="0"/></linearGradient>
"""
        body = f"""
<rect x="0" y="118" width="{W}" height="3" rx="1.5" fill="{CYAN}" fill-opacity=".14"/>
<rect x="-300" y="116" width="300" height="6" rx="3" fill="url(#sw)">
  <animate attributeName="x" from="-300" to="{W}" dur="3.6s" repeatCount="indefinite"/>
</rect>
<path d="M20 30 V12 H38 M{W-20} 30 V12 H{W-38}" fill="none" stroke="{CYAN}" stroke-width="3" stroke-linecap="round" stroke-opacity=".7"/>
<text x="{W/2}" y="70" text-anchor="middle" font-family="{SANS}" font-size="50" font-weight="800" fill="url(#tg)">{emoji} {esc(title)}</text>
<text x="{W/2}" y="104" text-anchor="middle" font-family="{SANS}" font-size="22" fill="#8aa4c8">{esc(sub)}</text>
"""
        write("h-" + name, W, H, defs, body)


# ───────────────────────── 3. WHOAMI TERMINAL ─────────────────────────
CODE = [
    ("$ node whoami.js", "prompt"),
    ("const akarsh = {", "code"),
    ('  role:      "Full-Stack Developer & AI/ML Engineer",', "code"),
    ('  education: "B.Tech CSE · 4th Year @ SRMU",', "code"),
    ('  location:  "Lucknow, India",', "code"),
    ('  stack:     ["MERN", "Python", "Java", "FastAPI"],', "code"),
    ('  building:  ["ENROLE", "MedRx", "NeuroTrackAI"],', "code"),
    ('  research:  "6G + Machine Learning",', "code"),
    ("  achieved:  \"Finalist @ HackWithUP '25\",", "code"),
    ('  motto:     "Build systems. Not just projects.",', "code"),
    ("};", "code"),
]


def colorize(line, kind):
    if kind == "prompt":
        return f'<tspan fill="{GREEN}">$</tspan><tspan fill="#e6edf7">{esc(line[1:])}</tspan>'
    out = ""
    parts = re.split(r'("[^"]*")', line)
    for p in parts:
        if p.startswith('"') and p.endswith('"') and len(p) >= 2:
            out += f'<tspan fill="#9ef0a8">{esc(p)}</tspan>'
        else:
            m = re.match(r"^(\s*)(const)(\s.*)$", p)
            k = re.match(r"^(\s+)(\w+)(:)(.*)$", p)
            if m:
                out += f'{esc(m.group(1))}<tspan fill="{PINK}">const</tspan><tspan fill="#e6edf7">{esc(m.group(3))}</tspan>'
            elif k:
                out += f'{esc(k.group(1))}<tspan fill="{CYAN}">{esc(k.group(2))}</tspan><tspan fill="#7f8db0">{esc(k.group(3))}</tspan><tspan fill="#e6edf7">{esc(k.group(4))}</tspan>'
            else:
                out += f'<tspan fill="#e6edf7">{esc(p)}</tspan>'
    return out


def whoami():
    W = 1000
    STEP, TOP = 38, 108
    n = len(CODE)
    H = TOP + n * STEP + 50
    fs = 24
    cw = fs * 0.6
    clips, lines = "", ""
    DUR = 18
    for i, (line, kind) in enumerate(CODE):
        s = 0.02 + i * 0.045
        e = s + 0.04
        full = len(line) * cw + 20
        clips += (
            f'<clipPath id="c{i}"><rect x="30" y="{TOP + i*STEP - 28}" width="{full:.0f}" height="{STEP}">'
            f'<animate attributeName="width" values="0;0;{full:.0f};{full:.0f};0" keyTimes="0;{s:.3f};{e:.3f};0.94;1" dur="{DUR}s" repeatCount="indefinite"/>'
            f"</rect></clipPath>"
        )
        lines += (
            f'<g clip-path="url(#c{i})"><text x="40" y="{TOP + i*STEP}" font-family="{MONO}" font-size="{fs}" xml:space="preserve" '
            f'style="white-space:pre">{colorize(line, kind)}</text></g>'
        )
    cursor_y = TOP + n * STEP
    defs = f"""
{sweep_gradient("bd", VIOLET, CYAN, 5)}
<linearGradient id="bar" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="#18213a"/><stop offset="1" stop-color="#131a30"/></linearGradient>
{clips}
"""
    body = f"""
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="20" fill="#0a0f1d" stroke="url(#bd)" stroke-width="3"/>
<path d="M2 22 a20 20 0 0 1 20 -20 H{W-22} a20 20 0 0 1 20 20 V62 H2 Z" fill="url(#bar)"/>
<circle cx="38" cy="32" r="9" fill="#ff5f56"/><circle cx="68" cy="32" r="9" fill="#ffbd2e"/><circle cx="98" cy="32" r="9" fill="#27c93f"/>
<text x="{W/2}" y="39" text-anchor="middle" font-family="{MONO}" font-size="19" fill="#7f8db0">akarsh@lucknow: ~</text>
{lines}
<text x="40" y="{cursor_y}" font-family="{MONO}" font-size="{fs}" fill="{GREEN}">$ <tspan fill="{CYAN}">▍<animate attributeName="opacity" values="1;1;0;0" keyTimes="0;.5;.5;1" dur="1s" repeatCount="indefinite"/></tspan></text>
"""
    write("whoami", W, H, defs, body)


# ───────────────────────── 4. RIGHT NOW TILES ─────────────────────────
def now():
    tiles = [
        ("🔭", "BUILDING", "ENROLE · MedRx", CYAN),
        ("🧪", "RESEARCHING", "6G × Machine Learning", VIOLET),
        ("🌱", "LEARNING", "System design & LLMs", GREEN),
        ("✍️", "WRITING", "Articles on dev.to", ORANGE),
        ("🎥", "TEACHING", "YouTube tutorials", PINK),
        ("🤝", "OPEN TO", "Collabs & Internships", YELLOW),
    ]
    W, TW, TH, GAP = 1000, 485, 112, 20
    H = 3 * TH + 2 * GAP + 20
    defs = "".join(sweep_gradient(f"b{i}", c, "#ffffff", 3 + i * 0.4) for i, (_, _, _, c) in enumerate(tiles))
    body = ""
    for i, (em, lab, val, c) in enumerate(tiles):
        col, row = i % 2, i // 2
        x = 10 + col * (TW + 10 + 0)
        y = 10 + row * (TH + GAP)
        body += f"""
<g>
  <rect x="{x}" y="{y}" width="{TW}" height="{TH}" rx="20" fill="{PANEL}" stroke="url(#b{i})" stroke-width="2.5"/>
  <rect x="{x}" y="{y}" width="6" height="{TH}" rx="3" fill="{c}"/>
  <text x="{x+52}" y="{y+72}" text-anchor="middle" font-size="46">{em}
    <animateTransform attributeName="transform" type="translate" values="0 0;0 -6;0 0" dur="{3+i*0.5}s" repeatCount="indefinite"/></text>
  <text x="{x+105}" y="{y+45}" font-family="{SANS}" font-size="17" font-weight="700" letter-spacing="3" fill="{c}">{lab}</text>
  <text x="{x+105}" y="{y+84}" font-family="{SANS}" font-size="25" font-weight="700" fill="#f2f6ff">{esc(val)}</text>
  <circle cx="{x+TW-28}" cy="{y+28}" r="6" fill="{c}"><animate attributeName="r" values="5;9;5" dur="2s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;.3;1" dur="2s" repeatCount="indefinite"/></circle>
</g>"""
    write("now", W, H, defs, body)


# ───────────────────────── 5. JOURNEY TIMELINE ─────────────────────────
def journey():
    items = [
        ("Oct 2024", "First GitHub", "contribution", CYAN),
        ("2025", "HackWithUP '25", "Finalist 🏆", ORANGE),
        ("2026", "4th Year CSE", "@ SRMU, Lucknow", VIOLET),
        ("Now", "Building ENROLE,", "MedRx & NeuroTrackAI", GREEN),
    ]
    W, H = 1000, 270
    defs = f"""
<linearGradient id="ln" x1="0" x2="1"><stop offset="0" stop-color="{CYAN}"/><stop offset=".5" stop-color="{VIOLET}"/><stop offset="1" stop-color="{GREEN}"/></linearGradient>
"""
    xs = [125, 375, 625, 875]
    body = f'<rect x="125" y="118" width="750" height="6" rx="3" fill="#ffffff" fill-opacity=".08"/>'
    body += f'<rect x="125" y="118" width="750" height="6" rx="3" fill="url(#ln)"><animate attributeName="width" values="0;750;750;0" keyTimes="0;.5;.92;1" dur="9s" repeatCount="indefinite"/></rect>'
    for i, ((d, a, b, c), x) in enumerate(zip(items, xs)):
        t0 = 0.5 * i / 3
        body += f"""
<g opacity="1">
  <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="0;{t0:.3f};{t0+.06:.3f};.92;1" dur="9s" repeatCount="indefinite"/>
  <circle cx="{x}" cy="121" r="22" fill="{c}" fill-opacity=".18"><animate attributeName="r" values="18;26;18" dur="2.4s" repeatCount="indefinite"/></circle>
  <circle cx="{x}" cy="121" r="12" fill="{c}"/>
  <text x="{x}" y="70" text-anchor="middle" font-family="{SANS}" font-size="30" font-weight="800" fill="{c}">{esc(d)}</text>
  <text x="{x}" y="182" text-anchor="middle" font-family="{SANS}" font-size="25" font-weight="700" fill="#f2f6ff">{esc(a)}</text>
  <text x="{x}" y="214" text-anchor="middle" font-family="{SANS}" font-size="22" fill="#a9bbd8">{esc(b)}</text>
</g>"""
    write("journey", W, H, defs, body)


# ───────────────────────── 6. PROJECT CARDS ─────────────────────────
def project_cards():
    W, H = 460, 330
    for fname, emoji, name, tag, chips, status, accent, _ in PROJECTS:
        spw = len(status) * 9.6 + 46
        chips_svg, x = "", 28
        for c in chips:
            w = len(c) * 9.4 + 28
            if x + w > W - 24:
                break
            chips_svg += (
                f'<rect x="{x:.0f}" y="240" width="{w:.0f}" height="34" rx="17" fill="{accent}" fill-opacity=".14" stroke="{accent}" stroke-opacity=".55"/>'
                f'<text x="{x + w/2:.0f}" y="263" text-anchor="middle" font-family="{SANS}" font-size="16" font-weight="600" fill="#eaf1ff">{esc(c)}</text>'
            )
            x += w + 10
        tagsvg = "".join(
            f'<text x="28" y="{176 + i*30}" font-family="{SANS}" font-size="21" fill="#b9c8e2">{esc(t)}</text>' for i, t in enumerate(tag)
        )
        defs = f"""
<linearGradient id="cb" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#121a31"/><stop offset="1" stop-color="#0a0f1f"/></linearGradient>
{sweep_gradient("br", accent, "#ffffff", 4)}
<radialGradient id="bl"><stop offset="0" stop-color="{accent}" stop-opacity=".5"/><stop offset="1" stop-color="{accent}" stop-opacity="0"/></radialGradient>
<clipPath id="cp"><rect x="2" y="2" width="{W-4}" height="{H-4}" rx="22"/></clipPath>
"""
        body = f"""
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="22" fill="url(#cb)"/>
<g clip-path="url(#cp)">
  <circle cx="{W-40}" cy="40" r="150" fill="url(#bl)"><animate attributeName="r" values="130;170;130" dur="6s" repeatCount="indefinite"/></circle>
  <rect x="2" y="2" width="6" height="{H-4}" fill="{accent}"/>
</g>
<rect x="2" y="2" width="{W-4}" height="{H-4}" rx="22" fill="none" stroke="url(#br)" stroke-width="3"/>
<circle cx="64" cy="62" r="34" fill="{accent}" fill-opacity=".16" stroke="{accent}" stroke-opacity=".5"/>
<text x="64" y="76" text-anchor="middle" font-size="36">{emoji}</text>
<rect x="{W-28-spw:.0f}" y="44" width="{spw:.0f}" height="34" rx="17" fill="#ffffff" fill-opacity=".07"/>
<circle cx="{W-28-spw+20:.0f}" cy="61" r="5" fill="{accent}"><animate attributeName="opacity" values="1;.25;1" dur="1.8s" repeatCount="indefinite"/></circle>
<text x="{W-28-spw+34:.0f}" y="67" font-family="{SANS}" font-size="16" font-weight="600" fill="#d9e6ff">{esc(status)}</text>
<text x="28" y="140" font-family="{SANS}" font-size="33" font-weight="800" fill="#ffffff">{esc(name)}</text>
{tagsvg}
{chips_svg}
<text x="28" y="312" font-family="{SANS}" font-size="19" font-weight="700" fill="{accent}">View repository
  <tspan>→<animate attributeName="dx" values="4;12;4" dur="1.6s" repeatCount="indefinite"/></tspan></text>
"""
        write("p-" + fname, W, H, defs, body)


# ───────────────────────── 7. ACHIEVEMENTS ─────────────────────────
def achievements():
    items = [
        ("⭐", "Starstruck", "GitHub achievement", YELLOW),
        ("🧠", "Galaxy Brain", "GitHub achievement", VIOLET),
        ("🦈", "Pull Shark", "GitHub achievement", CYAN),
        ("🎲", "YOLO", "GitHub achievement", ORANGE),
        ("⚡", "Quickdraw", "GitHub achievement", GREEN),
        ("🏆", "HackWithUP '25", "Hackathon Finalist", PINK),
    ]
    W, TW, TH = 1000, 320, 165
    H = 2 * TH + 40
    defs = "".join(sweep_gradient(f"a{i}", c, "#ffffff", 3.5 + i * 0.3) for i, (_, _, _, c) in enumerate(items))
    body = ""
    for i, (em, t, s, c) in enumerate(items):
        col, row = i % 3, i // 3
        x = 10 + col * (TW + 15)
        y = 10 + row * (TH + 20)
        body += f"""
<rect x="{x}" y="{y}" width="{TW}" height="{TH}" rx="20" fill="{PANEL}" stroke="url(#a{i})" stroke-width="2.5"/>
<circle cx="{x+TW/2}" cy="{y+58}" r="40" fill="{c}" fill-opacity=".14"><animate attributeName="r" values="36;44;36" dur="3s" repeatCount="indefinite"/></circle>
<text x="{x+TW/2}" y="{y+74}" text-anchor="middle" font-size="52">{em}
  <animateTransform attributeName="transform" type="translate" values="0 0;0 -7;0 0" dur="{2.6+i*0.4}s" repeatCount="indefinite"/></text>
<text x="{x+TW/2}" y="{y+127}" text-anchor="middle" font-family="{SANS}" font-size="26" font-weight="800" fill="#ffffff">{esc(t)}</text>
<text x="{x+TW/2}" y="{y+153}" text-anchor="middle" font-family="{SANS}" font-size="17" fill="{c}">{esc(s)}</text>"""
    write("achievements", W, H, defs, body)


# ───────────────────────── 8. FOOTER ─────────────────────────
def footer():
    W, H = 1200, 240

    def wave(amp, phase, y0, period=600):
        pts = []
        for x in range(0, 2 * W + 20, 20):
            pts.append(f"{x},{y0 + amp*math.sin((x/period)*2*math.pi + phase):.1f}")
        return "M" + " L".join(pts) + f" L{2*W+20},{H} L0,{H} Z"

    defs = f"""
<linearGradient id="fw" x1="0" x2="1"><stop offset="0" stop-color="#0f2740"/><stop offset=".5" stop-color="#2c1a6b"/><stop offset="1" stop-color="#0f2740"/></linearGradient>
<linearGradient id="ft" x1="0" x2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#9ffaff"/></linearGradient>
"""
    body = f"""
<rect width="{W}" height="{H}" fill="none"/>
<g opacity=".35"><path d="{wave(14, 0, 120)}" fill="{CYAN}"><animateTransform attributeName="transform" type="translate" from="0 0" to="-600 0" dur="14s" repeatCount="indefinite"/></path></g>
<g opacity=".55"><path d="{wave(18, 1.6, 140)}" fill="{VIOLET}"><animateTransform attributeName="transform" type="translate" from="-600 0" to="0 0" dur="11s" repeatCount="indefinite"/></path></g>
<g><path d="{wave(12, 3.1, 165)}" fill="url(#fw)"><animateTransform attributeName="transform" type="translate" from="0 0" to="-600 0" dur="8s" repeatCount="indefinite"/></path></g>
<text x="{W/2}" y="120" text-anchor="middle" font-family="{SANS}" font-size="46" font-weight="800" fill="url(#ft)">⚡ Build systems. Not just projects.</text>
<text x="{W/2}" y="205" text-anchor="middle" font-family="{SANS}" font-size="22" fill="#cfe3ff">Thanks for stopping by  ·  Akarsh Mishra</text>
"""
    write("footer", W, H, defs, body)


if __name__ == "__main__":
    banner()
    headers()
    whoami()
    now()
    journey()
    project_cards()
    achievements()
    footer()
    print("Generated", len(os.listdir(OUT)), "SVG files in", OUT)
