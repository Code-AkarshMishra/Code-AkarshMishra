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
    ("lifelens", "LifeLens",
     ["Turns notices into a personal", "action plan"],
        ["JavaScript", "Productivity"], "Project", f"{GH}/LifeLens", ""),
    ("enrole", "ENROLE",
     ["AI interview and recruitment", "workflow platform"],
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
    ("audio-analyzer", "Audio Analyzer Pro",
     ["Real-time and post-recording", "audio analysis tool"],
     ["Python", "Audio"], "Project", f"{GH}/Audio-Analyzer-pro", ""),
    ("simon-says", "Simon Says",
     ["Animated memory game with", "sound and score tracking"],
        ["HTML", "CSS", "JavaScript"], "Project", f"{GH}/simon-says-game", ""),
]

STATUS_COLOR = {"Live": GREEN, "In development": AMBER, "Research": MUTED, "Project": MUTED}


def write(name, w, h, defs, body):
    svg = (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
        f'role="img" aria-label="{esc(name)}">\n<defs>\n{defs}\n</defs>\n{body}\n</svg>\n'
    )
    with open(os.path.join(OUT, name + ".svg"), "w", encoding="utf-8") as f:
        f.write(svg)


# ───────────────────────── animated developer room ─────────────────────────
def banner():
        W, H = 1200, 480
        defs = f"""
<pattern id="grid" width="32" height="32" patternUnits="userSpaceOnUse">
    <path d="M32 0H0V32" fill="none" stroke="{BORDER}" stroke-opacity=".35" stroke-width="1"/>
</pattern>
<linearGradient id="room" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#17252b"/><stop offset=".58" stop-color="{BG}"/><stop offset="1" stop-color="#28221d"/></linearGradient>
<linearGradient id="screen" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#183b3a"/><stop offset="1" stop-color="#101a21"/></linearGradient>
<filter id="glow"><feGaussianBlur stdDeviation="9"/></filter>
"""
        body = f"""
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#room)" stroke="{BORDER}" stroke-width="2"/>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="18" fill="url(#grid)"/>
<path d="M24 151H1176" stroke="#69796e" stroke-opacity=".42" stroke-width="2"/>
<text x="52" y="58" font-family="{MONO}" font-size="16" letter-spacing="2" fill="{GREEN}">PLAYER PROFILE  /  BUILD MODE</text>
<text x="50" y="116" font-family="{SANS}" font-size="54" font-weight="800" fill="{TEXT}">Akarsh Mishra</text>
<text x="53" y="143" font-family="{MONO}" font-size="17" fill="#b9c4c7">FULL-STACK DEVELOPER  +  AI / ML EXPLORER</text>
<g>
    <rect x="930" y="38" width="216" height="42" rx="8" fill="{PANEL}" stroke="#60746c"/>
    <circle cx="953" cy="59" r="6" fill="{GREEN}"><animate attributeName="opacity" values="1;.3;1" dur="1.8s" repeatCount="indefinite"/></circle>
    <text x="970" y="65" font-family="{MONO}" font-size="15" fill="{TEXT}">QUEST: IN PROGRESS</text>
</g>

<!-- library wall -->
<rect x="44" y="181" width="222" height="205" rx="6" fill="#342c25" stroke="#876b4e" stroke-width="3"/>
<rect x="51" y="188" width="208" height="7" fill="#b28a5a"/>
<rect x="51" y="252" width="208" height="7" fill="#b28a5a"/>
<rect x="51" y="321" width="208" height="7" fill="#b28a5a"/>
<rect x="51" y="379" width="208" height="7" fill="#b28a5a"/>
<g stroke="#201d1a" stroke-width="2">
    <rect x="63" y="205" width="18" height="45" rx="2" fill="#4e927f"/><rect x="84" y="198" width="23" height="52" rx="2" fill="#d08b4f"/><rect x="111" y="209" width="19" height="41" rx="2" fill="#bb6454"/><rect x="134" y="201" width="26" height="49" rx="2" fill="#577989"/><rect x="164" y="211" width="19" height="39" rx="2" fill="#c7a85c"/><rect x="187" y="199" width="28" height="51" rx="2" fill="#53836b"/><rect x="219" y="207" width="27" height="43" rx="2" fill="#ba7750"/>
    <rect x="63" y="270" width="27" height="45" rx="2" fill="#a55b50"/><rect x="94" y="266" width="18" height="49" rx="2" fill="#52847c"/><rect x="116" y="277" width="28" height="38" rx="2" fill="#d09c58"/><rect x="148" y="263" width="21" height="52" rx="2" fill="#687b9a"/><rect x="173" y="272" width="25" height="43" rx="2" fill="#b26b4e"/><rect x="202" y="266" width="42" height="49" rx="2" fill="#557b5f"/>
    <rect x="65" y="338" width="43" height="35" rx="2" fill="#bf8a49"/><rect x="112" y="333" width="23" height="40" rx="2" fill="#66899a"/><rect x="139" y="341" width="32" height="32" rx="2" fill="#a75c51"/><rect x="175" y="335" width="20" height="38" rx="2" fill="#4c8877"/><rect x="199" y="340" width="44" height="33" rx="2" fill="#bd9955"/>
</g>
<text x="65" y="235" font-family="{MONO}" font-size="9" fill="#f3ead7">IDEAS / NOTES / DOCS</text>

<!-- window and night sky -->
<rect x="884" y="174" width="255" height="146" rx="5" fill="#233a43" stroke="#af9270" stroke-width="6"/>
<rect x="895" y="185" width="233" height="124" fill="#253b46"/>
<circle cx="1078" cy="210" r="18" fill="#f0c978" opacity=".92"/>
<path d="M895 275L942 235 978 265 1022 222 1062 264 1102 240 1128 266V309H895Z" fill="#314c4c"/>
<path d="M895 289L937 257 974 280 1017 246 1051 281 1090 263 1128 288V309H895Z" fill="#253b35"/>
<path d="M1000 185V309M895 248H1128" stroke="#af9270" stroke-width="5"/>
<rect x="872" y="320" width="280" height="12" rx="3" fill="#ad8c63"/>

<!-- chair -->
<path d="M437 252Q437 235 454 235H515V306H451Q437 306 437 291Z" fill="#a24f3d" stroke="#d18458" stroke-width="3"/>
<rect x="448" y="302" width="105" height="17" rx="7" fill="#bd6847"/>
<path d="M472 318L462 385M532 318L548 385M449 385H567" fill="none" stroke="#c58e5e" stroke-width="7" stroke-linecap="round"/>

<!-- seated builder -->
<path d="M524 224Q526 204 550 203H590Q617 208 624 238L637 302H512Z" fill="#397a70" stroke="#75b09a" stroke-width="3"/>
<path d="M532 220Q547 208 563 212L584 237 573 257 544 244Z" fill="#e0a85f"/>
<path d="M543 206L541 193 574 193 578 213" fill="#d99b68"/>
<ellipse cx="560" cy="181" rx="31" ry="36" fill="#d79a67"/>
<path d="M530 182Q527 145 558 145Q591 147 591 179L581 174 570 158Q555 176 531 174Z" fill="#342c2a"/>
<path d="M544 185H551M566 185H573" stroke="#342c2a" stroke-width="3" stroke-linecap="round"/>
<path d="M552 199Q560 203 568 198" fill="none" stroke="#995d4b" stroke-width="2"/>
<path d="M533 233Q558 238 584 229" fill="none" stroke="#75b09a" stroke-width="4"/>

<!-- workstation -->
<rect x="656" y="184" width="183" height="124" rx="9" fill="#202c30" stroke="#a9a58b" stroke-width="4"/>
<rect x="668" y="196" width="159" height="99" rx="3" fill="url(#screen)"/>
<circle cx="748" cy="190" r="2.5" fill="#d0d4c0"/>
<path d="M683 215H735M683 230H787M683 245H759M683 260H775M683 276H724" stroke="#70c5a2" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<path d="M737 215H796M790 230H810M763 245H811M782 260H807M731 276H794" stroke="#e2b36e" stroke-width="3" stroke-linecap="round" opacity=".8"/>
<rect x="717" y="309" width="62" height="12" fill="#817b68"/>
<path d="M695 321H802" stroke="#c1aa7b" stroke-width="5" stroke-linecap="round"/>
<rect x="565" y="277" width="98" height="49" rx="5" fill="#283337" stroke="#d4bd91" stroke-width="3"/>
<path d="M575 287H651M580 296H628M586 305H642" stroke="#70c5a2" stroke-width="2.5" stroke-linecap="round"/>
<path d="M571 326H659L670 334H560Z" fill="#b49b71"/>
<path d="M573 335H657" stroke="#e4d4af" stroke-width="2"/>

<!-- typing arm, soft monitor glow, and editor caret -->
<path d="M580 238Q598 244 614 260L640 278" fill="none" stroke="#d79a67" stroke-width="13" stroke-linecap="round">
    <animate attributeName="d" values="M580 238Q598 244 614 260L640 278;M580 238Q601 240 617 255L643 274;M580 238Q598 244 614 260L640 278" dur="1.1s" repeatCount="indefinite"/>
</path>
<circle cx="748" cy="242" r="83" fill="#59bd9b" opacity=".08" filter="url(#glow)"><animate attributeName="opacity" values=".05;.13;.05" dur="3s" repeatCount="indefinite"/></circle>
<rect x="812" y="276" width="3" height="11" fill="#f1c26f"><animate attributeName="opacity" values="1;0;1" dur="1s" repeatCount="indefinite"/></rect>

<!-- desk, lamp, plant, and little build details -->
<rect x="311" y="340" width="787" height="18" rx="5" fill="#bb8a58" stroke="#e1b975" stroke-width="2"/>
<path d="M365 358L351 423M1048 358L1062 423" stroke="#9a7049" stroke-width="13" stroke-linecap="round"/>
<path d="M828 336L852 250 870 250" fill="none" stroke="#b9a275" stroke-width="6" stroke-linecap="round"/>
<path d="M850 251Q852 229 876 232Q899 235 898 253Z" fill="#d09a52" stroke="#f0c475" stroke-width="2"/>
<path d="M864 257L855 280" stroke="#f6d48b" stroke-width="6" opacity=".7"/>
<rect x="921" y="322" width="76" height="14" rx="3" fill="#586e59"/>
<path d="M959 322Q943 294 931 295Q934 317 959 322M960 322Q963 288 982 284Q985 311 960 322M958 322Q945 310 948 280Q967 292 958 322" fill="#77a879" stroke="#a2c181" stroke-width="2"/>
<rect x="316" y="364" width="122" height="50" rx="6" fill="#253136" stroke="#537368" stroke-width="2"/>
<text x="330" y="384" font-family="{MONO}" font-size="11" fill="{GREEN}">NEXT UP</text>
<text x="330" y="402" font-family="{MONO}" font-size="13" fill="{TEXT}">SHIP SOMETHING</text>
<text x="704" y="389" font-family="{MONO}" font-size="13" fill="#24302f">SRMU  /  LUCKNOW  /  2023-27</text>
<path d="M496 433H749" stroke="#70b59a" stroke-opacity=".55" stroke-width="2" stroke-dasharray="5 8"><animate attributeName="stroke-dashoffset" values="0;-26" dur="2s" repeatCount="indefinite"/></path>
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
