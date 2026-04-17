## 2024-04-18 - Improve UI Contrast and Discoverability
**Learning:** Text over a live camera feed lacks contrast and can be hard to read against light/busy backgrounds. Also, keyboard shortcuts are not discoverable without hints.
**Action:** Always use a "text outline" technique (thick black stroke, thin white/colored fill) when using `cv2.putText` and explicitly render essential keyboard shortcuts on-screen.
