# Profile Photography, Screenshots & GIF Guide

The profile README already references the current public portfolio portrait and three screenshots. Use these folders to add the additional media you send later.

## Existing photo and screenshot sources

- Profile photograph: `public/profile.jpg` in the existing Next.js portfolio repository.
- ENROLE screenshot: `public/projects/enrole.png`.
- MedRx screenshot: `public/projects/medrx.png`.
- Prepbot.ai screenshot: `public/projects/prepbot.png`.

These images are referenced through the repository's raw GitHub URLs. The package does not replace or copy the existing Next.js `public/` directory.

## Where new media belongs

```text
assets/
├── photos/
│   ├── profile-portrait.jpg
│   ├── hackathon-team.jpg
│   ├── research-presentation.jpg
│   └── tech-club-event.jpg
├── projects/
│   ├── enrole-dashboard.png
│   ├── medrx-report-view.png
│   ├── neurotrack-session.png
│   ├── weathergpt-dashboard.png
│   └── framesutra-workspace.png
└── demos/
    ├── enrole-demo.gif
    ├── medrx-demo.gif
    ├── neurotrack-demo.gif
    └── framesutra-demo.gif
```

## Recommended source quality

- Portrait: original JPG or PNG, square/portrait crop, clear face, clean background.
- Event photography: original high-resolution JPG/PNG. Keep captions factual and include the event name/year.
- Project screenshots: PNG or WebP, at least 1200 px wide where possible. Hide secrets, emails, API keys, personal records, and user data.
- Demo GIFs: short, focused, optimized, ideally 5–12 seconds and below a few MB.
- Screen recordings: MP4 is preferable for longer walkthroughs; link to a public demo/video rather than embedding a large file.

## Adding your files

Upload media into the matching folder, then add a descriptive image reference to the corresponding README section. Use meaningful alt text such as `ENROLE recruiter dashboard showing interview scheduling` rather than `image1`.

Only publish photos that you own or have permission to share.
