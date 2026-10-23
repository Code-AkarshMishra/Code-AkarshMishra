# Gamified GitHub Profile — setup

## Install the profile

1. Download and extract the ZIP.
2. Open `Code-AkarshMishra/Code-AkarshMishra` on GitHub.
3. Replace `README.md` with the included `README.md` and upload `assets/arcade-banner.svg`, `assets/arcade-footer.svg`, and `.github/workflows/` preserving paths.
4. Commit the changes to `main`.
5. Open **Settings → Actions → General → Workflow permissions**. Select **Read and write permissions** so the contribution-snake workflow can publish generated SVGs to the `output` branch.
6. Go to **Actions → Generate Contribution Snake → Run workflow** to create the first animation.
7. The README references the generated SVG at `output/github-snake.svg` and `output/github-snake-dark.svg`. The files show after a successful run.

## About workflow failures

The existing blog workflow failed because `https://dev.to/feed/codeakarshmishra` returned **HTTP 404** on the latest inspected run. The updated `Latest Blog Posts` workflow is intentionally a manual, non-blocking feed check; it does not try to edit the README or fail when the external feed is unavailable. Once the correct DEV RSS feed URL is confirmed, it can be re-enabled as an actual publisher.

The Snake workflow is kept separately. It needs write permission for repository contents and relies on external GitHub Actions/service availability. Avoid setting a schedule more frequently than needed.

## Optional: GitHub Metrics map

The README includes a placeholder for `metrics/github-metrics.svg`. GitHub README Markdown cannot generate this file by itself. To enable it, follow the upstream setup at https://github.com/lowlighter/metrics and add a workflow from that project. It is deliberately not included in the default Actions set so the profile does not gain another potentially brittle scheduled workflow.

## Mini-games

README files do not execute JavaScript. The Arcade Corner links to mini-games hosted by Readme Games instead of pretending there is an embedded game running inside GitHub.

## Before committing

- Confirm all repository links and public demos still point to the intended project.
- Edit the manual RPG Level/XP values when your milestones change.
- External stats services can rate-limit or go offline. A third-party image failing does not indicate that your GitHub Actions workflow failed.
