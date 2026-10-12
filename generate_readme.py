#!/usr/bin/env python3
"""Builds README.md from the data in generate_assets.py"""
import os
from generate_assets import PROJECTS

USER = "Code-AkarshMishra"
RAW = f"https://raw.githubusercontent.com/{USER}/{USER}/main/assets/"
HERE = os.path.dirname(os.path.abspath(__file__))


def asset(n):
    return RAW + n


def pic(dark, light, width=None, height=None, alt=""):
    size = (f' width="{width}"' if width else "") + (f' height="{height}"' if height else "")
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="{dark}"/>'
        f'<source media="(prefers-color-scheme: light)" srcset="{light}"/>'
        f'<img alt="{alt}" src="{dark}"{size}/></picture>'
    )


def skills(label, icons):
    d = f"https://skillicons.dev/icons?i={icons}&theme=dark"
    l = f"https://skillicons.dev/icons?i={icons}&theme=light"
    return f"<tr>\n<td><b>{label}</b></td>\n<td>{pic(d, l, alt=label)}</td>\n</tr>\n"


def cell(p, colspan=False):
    fname, name, _, _, _, repo, live = p
    btns = f'<a href="{repo}"><img src="{asset("btn-repo.svg")}" height="42" alt="{name} repository"/></a>'
    if live:
        btns += f'&nbsp;<a href="{live}"><img src="{asset("btn-live.svg")}" height="42" alt="{name} live demo"/></a>'
    w = "50%" if colspan else "100%"
    td = 'colspan="2" align="center"' if colspan else 'width="50%" align="center" valign="top"'
    return (
        f"<td {td}>\n"
        f'<a href="{repo}"><img src="{asset("p-" + fname + ".svg")}" width="{w}" alt="{name}"/></a><br/>\n'
        f"{btns}\n<br/>&nbsp;\n</td>"
    )


def build():
    o = []
    o.append(f'''<div align="center">
<img src="{asset("banner.svg")}" width="100%" alt="Akarsh Mishra, Full-Stack Developer and AI/ML Engineer"/>
</div>

<p align="center">
  <a href="https://code-akarshmishra.vercel.app/">Portfolio</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/code-akarshmishra/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://www.youtube.com/@code-akarshmishra">YouTube</a> &nbsp;·&nbsp;
  <a href="https://dev.to/codeakarshmishra">dev.to</a> &nbsp;·&nbsp;
  <a href="https://www.instagram.com/akarsh.mishra.45/">Instagram</a> &nbsp;·&nbsp;
  <a href="mailto:akarshmishra3145@gmail.com">Email</a>
</p>

## About

I build full-stack products and I'm getting deeper into AI and machine learning. I'm in the final year of B.Tech CSE at SRMU, Lucknow, and I was a finalist at HackWithUP '25.

- Building **ENROLE**, an AI interview simulator, and **MedRx**, which explains medical reports in plain language
- Working with the MERN stack, Java and Python
- Exploring 6G and machine learning
- Writing and teaching developer concepts on [YouTube](https://www.youtube.com/@code-akarshmishra) and [dev.to](https://dev.to/codeakarshmishra)
- Open to collaborations, open-source work and internships. [Book a call](https://topmate.io/codeakarshmishra/)

## Tech stack

<table>
''')
    for label, icons in [
        ("Languages", "js,ts,python,java,cpp,html,css"),
        ("Frontend", "react,nextjs,tailwind,figma"),
        ("Backend", "nodejs,express,fastapi,flask"),
        ("AI / ML", "pytorch,tensorflow,opencv"),
        ("Databases", "mongodb,postgres,mysql,redis"),
        ("Tools", "docker,git,github,linux,vercel,postman,vscode"),
    ]:
        o.append(skills(label, icons))
    o.append("</table>\n\n## Projects\n\n<table>\n")
    n = len(PROJECTS)
    for i in range(0, n - n % 2, 2):
        o.append("<tr>\n" + cell(PROJECTS[i]) + "\n" + cell(PROJECTS[i + 1]) + "\n</tr>\n")
    if n % 2:
        o.append("<tr>\n" + cell(PROJECTS[-1], colspan=True) + "\n</tr>\n")
    o.append(f'</table>\n\n<p align="center"><a href="https://github.com/{USER}?tab=repositories">See all repositories →</a></p>\n\n')

    # ---- stats: GitHub-native colours, light + dark variants ----
    streak_d = (f"https://streak-stats.demolab.com/?user={USER}&hide_border=false&background=161B22&border=30363D&stroke=30363D"
                "&ring=3FB950&fire=D29922&currStreakNum=E6EDF3&sideNums=E6EDF3&currStreakLabel=3FB950&sideLabels=8B949E&dates=8B949E")
    streak_l = (f"https://streak-stats.demolab.com/?user={USER}&hide_border=false&background=FFFFFF&border=D0D7DE&stroke=D0D7DE"
                "&ring=1A7F37&fire=BF8700&currStreakNum=1F2328&sideNums=1F2328&currStreakLabel=1A7F37&sideLabels=656D76&dates=656D76")
    base = "https://github-readme-stats.vercel.app/api"
    dark = "&title_color=3fb950&icon_color=3fb950&text_color=e6edf3&bg_color=161b22&border_color=30363d&text_bold=false"
    light = "&title_color=1a7f37&icon_color=1a7f37&text_color=1f2328&bg_color=ffffff&border_color=d0d7de&text_bold=false"
    stats = f"{base}?username={USER}&show_icons=true&count_private=true&include_all_commits=true&card_width=420"
    langs = f"{base}/top-langs/?username={USER}&layout=compact&langs_count=8&card_width=420"
    o.append(f'''## GitHub stats

<p align="center">
{pic(streak_d, streak_l, width="100%", alt="Contribution streak")}
</p>

<table>
<tr>
<td width="50%">{pic(stats + dark, stats + light, width="100%", alt="GitHub stats")}</td>
<td width="50%">{pic(langs + dark, langs + light, width="100%", alt="Top languages")}</td>
</tr>
</table>

''')
    snake = f"https://raw.githubusercontent.com/{USER}/{USER}/output/"
    o.append(f'<p align="center">\n{pic(snake + "github-snake-dark.svg", snake + "github-snake.svg", width="100%", alt="Contribution snake")}\n</p>\n\n')

    o.append('## Achievements\n\n<p align="center">\n')
    for name, slug, img in [
        ("Starstruck", "starstruck", "starstruck-default-b6610abad518"),
        ("Galaxy Brain", "galaxy-brain", "galaxy-brain-default-847262c21056"),
        ("Pull Shark", "pull-shark", "pull-shark-default-498c279a747d"),
        ("YOLO", "yolo", "yolo-default-be0bbff04951"),
        ("Quickdraw", "quickdraw", "quickdraw-default-39c6aec8ff89"),
    ]:
        o.append(f'  <a href="https://github.com/{USER}?achievement={slug}&tab=achievements"><img src="https://github.githubassets.com/assets/{img}.png" width="120" alt="{name}" title="{name}"/></a>\n')
    o.append("</p>\n\n")

    lc_d = "https://leetcard.jacoblin.cool/code_akarshmishra?theme=dark&font=Fira+Code&ext=contest"
    lc_l = "https://leetcard.jacoblin.cool/code_akarshmishra?theme=light&font=Fira+Code&ext=contest"
    o.append(f'''## Problem solving

<p align="center">
{pic(lc_d, lc_l, width="70%", alt="LeetCode stats")}
</p>

<p align="center">
  <a href="https://leetcode.com/u/code_akarshmishra/">LeetCode</a> &nbsp;·&nbsp;
  <a href="https://www.hackerrank.com/CodeAkarshMishra">HackerRank</a> (Java ★, Python ★★★)
</p>

<br/>

<img src="{asset("footer.svg")}" width="100%" alt="Build systems. Not just projects."/>
''')
    with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8") as f:
        f.write("".join(o))
    print("README.md written")


if __name__ == "__main__":
    build()
