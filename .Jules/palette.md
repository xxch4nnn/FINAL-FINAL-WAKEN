
## 2024-05-18 - Text Contrast and Discoverability in Computer Vision UX
**Learning:** Raw colored text overlaid on live camera feeds (which have dynamic lighting and variable backgrounds) frequently fails WCAG contrast guidelines, leading to poor readability. Additionally, "invisible" UX (like keyboard shortcuts that aren't displayed) creates a discoverability barrier for users navigating custom computer vision tools.
**Action:** Always implement a `draw_text_with_outline` function to render a solid black stroke behind overlay text. Explicitly and persistently display vital keyboard shortcuts on-screen to ensure the interface is immediately usable and accessible without relying on external documentation.
