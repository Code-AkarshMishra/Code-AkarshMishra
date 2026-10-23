# Workflow fix

The previous `Latest Blog Posts` workflow ran on a 6-hour schedule and called the DEV feed endpoint `https://dev.to/feed/codeakarshmishmra`. GitHub Actions logs reported HTTP 404 / zero blog posts, so it repeatedly failed. This package replaces that schedule with a manual-only check that logs a warning rather than failing. Confirm your DEV username/feed URL before enabling automatic publishing again.
