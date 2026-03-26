## 2024-03-27 - [Text Outline for Live Feed Accessibility]
**Learning:** Live camera feeds often have unpredictable lighting and colors, making standard text overlays (like `cv2.putText`) difficult to read without a high-contrast background.
**Action:** When adding text over a live feed, always apply a 'text outline' technique by drawing a thick black stroke followed by a thin white (or colored) fill. This ensures legibility regardless of the background.
