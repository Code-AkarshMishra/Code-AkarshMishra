#!/usr/bin/env python3
"""
Builds the few custom images used by README.md  ->  ./assets
Run:  python3 generate_assets.py && python3 generate_readme.py

Everything you are likely to edit is in the DATA section.
"""
import os
from xml.sax.saxutils import escape as esc

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")
os.makedirs(OUT, exist_ok=True)

SANS = "'Segoe UI','Helvetica Neue',Helvetica,Arial,sans-serif"
MONO = "'SFMono-Regular',Consolas,'Liberation Mono','Courier New',monospace"

# GitHub-dark neutrals + one green accent (every image carries its own background,
# so it looks identical in light and dark mode)
BG, PANEL, BORDER = "#0d1117", "#161b22", "#30363d"
TEXT, MUTED = "#e6edf3", "#8b949e"
GREEN, AMBER = "#3fb950", "#d29922"

GH = "https://github.com/Code-AkarshMishra"

# ───────────────────────── DATA (edit me) ─────────────────────────
# file, name, description lines, chips, status, repo URL, live URL ("" = no Live button)
PROJECTS = [
    ("enrole", "ENROLE",
     ["AI-powered interview simulator"],
     ["AI", "Python"], "In development", f"{GH}/ENROLE", ""),
    ("medrx", "MedRx",
     ["Turns medical reports and prescriptions", "into patient-friendly explanations"],
     ["AI", "JavaScript"], "Live", f"{GH}/MedRx", "https://medrx-beta.vercel.app"),
    ("neurotrackai", "NeuroTrackAI",
     ["Real-time cognitive load and", "mental fatigue analyzer"],
     ["React", "Spring Boot", "OpenCV"], "Research", f"{GH}/CognitiveLoadDetector", ""),
    ("weathergpt", "WeatherGPT",
     ["AI-powered weather assistant"],
     ["Express", "FastAPI", "JavaScript"], "Project", f"{GH}/WeatherGPT", ""),
    ("prepbot", "PrepBot.AI",
     ["Hyper-personalized learning platform"],
     ["React", "JavaScript"], "Project", f"{GH}/Prepbot.ai", ""),
    ("mahakal", "Mahakal Swarn Builder",
     ["Open-source web app", "built with Next.js"],
     ["Next.js", "Open source"], "Live", f"{GH}/mahakalswarnbuilder", "https://mahakalswarnbuilder.vercel.app"),
    ("sparsh", "Sparsh Trading",
     ["Open-source storefront for", "Sparsh Trading"],
     ["TypeScript", "Open source"], "Live", f"{GH}/Sparsh-Trading", "https://sparshtrading.shop"),
]

STATUS_COLOR = {"Live": GREEN, "In development": AMBER, "Research": MUTED, "Project": MUTED}


def write(name, w, h, defs, body):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{esc(name)}">\n<defs>\n{defs}\n</defs>\n{body}\n</svg>\n'
    )
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)


# ───────────────────────── banner ─────────────────────────
def banner():
    W, H = 1200, 320
    defs = f"""
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse">
  <circle cx="2" cy="2" r="1.6" fill="{BORDER}"/>
</pattern>
<linearGradient id="fade" x1="0" x2="1"><stop offset="0" stop-color="{BG}" stop-opacity="1"/><stop offset=".55" stop-color="{BG}" stop-opacity=".92"/><stop offset="1" stop-color="{BG}" stop-opacity="0"/></linearGradient>
"""
    body = f"""
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{BG}" stroke="{BORDER}" stroke-width="2"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#dots)"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#fade)"/>
<text x="64" y="82" font-family="{SANS}" font-size="28" font-weight="600" fill="{AMBER}">Namaste, I'm</text>
<text x="60" y="168" font-family="{SANS}" font-size="84" font-weight="800" fill="{TEXT}">Akarsh Mishra</text>
<rect x="64" y="190" width="96" height="6" rx="3" fill="{GREEN}"/>
<text x="64" y="242" font-family="{SANS}" font-size="30" fill="{TEXT}">Full-Stack Developer  ·  AI/ML Engineer</text>
<text x="64" y="282" font-family="{SANS}" font-size="23" fill="{MUTED}">4th-year CSE @ SRMU, Lucknow  ·  HackWithUP '25 Finalist</text>
<g>
  <rect x="{W-372}" y="42" width="320" height="44" rx="22" fill="{PANEL}" stroke="{BORDER}" stroke-width="2"/>
  <circle cx="{W-342}" cy="64" r="7" fill="{GREEN}"><animate attributeName="opacity" values="1;.35;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <text x="{W-324}" y="71" font-family="{SANS}" font-size="20" fill="{TEXT}">Building ENROLE &amp; MedRx</text>
</g>
"""
    write("banner", W, H, defs, body)


# ───────────────────────── project cards ─────────────────────────
def project_cards():
    W, H = 460, 232
    for fname, name, desc, chips, status, repo, live in PROJECTS:
        st = "Live" if live else status
        col = STATUS_COLOR.get(st, MUTED)
        sw = len(st) * 9 + 36
        chips_svg, x = "", 28
        for c in chips:
            w = len(c) * 8.8 + 26
            if x + w > W - 20:
                break
            chips_svg += (
                f'<rect x="{x:.0f}" y="178" width="{w:.0f}" height="32" rx="16" fill="{BG}" stroke="{BORDER}" stroke-width="1.5"/>'
                f'<text x="{x + w/2:.0f}" y="199" text-anchor="middle" font-family="{SANS}" font-size="15" fill="{TEXT}">{esc(c)}</text>'
            )
            x += w + 8
        desc_svg = "".join(
            f'<text x="28" y="{108 + i*28}" font-family="{SANS}" font-size="19" fill="{MUTED}">{esc(t)}</text>' for i, t in enumerate(desc)
        )
        body = f"""
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="{PANEL}" stroke="{BORDER}" stroke-width="2"/>
<rect x="1" y="26" width="5" height="46" rx="2.5" fill="{GREEN}"/>
<text x="28" y="62" font-family="{SANS}" font-size="30" font-weight="700" fill="{TEXT}">{esc(name)}</text>
<circle cx="{W-28-sw+10:.0f}" cy="24" r="5" fill="{col}"/>
<text x="{W-28-sw+22:.0f}" y="30" font-family="{SANS}" font-size="15" fill="{col}">{esc(st)}</text>
{desc_svg}
{chips_svg}
"""
        write("p-" + fname, W, H, "", body)


# ───────────────────────── buttons ─────────────────────────
def buttons():
    W, H = 216, 48
    write("btn-repo", W, H, "", f"""
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="{PANEL}" stroke="#4b535d" stroke-width="2"/>
<text x="{W/2}" y="31" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="600" fill="{TEXT}">View repository</text>
""")
    write("btn-live", W, H, "", f"""
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="10" fill="#238636" stroke="#2ea043" stroke-width="2"/>
<text x="{W/2}" y="31" text-anchor="middle" font-family="{SANS}" font-size="19" font-weight="700" fill="#ffffff">Live demo  ↗</text>
""")


# ───────────────────────── footer ─────────────────────────
def footer():
    W, H = 1200, 110
    write("footer", W, H, "", f"""
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="{BG}" stroke="{BORDER}" stroke-width="2"/>
<rect x="{W/2-48}" y="22" width="96" height="5" rx="2.5" fill="{GREEN}"/>
<text x="{W/2}" y="70" text-anchor="middle" font-family="{SANS}" font-size="32" font-weight="700" fill="{TEXT}">Build systems. Not just projects.</text>
<text x="{W/2}" y="96" text-anchor="middle" font-family="{SANS}" font-size="17" fill="{MUTED}">Thanks for stopping by</text>
""")


if __name__ == "__main__":
    banner()
    project_cards()
    buttons()
    footer()
    print("Generated", len(os.listdir(OUT)), "SVG files")
