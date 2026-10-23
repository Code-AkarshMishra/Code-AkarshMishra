# Workflow diagnosis

The inspected `.github/workflows/blog-posts.yml` used `gautamkrishnar/blog-post-workflow@v1` to fetch `https://dev.to/feed/codeakarshmishra`. The latest inspected run (`Latest Blog Posts #59`, 2026-10-23) failed at that action step. Its log explicitly reported HTTP 404 from the feed, with zero posts fetched. The root cause is the configured feed URL returning 404, not Markdown rendering.

The new workflow changes the behaviour: it is manual-only and treats a missing feed as a notice. It will not update README or fail while the feed URL is broken. When the correct RSS URL is known, replace the check with a feed publisher and add matching `<!-- BLOG-POST-LIST:START -->` / `<!-- BLOG-POST-LIST:END -->` markers before enabling scheduled commits.
