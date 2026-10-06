# Setup

## Upload to your profile repo  (Code-AkarshMishra/Code-AkarshMishra, branch: main)
Unzip first, then upload these (GitHub's "Add file -> Upload files" accepts folders by drag and drop):

- `README.md`
- `assets/`            (28 SVG files, they must be here or images show as broken)
- `.github/`           (3 folders of workflows + 1 script; if the browser skips hidden
                        folders, use "Create new file" and type the path, e.g.
                        `.github/workflows/snake.yml`, then paste the contents)
- `generate_assets.py`, `generate_readme.py`   (optional, only to edit things)

## Run the workflows once (Actions tab -> pick one -> Run workflow)
1. Generate Contribution Snake   -> creates the `output` branch used by the snake image
2. Activity Graph                -> replaces the placeholder with your real last-31-days chart
3. Latest Blog Posts             -> fills the dev.to list

If Actions is off: Settings -> Actions -> General -> Allow actions, and set
Workflow permissions to "Read and write permissions".

## Adding live links and fixing repo links
Open `generate_assets.py`:
- `PROJECTS`  last value of each row = repo link (NeuroTrackAI and Mahakal still point to a
              repo search because the exact repo names were not known)
- `LIVE`      paste a URL to show a "Live Demo" button on that card. Empty = no button.

Then run:
    python3 generate_assets.py
    python3 generate_readme.py
and commit README.md + assets/.

## Notes
- Achievement badge images come from github.githubassets.com. GitHub occasionally changes the
  hash in those file names; if a badge breaks, right-click the badge on your profile ->
  copy image address, and update `ACH` in generate_readme.py.
- Light/dark: all custom images carry their own dark panel (look the same in both themes);
  third-party cards and skill icons switch automatically with the viewer's GitHub theme.
