# Profile README setup

## Upload

1. Extract the ZIP.
2. In `Code-AkarshMishra/Code-AkarshMishra`, replace `README.md` and upload `assets/` plus `.github/workflows/`, preserving paths.
3. Commit to `main`.
4. Go to **Settings → Actions → General → Workflow permissions** and enable read/write repository contents if the repository permits it.
5. Run **Actions → Generate Contribution Snake → Run workflow** once.

The supplied workstation image is named `assets/programmer.png`. The uploaded file had PNG image data despite its `.gif` filename, so it is saved with the correct `.png` extension and referenced correctly in the README.

## Workflows included

- `snake.yml`: Generates the contribution-snake SVGs into the `output` branch.
- `blog-posts.yml`: Manual-only, non-failing feed check. The previous scheduled blog-post action failed because `https://dev.to/feed/codeakarshmishmra` returned HTTP 404. The new workflow does not update the README until a working feed is confirmed.

## External images and counters

Trophies, streaks, stats, activity graph, typing text, profile-view counter, and some badges are delivered by external services. If a service is down or rate-limited, the README still renders its local banners, image, text, project links, and technology icons.

## XP score

The Level/XP panel is a custom, manually maintained profile metric based on the milestones and rules shown in the README. It is not an official GitHub score, official academic grade, or live calculation from GitHub's API.
