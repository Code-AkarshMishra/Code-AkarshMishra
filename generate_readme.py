#!/usr/bin/env python3
"""
Builds README.md.   Run:  python3 generate_assets.py && python3 generate_readme.py

Project repo links come from PROJECTS and live links from LIVE (both in generate_assets.py).
"""
import os
from generate_assets import PROJECTS, LIVE

USER = "Code-AkarshMishra"
BRANCH = "main"
RAW = f"https://raw.githubusercontent.com/{USER}/{USER}/{BRANCH}/assets/"
HERE = os.path.dirname(os.path.abspath(__file__))


def asset(name):
    return RAW + name


def pic(dark, light, width=None, height=None, alt=""):
    """<picture> that follows the viewer's GitHub theme (dark / light)."""
    size = (f' width="{width}"' if width else "") + (f' height="{height}"' if height else "")
    return (
        f'<picture>'
        f'<source media="(prefers-color-scheme: dark)" srcset="{dark}"/>'
        f'<source media="(prefers-color-scheme: light)" srcset="{light}"/>'
        f'<img alt="{alt}" src="{dark}"{size}/></picture>'
    )


def header(name, alt):
    return f'<img src="{asset("h-" + name + ".svg")}" width="100%" alt="{alt}"/>\n'


def skill_row(label, icons):
    d = f"https://skillicons.dev/icons?i={icons}&theme=dark"
    l = f"https://skillicons.dev/icons?i={icons}&theme=light"
    return f'<tr>\n  <td align="right"><h3>{label}</h3></td>\n  <td>{pic(d, l, height=64, alt=label)}</td>\n</tr>\n'


def project_cell(p):
    fname, _, name, _, _, _, _, repo = p
    live = LIVE.get(fname, "")
    btns = f'<a href="{repo}"><img src="{asset("btn-repo.svg")}" height="48" alt="{name} repository"/></a>'
    if live:
        btns += f'&nbsp;&nbsp;<a href="{live}"><img src="{asset("btn-live.svg")}" height="48" alt="{name} live demo"/></a>'
    return (
        f'<td width="50%" align="center" valign="top">\n'
        f'<a href="{repo}"><img src="{asset("p-" + fname + ".svg")}" width="100%" alt="{name}"/></a>\n'
        f'<br/>{btns}\n</td>'
    )


ACH = [
    ("Starstruck", "starstruck", "https://github.githubassets.com/assets/starstruck-default-b6610abad518.png"),
    ("Galaxy Brain", "galaxy-brain", "https://github.githubassets.com/assets/galaxy-brain-default-847262c21056.png"),
    ("Pull Shark", "pull-shark", "https://github.githubassets.com/assets/pull-shark-default-498c279a747d.png"),
    ("YOLO", "yolo", "https://github.githubassets.com/assets/yolo-default-be0bbff04951.png"),
    ("Quickdraw", "quickdraw", "https://github.githubassets.com/assets/quickdraw-default-39c6aec8ff89.png"),
]


def build():
    o = []
    # ---------------- header ----------------
    o.append(f'''<div align="center">

<img src="{asset("banner.svg")}" alt="Akarsh Mishra: Full-Stack Developer, AI/ML Engineer, Open Source Builder" width="100%"/>

<br/>

<img src="https://komarev.com/ghpvc/?username={USER}&label=PROFILE+VIEWS&color=00f7ff&style=for-the-badge&labelColor=0f2027" height="44"/>
<img src="https://img.shields.io/github/followers/{USER}?style=for-the-badge&logo=github&color=7b2ff7&labelColor=0f2027" height="44"/>
<img src="https://img.shields.io/badge/HackWithUP'25-FINALIST-ff6b35?style=for-the-badge&logo=rocket&logoColor=white&labelColor=0f2027" height="44"/>

<br/>

<a href="https://code-akarshmishra.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-00F7FF?style=for-the-badge&logo=vercel&logoColor=black" height="46"/></a>
<a href="https://www.linkedin.com/in/code-akarshmishra/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" height="46"/></a>
<a href="https://www.youtube.com/@code-akarshmishra"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" height="46"/></a>
<a href="https://topmate.io/codeakarshmishra/"><img src="https://img.shields.io/badge/Book%20a%20Call-FF6B35?style=for-the-badge&logo=googlemeet&logoColor=white" height="46"/></a>

</div>

<br/>
''')
    # ---------------- whoami / now / journey ----------------
    o.append(header("whoami", "whoami"))
    o.append(f'<div align="center">\n<img src="{asset("whoami.svg")}" width="100%" alt="About me"/>\n</div>\n\n<br/>\n')
    o.append(header("now", "Right now"))
    o.append(f'<div align="center">\n<img src="{asset("now.svg")}" width="100%" alt="What I am doing right now"/>\n</div>\n\n<br/>\n')
    o.append(header("journey", "My journey"))
    o.append(f'<div align="center">\n<img src="{asset("journey.svg")}" width="100%" alt="Timeline"/>\n</div>\n\n<br/>\n')

    # ---------------- stack ----------------
    o.append(header("stack", "Tech arsenal"))
    o.append('<table align="center">\n')
    for label, icons in [
        ("Languages", "js,ts,python,java,cpp,html,css"),
        ("Frontend", "react,nextjs,tailwind,figma"),
        ("Backend", "nodejs,express,fastapi,flask"),
        ("AI / ML", "pytorch,tensorflow,opencv"),
        ("Databases", "mongodb,postgres,mysql,redis"),
        ("DevOps &amp; Tools", "docker,git,github,linux,vercel,postman,vscode"),
    ]:
        o.append(skill_row(label, icons))
    o.append('</table>\n\n<br/>\n')

    # ---------------- projects ----------------
    o.append(header("projects", "Featured projects"))
    o.append('<table align="center">\n')
    for i in range(0, len(PROJECTS) - 1, 2):
        o.append("<tr>\n" + project_cell(PROJECTS[i]) + "\n" + project_cell(PROJECTS[i + 1]) + "\n</tr>\n")
    if len(PROJECTS) % 2:
        o.append('<tr>\n' + project_cell(PROJECTS[-1]).replace('width="50%"', 'colspan="2" width="100%"', 1)
                 .replace('<img src="' + asset("p-" + PROJECTS[-1][0] + ".svg") + '" width="100%"',
                          '<img src="' + asset("p-" + PROJECTS[-1][0] + ".svg") + '" width="50%"') + '\n</tr>\n')
    o.append('</table>\n\n')
    o.append(f'<div align="center">\n<a href="https://github.com/{USER}?tab=repositories"><img src="https://img.shields.io/badge/Explore%20all%20repositories%20→-0f2027?style=for-the-badge&labelColor=0f2027&color=00f7ff" height="46"/></a>\n</div>\n\n<br/>\n')

    # ---------------- stats (theme aware) ----------------
    o.append(header("stats", "GitHub stats"))
    streak_d = f"https://streak-stats.demolab.com/?user={USER}&theme=tokyonight&hide_border=true&background=0D1117&ring=00F7FF&fire=FF6B35&currStreakLabel=00F7FF"
    streak_l = f"https://streak-stats.demolab.com/?user={USER}&theme=default&hide_border=true"
    stats_d = f"https://github-readme-stats.vercel.app/api?username={USER}&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&count_private=true&include_all_commits=true&rank_icon=github&card_width=420&text_bold=true"
    stats_l = f"https://github-readme-stats.vercel.app/api?username={USER}&show_icons=true&theme=default&hide_border=true&count_private=true&include_all_commits=true&rank_icon=github&card_width=420&text_bold=true"
    lang_d = f"https://github-readme-stats.vercel.app/api/top-langs/?username={USER}&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&langs_count=8&card_width=420&text_bold=true"
    lang_l = f"https://github-readme-stats.vercel.app/api/top-langs/?username={USER}&layout=compact&theme=default&hide_border=true&langs_count=8&card_width=420&text_bold=true"
    o.append(f'''<div align="center">

{pic(streak_d, streak_l, width="100%", alt="Streak stats")}

<table>
<tr>
  <td width="50%">{pic(stats_d, stats_l, width="100%", alt="GitHub stats")}</td>
  <td width="50%">{pic(lang_d, lang_l, width="100%", alt="Top languages")}</td>
</tr>
</table>

</div>

<br/>
''')

    # ---------------- snake ----------------
    snake = f"https://raw.githubusercontent.com/{USER}/{USER}/output/"
    o.append(header("snake", "Contribution snake"))
    o.append(f'<div align="center">\n{pic(snake + "github-snake-dark.svg", snake + "github-snake.svg", width="100%", alt="Contribution snake")}\n</div>\n\n<br/>\n')

    # ---------------- activity (self-hosted svg) ----------------
    o.append(header("activity", "Activity graph"))
    o.append(f'<div align="center">\n<img src="{asset("activity.svg")}" width="100%" alt="Contribution activity, last 31 days"/>\n</div>\n\n<br/>\n')

    # ---------------- analytics (theme aware) ----------------
    base = "https://github-profile-summary-cards.vercel.app/api/cards/"

    def card(kind, extra=""):
        d = f"{base}{kind}?username={USER}&theme=tokyonight{extra}"
        l = f"{base}{kind}?username={USER}&theme=default{extra}"
        return pic(d, l, width="100%", alt=kind)

    o.append(header("analytics", "Deep analytics"))
    o.append(f'''<div align="center">

<table>
<tr>
  <td width="50%" colspan="2" align="center">{card("profile-details")}</td>
</tr>
<tr>
  <td width="50%">{card("repos-per-language")}</td>
  <td width="50%">{card("most-commit-language")}</td>
</tr>
<tr>
  <td width="50%">{card("stats")}</td>
  <td width="50%">{card("productive-time", "&utcOffset=5.5")}</td>
</tr>
</table>

</div>

<br/>
''')

    # ---------------- achievements (official GitHub badges) ----------------
    o.append(header("achievements", "Achievements"))
    o.append('<div align="center">\n\n<table>\n<tr>\n')
    for name, slug, img in ACH:
        o.append(
            f'  <td align="center" width="20%">\n'
            f'    <a href="https://github.com/{USER}?achievement={slug}&tab=achievements"><img src="{img}" width="150" alt="{name}"/></a>\n'
            f'    <br/><b>{name}</b>\n  </td>\n'
        )
    o.append('</tr>\n</table>\n\n')
    o.append(f'<img src="https://img.shields.io/badge/HackWithUP\'25-Finalist-ff6b35?style=for-the-badge&logo=rocket&logoColor=white&labelColor=0f2027" height="46"/>\n')
    o.append(f'<a href="https://github.com/pulls?q=is%3Apr+author%3A{USER}"><img src="https://img.shields.io/badge/View%20my%20Pull%20Requests-→-7b2ff7?style=for-the-badge&logo=github&logoColor=white&labelColor=0f2027" height="46"/></a>\n\n</div>\n\n<br/>\n')

    # ---------------- coding ----------------
    o.append(header("coding", "Competitive coding"))
    lc_d = "https://leetcard.jacoblin.cool/code_akarshmishra?theme=dark&font=Fira+Code&ext=contest"
    lc_l = "https://leetcard.jacoblin.cool/code_akarshmishra?theme=light&font=Fira+Code&ext=contest"
    o.append(f'''<div align="center">
{pic(lc_d, lc_l, width="75%", alt="LeetCode stats")}
<br/><br/>
<a href="https://www.hackerrank.com/CodeAkarshMishra"><img src="https://img.shields.io/badge/HackerRank-Java%20%E2%98%85%20%7C%20Python%20%E2%98%85%E2%98%85%E2%98%85-2EC866?style=for-the-badge&logo=hackerrank&logoColor=white&labelColor=0f2027" height="50"/></a>
</div>

<br/>
''')

    # ---------------- blog ----------------
    o.append(header("blog", "Latest writing"))
    o.append('''<!-- Auto-updated by .github/workflows/blog-posts.yml (dev.to feed) -->
<!-- BLOG-POST-LIST:START -->
<!-- BLOG-POST-LIST:END -->

<div align="center">
<a href="https://dev.to/codeakarshmishra"><img src="https://img.shields.io/badge/Read%20more%20on%20dev.to-→-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" height="46"/></a>
</div>

<br/>
''')

    # ---------------- connect + footer ----------------
    o.append(header("connect", "Let's connect"))
    o.append(f'''<div align="center">

<a href="https://code-akarshmishra.vercel.app/"><img src="https://img.shields.io/badge/Portfolio-00F7FF?style=for-the-badge&logo=vercel&logoColor=black" height="52"/></a>
<a href="https://www.linkedin.com/in/code-akarshmishra/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" height="52"/></a>
<a href="https://www.youtube.com/@code-akarshmishra"><img src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" height="52"/></a>
<a href="https://dev.to/codeakarshmishra"><img src="https://img.shields.io/badge/dev.to-0A0A0A?style=for-the-badge&logo=devdotto&logoColor=white" height="52"/></a>

<a href="https://www.instagram.com/akarsh.mishra.45/"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" height="52"/></a>
<a href="https://www.commudle.com/users/Code_AkarshMishra"><img src="https://img.shields.io/badge/Commudle-6C47FF?style=for-the-badge" height="52"/></a>
<a href="https://topmate.io/codeakarshmishra/"><img src="https://img.shields.io/badge/Topmate-FF6B35?style=for-the-badge" height="52"/></a>
<a href="mailto:akarshmishra3145@gmail.com"><img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" height="52"/></a>

</div>

<img src="{asset("footer.svg")}" width="100%" alt="Build systems. Not just projects."/>
''')
    with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(o))
    print("README.md written")


if __name__ == "__main__":
    build()
