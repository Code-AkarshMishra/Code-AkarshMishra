# Akarsh Retro Pixel Profile — Install guide

## Upload

1. Download and extract this ZIP.
2. In `Code-AkarshMishra/Code-AkarshMishra`, upload/replace the included `README.md`, `assets/` and `.github/workflows/` directories, keeping their exact paths.
3. Commit the changes to `main`.

## What the README includes

- Hand-made Minecraft / retro pixel-style banner and footer, in earthy grass, wood, dirt and emerald colours.
- Workstation illustration you supplied (file is stored locally as `assets/programmer.png`).
- Animated rotating role text for full-stack, MERN, Java, Python, open-source and freelance roles.
- Original icon resources from Devicon and skillicons.dev.
- Project links, live demo links, GitHub achievement links, trophies, streaks, stats, profile views, RPG-style XP/level and grade report card.
- Contribution snake and optional metrics/3D contribution workflows.

## Enable GitHub Actions

Open **Settings → Actions → General → Workflow permissions**. Grant read/write repository contents only if repository policy allows it. Then manually run the workflows from the **Actions** tab.

- `Generate Contribution Snake` publishes `github-snake.svg` and `github-snake-dark.svg` to the `output` branch.
- `Generate GitHub Metrics Map` is optional and depends on the upstream Metrics action. The default configuration only uses the standard token; additional private/contribution features may need extra token scopes.
- `Generate 3D Contribution Skyline` is optional and depends on its upstream action. If it fails because the upstream action or current workflow configuration changes, disable this optional workflow; it doesn't affect the README or snake workflow.

## Known external dependencies

Trophy, streak, stats, skillicons, typing SVG and profile-view count are third-party image services. Their uptime/rate limits are outside GitHub README control. Profile visits count only after the external counter image loads.

The README cannot host JavaScript games inline. Game buttons link to the Readme Games repository instead of faking an embedded game.

## Personal XP / grades

The XP amount (Level 12; 750 / 1,000), task XP and grade report are **personal gamification values**, not official GitHub measurements or a school result. Change them to match your current goals. Keep actual achievements linked to their original pages; don't label the RPG score as an official result.

## Link maintenance

Verify your profile handle links (LeetCode, HackerRank, DEV, LinkedIn) before sharing. Third-party usernames are preserved from the provided profile history; update any that are incorrect.

## Safe checks

- Confirm the profile repository is public.
- Check Actions logs for workflow-specific failures.
- If a dynamic image does not appear, open its image URL in a browser; distinguish an external service outage from an Actions run failure.
