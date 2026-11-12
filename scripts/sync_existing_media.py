#!/usr/bin/env python3
"""Copy existing Next.js portfolio media into the GitHub profile asset folders.

Run this from the root of the existing Code-AkarshMishra repository, after
merging this package. The original public/ files are left untouched.
"""

from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
MAPPINGS = {
    Path("public/profile.jpg"): Path("assets/photos/profile.jpg"),
    Path("public/projects/enrole.png"): Path("assets/projects/enrole.png"),
    Path("public/projects/medrx.png"): Path("assets/projects/medrx.png"),
    Path("public/projects/prepbot.png"): Path("assets/projects/prepbot.png"),
}


def main() -> int:
    copied = []
    kept = []
    missing = []

    for source_rel, destination_rel in MAPPINGS.items():
        source = ROOT / source_rel
        destination = ROOT / destination_rel
        if not source.is_file():
            missing.append(str(source_rel))
            continue

        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            print(f"KEEP    {destination_rel} (already exists; not overwritten)")
            kept.append(str(destination_rel))
            continue
        shutil.copy2(source, destination)
        copied.append((str(source_rel), str(destination_rel)))

    for source, destination in copied:
        print(f"COPIED  {source} -> {destination}")

    if missing:
        print("\nWARNING: Some existing portfolio media was not found:")
        for item in missing:
            print(f"  - {item}")
        print("You can add replacements manually using MEDIA-GUIDE.md.")

    if not copied and not kept:
        print("ERROR: No existing media was available. Run this script from the profile repo root.")
        return 1

    print(f"\nMedia sync complete: {len(copied)} copied, {len(kept)} preserved.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
