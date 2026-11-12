#!/usr/bin/env python3
"""Validate the GitHub profile README and bundled assets.

Use --require-media after running sync_existing_media.py to verify that the
existing portfolio portrait and screenshots have been copied into assets/.
"""

from pathlib import Path
import argparse
import sys

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"

REQUIRED_SECTIONS = (
    "# Akarsh Mishra | Software Engineer",
    "## Engineering Profile",
    "## Featured Software Projects",
    "## Project Screenshots & Demonstrations",
    "## Technical Skills & Technology Stack",
    "## Research, Hackathons & Achievements",
    "## GitHub Statistics & Live Activity",
    "## Engineering Workflow",
    "## Let's Connect",
)

BUNDLED_ASSETS = (
    "assets/header-banner.svg",
    "assets/footer-banner.svg",
    "assets/programmer.gif",
    "assets/github-metrics.svg",
)

MEDIA_ASSETS = (
    "assets/photos/profile.jpg",
    "assets/projects/enrole.png",
    "assets/projects/medrx.png",
    "assets/projects/prepbot.png",
)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--require-media",
        action="store_true",
        help="Fail if the existing profile photograph and project screenshots are missing.",
    )
    args = parser.parse_args()

    if not README.is_file():
        print("ERROR: README.md is missing from the repository root.")
        return 1

    markdown = README.read_text(encoding="utf-8")
    missing_sections = [item for item in REQUIRED_SECTIONS if item not in markdown]
    missing_bundled = [item for item in BUNDLED_ASSETS if not (ROOT / item).is_file()]
    missing_media = [item for item in MEDIA_ASSETS if not (ROOT / item).is_file()]

    if missing_sections or missing_bundled or (args.require_media and missing_media):
        if missing_sections:
            print("Missing README sections:")
            for item in missing_sections:
                print(f"  - {item}")
        if missing_bundled:
            print("Missing bundled assets:")
            for item in missing_bundled:
                print(f"  - {item}")
        if args.require_media and missing_media:
            print("Missing profile photo / project screenshots:")
            for item in missing_media:
                print(f"  - {item}")
        return 1

    if missing_media:
        print("NOTE: Existing portfolio media has not been synced yet.")
        print("Run: python scripts/sync_existing_media.py")
    else:
        print(f"Verified {len(MEDIA_ASSETS)} photo/screenshot assets.")

    print(f"Profile validation passed. Verified {len(BUNDLED_ASSETS)} bundled assets.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
