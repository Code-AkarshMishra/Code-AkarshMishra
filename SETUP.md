# Setup (5 minutes)

1. Copy everything in this folder into your `Code-AkarshMishra/Code-AkarshMishra` repo:
   - `README.md`
   - `assets/` (all 26 SVG files)
   - `.github/workflows/` (snake.yml and blog-posts.yml)
   - `generate_assets.py` (optional, only needed to edit the visuals)
2. Commit to the `main` branch.
3. Repo -> Actions tab -> run **Generate Contribution Snake** and **Latest Blog Posts** once
   ("Run workflow"). The snake image and blog list stay empty until they run.
4. If Actions are disabled: Settings -> Actions -> General -> allow actions, and
   set Workflow permissions to "Read and write".

## Editing the visuals
Open `generate_assets.py`, change the DATA section at the top (project taglines, chips,
status, banner lines, section titles), run `python3 generate_assets.py`, commit `assets/`.

## Fix these two links
NeuroTrackAI and Mahakal Swarn Builder cards link to a repo *search* because I could not
confirm their exact repo names. Put the real URL in `PROJECTS` (generate_assets.py is only
for the card art) and in the matching `<a href>` in README.md.
