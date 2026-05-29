## 2024-05-18 - Improve Text Contrast for Variable Backgrounds
**Learning:** Text overlays on dynamic camera feeds often fail WCAG contrast guidelines due to varying brightness levels, making the UI inaccessible for users with visual impairments.
**Action:** Always implement a custom `draw_text_with_outline` function that renders a solid black outline behind text overlays to guarantee sufficient contrast against any background lighting condition.
