# Setup

Upload to your profile repo (Code-AkarshMishra/Code-AkarshMishra, branch main).
Unzip first, then drag these in via "Add file -> Upload files":

- README.md                      (replaces the old one)
- assets/                        (11 SVG files; images show as broken without this folder)
- .github/workflows/snake.yml    (if the hidden .github folder is skipped, use
                                  "Create new file", type .github/workflows/snake.yml and paste)

Then: Actions tab -> "Generate Contribution Snake" -> Run workflow (once).
It creates the `output` branch that the snake image reads from.

## Delete these old files from the repo if you uploaded the earlier versions
- .github/workflows/blog-posts.yml   (this is the one failing: dev.to/feed/... returned 404)
- .github/workflows/activity.yml
- .github/scripts/activity.py
- the old assets/ files that are no longer used (h-*.svg, now.svg, whoami.svg, journey.svg,
  activity.svg, achievements.svg). Easiest: delete the whole assets/ folder, then upload the new one.

## Editing
Project names, descriptions, tags, repo links and live links are all in generate_assets.py (PROJECTS).
Change them, then run:
    python3 generate_assets.py
    python3 generate_readme.py
and commit README.md + assets/.
(Or edit README.md directly for text changes.)

## Notes
- All custom images have their own dark background, so they look the same in light and dark mode.
  Stats cards, skill icons, LeetCode card and the snake switch with the viewer's GitHub theme.
- Achievement badge images come from github.githubassets.com. If GitHub changes a file hash and a
  badge breaks, copy the new image address from your profile and update generate_readme.py.
