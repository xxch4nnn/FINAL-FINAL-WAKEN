## 2024-05-20 - Custom Text Outline Helper
**Learning:** WCAG contrast guidelines require text overlays against dynamic, variable-lighting camera feeds to have a custom `draw_text_with_outline` function (drawing a black outline behind the text) across `main_runtime.py`, `VisionEngine.py`, and `src/runtime/vision_engine.py`.
**Action:** Implement `draw_text_with_outline` as a local, inline function at the top of each relevant script to prevent Python import pathing issues and use it instead of `cv2.putText`.
