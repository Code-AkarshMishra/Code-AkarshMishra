#!/usr/bin/env python3
"""Build README.md from the data in generate_assets.py"""
import os
from generate_assets import PROJECTS

USER = "Code-AkarshMishra"
RAW = f"https://raw.githubusercontent.com/{USER}/{USER}/main/assets/"
HERE = os.path.dirname(os.path.abspath(__file__))


def asset(name):
    return RAW + name


def pic(dark, light, width=None, height=None, alt=""):
    size = (f' width="{width}"' if width else "") + (f' height="{height}"' if height else "")
    return (
        f'<picture><source media="(prefers-color-scheme: dark)" srcset="{dark}"/>'
        f'<source media="(prefers-color-scheme: light)" srcset="{light}"/>'
        f'<img alt="{alt}" src="{dark}"{size}/></picture>'
    )


def skills(label, icons):
    dark = f"https://skillicons.dev/icons?i={icons}&theme=dark"
    light = f"https://skillicons.dev/icons?i={icons}&theme=light"
    return f"<tr>\n<td><b>{label}</b></td>\n<td>{pic(dark, light, alt=label)}</td>\n</tr>\n"


def cell(project):
    name, title, _, _, _, repo, live = project
    buttons = f'<a href="{repo}"><img src="{asset("btn-repo.svg")}" height="38" alt="Open {title} repository"/></a>'
    if live:
        buttons += f'&nbsp;<a href="{live}"><img src="{asset("btn-live.svg")}" height="38" alt="Open {title} live site"/></a>'
    return (
        '<td width="50%" align="center" valign="top">\n'
        f'<a href="{repo}"><img src="{asset("p-" + name + ".svg")}" width="100%" alt="{title} project card"/></a><br/>\n'
        f'{buttons}<br/>&nbsp;\n</td>'
    )


def build():
    output = [f'''<div align="center">
<img src="{asset("banner.svg")}" width="100%" alt="Akarsh Mishra coding at his workstation in a library"/>
</div>

<p align="center">
  <a href="https://github.com/{USER}?tab=repositories">ENTER THE REPOSITORY ARCADE</a> &nbsp;·&nbsp;
  <a href="https://code-akarshmishra.vercel.app/">Portfolio</a> &nbsp;·&nbsp;
  <a href="https://www.linkedin.com/in/code-akarshmishra/">LinkedIn</a> &nbsp;·&nbsp;
  <a href="https://www.youtube.com/@code-akarshmishmra">YouTube</a> &nbsp;·&nbsp;
  <a href="https://dev.to/codeakarshmishra">dev.to</a> &nbsp;·&nbsp;
  <a href="https://www.instagram.com/akarsh.mishra.45/">Instagram</a> &nbsp;·&nbsp;
  <a href="mailto:akarshmishmra3145@gmail.com">Email</a>
</p>

<table>
<tr>
<td width="25%" align="center"><a href="#the-workbench"><b>01 / WORKBENCH</b><br/>Current build + tools</a></td>
<td width="25%" align="center"><a href="#the-library"><b>02 / LIBRARY</b><br/>Projects + experiments</a></td>
<td width="25%" align="center"><a href="#academics-and-achievements"><b>03 / TROPHY ROOM</b><br/>Academics + milestones</a></td>
<td width="25%" align="center"><a href="#quest-log"><b>04 / QUEST LOG</b><br/>Stats + problem solving</a></td>
</tr>
</table>

## The Workbench

Full-stack builder from Lucknow, India, creating practical web products and exploring AI, machine learning, and computer vision. Currently pursuing a **B.Tech in Computer Science at SRMU (2023-2027)**.

<table>
<tr><td><b>ACTIVE QUEST</b></td><td>Building ENROLE, an AI-assisted interview and recruitment platform; developing MedRx to make medical reports easier to understand.</td></tr>
<tr><td><b>LOADOUT</b></td><td>MERN, JavaScript, Python, Java, React, Node.js, REST APIs, databases, computer vision</td></tr>
<tr><td><b>EXPLORING</b></td><td>Machine learning, facial emotion analysis, and 6G communication</td></tr>
</table>

<details>
<summary><b>Open the tool cabinet</b></summary>
<br/>
<table>
''']

    for label, icons in [
        ("Languages", "js,ts,python,java,cpp,html,css"),
        ("Frontend", "react,nextjs,tailwind,figma"),
        ("Backend", "nodejs,express,fastapi,flask"),
        ("AI / ML", "pytorch,tensorflow,opencv"),
        ("Databases", "mongodb,postgres,mysql,redis"),
        ("Tools", "docker,git,github,linux,vercel,postman,vscode"),
    ]:
        output.append(skills(label, icons))

    output.append("</table>\n</details>\n\n## The Library\n\nClick a project panel to open its repository.\n\n<table>\n")
    for index in range(0, len(PROJECTS), 2):
        output.append("<tr>\n" + cell(PROJECTS[index]) + "\n")
        if index + 1 < len(PROJECTS):
            output.append(cell(PROJECTS[index + 1]) + "\n")
        else:
            output.append('<td width="50%"></td>\n')
        output.append("</tr>\n")

    output.append(f'''</table>

<p align="center"><a href="https://github.com/{USER}?tab=repositories">Browse all repositories →</a></p>

## Academics and Achievements

<table>
<tr><td width="50%" valign="top">
<b>ACADEMIC SAVE FILE</b><br/><br/>
<b>B.Tech, Computer Science and Engineering</b><br/>
Shri Ramswaroop Memorial University (SRMU), Lucknow<br/>
2023-2027<br/><br/>
<a href="https://code-akarshmishra.vercel.app/#experience">Experience and leadership details ↗</a>
</td><td width="50%" valign="top">
<b>UNLOCKED MILESTONES</b><br/><br/>
Hack With Uttar Pradesh 2025 Grand Finale competitor; ENROLE project finalist<br/>
Vault of Codes: Web Development and Python internships; Python track offer letter<br/>
College Technical Club: event coordination and technical documentation<br/><br/>
<a href="https://code-akarshmishra.vercel.app/#certifications">View certifications ↗</a>
</td></tr>
</table>

<details>
<summary><b>Open the certificate case</b></summary>
<br/>
Deloitte Technology Simulation · Deloitte Cyber Simulation · Vault of Codes Web and Python internships · Hack With UP Grand Finale · Smart India Hackathon internal round · Google Ads certification
</details>

<p align="center">
  <a href="https://github.com/{USER}?achievement=starstruck&tab=achievements"><img src="https://github.githubassets.com/assets/starstruck-default-b6610abad518.png" width="92" alt="Starstruck GitHub achievement" title="Starstruck"/></a>
  <a href="https://github.com/{USER}?achievement=galaxy-brain&tab=achievements"><img src="https://github.githubassets.com/assets/galaxy-brain-default-847262c21056.png" width="92" alt="Galaxy Brain GitHub achievement" title="Galaxy Brain"/></a>
  <a href="https://github.com/{USER}?achievement=pull-shark&tab=achievements"><img src="https://github.githubassets.com/assets/pull-shark-default-498c279a747d.png" width="92" alt="Pull Shark GitHub achievement" title="Pull Shark"/></a>
  <a href="https://github.com/{USER}?achievement=yolo&tab=achievements"><img src="https://github.githubassets.com/assets/yolo-default-be0bbff04951.png" width="92" alt="YOLO GitHub achievement" title="YOLO"/></a>
  <a href="https://github.com/{USER}?achievement=quickdraw&tab=achievements"><img src="https://github.githubassets.com/assets/quickdraw-default-39c6aec8ff89.png" width="92" alt="Quickdraw GitHub achievement" title="Quickdraw"/></a>
</p>

## Quest Log

<p align="center">
  <a href="https://leetcode.com/u/code_akarshmishra/">LeetCode</a> &nbsp;·&nbsp;
  <a href="https://www.hackerrank.com/CodeAkarshMishra">HackerRank</a> (Java ★, Python ★★★) &nbsp;·&nbsp;
  <a href="https://github.com/{USER}?tab=achievements">All GitHub achievements</a>
</p>

## Player Stats

''')

    streak_dark = (f"https://streak-stats.demolab.com/?user={USER}&hide_border=false&background=161B22&border=30363D&stroke=30363D"
                   "&ring=3FB950&fire=D29922&currStreakNum=E6EDF3&sideNums=E6EDF3&currStreakLabel=3FB950&sideLabels=8B949E&dates=8B949E")
    streak_light = (f"https://streak-stats.demolab.com/?user={USER}&hide_border=false&background=FFFFFF&border=D0D7DE&stroke=D0D7DE"
                    "&ring=1A7F37&fire=BF8700&currStreakNum=1F2328&sideNums=1F2328&currStreakLabel=1A7F37&sideLabels=656D76&dates=656D76")
    base = "https://github-readme-stats.vercel.app/api"
    dark = "&title_color=3fb950&icon_color=3fb950&text_color=e6edf3&bg_color=161b22&border_color=30363d&text_bold=false"
    light = "&title_color=1a7f37&icon_color=1a7f37&text_color=1f2328&bg_color=ffffff&border_color=d0d7de&text_bold=false"
    stats = f"{base}?username={USER}&show_icons=true&count_private=true&include_all_commits=true&card_width=420"
    languages = f"{base}/top-langs/?username={USER}&layout=compact&langs_count=8&card_width=420"
    output.append(f'''<p align="center">
{pic(streak_dark, streak_light, width="100%", alt="Contribution streak")}
</p>

<table>
<tr>
<td width="50%">{pic(stats + dark, stats + light, width="100%", alt="GitHub stats")}</td>
<td width="50%">{pic(languages + dark, languages + light, width="100%", alt="Top languages")}</td>
</tr>
</table>

''')

    snake = f"https://raw.githubusercontent.com/{USER}/{USER}/output/"
    output.append(f'<p align="center">\n{pic(snake + "github-snake-dark.svg", snake + "github-snake.svg", width="100%", alt="Contribution snake")}\n</p>\n\n')
    leetcode_dark = "https://leetcard.jacoblin.cool/code_akarshmishra?theme=dark&font=Fira+Code&ext=contest"
    leetcode_light = "https://leetcard.jacoblin.cool/code_akarshmishra?theme=light&font=Fira+Code&ext=contest"
    output.append(f'''<p align="center">
{pic(leetcode_dark, leetcode_light, width="70%", alt="LeetCode stats")}
</p>

<br/>

<img src="{asset("footer.svg")}" width="100%" alt="Build systems. Not just projects."/>
''')

    with open(os.path.join(HERE, "README.md"), "w", encoding="utf-8") as readme:
        readme.write("".join(output))
    print("README.md written")


if __name__ == "__main__":
    build()
