# Old workflow failure

The existing `Latest Blog Posts` workflow failed because its configured `https://dev.to/feed/codeakarshmishra` endpoint returned HTTP 404 in the inspected GitHub Actions logs (2026-10-23). This replacement package removes automated RSS publishing, so an incorrect feed cannot keep causing failed scheduled runs. `blog-posts.yml` is no longer included here.

To reintroduce blog posts later, first verify your current DEV RSS URL in a browser, restore a `<!-- BLOG-POST-LIST:START -->` / `<!-- BLOG-POST-LIST:END -->` marker pair in the README, and test with a manual workflow dispatch before adding a schedule.
