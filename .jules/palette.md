## 2024-05-30 - WCAG Contrast & Keyboard Discoverability
**Learning:** Dynamic, variable-lighting camera feeds cause text to fail WCAG contrast guidelines. Also, on-screen keyboard shortcuts are not discoverable.
**Action:** Implemented a custom `draw_text_with_outline` function drawing a black outline behind the text across `main_runtime.py`, `VisionEngine.py`, and `src/runtime/vision_engine.py` to ensure readability. Added persistent UI hints at `(10, 30)` for keyboard shortcuts.
