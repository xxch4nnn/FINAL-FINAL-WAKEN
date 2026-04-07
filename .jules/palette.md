## 2024-05-24 - CV Camera Background Legibility & Discoverability
**Learning:** Raw text rendered directly over a dynamic camera feed is frequently illegible due to contrast conflicts. Furthermore, in full-screen or custom CV app windows, standard window controls may not be obvious, causing frustration if exit shortcuts aren't discoverable.
**Action:** Always use a 'text outline' pattern (thick black background stroke, thin colored fill) for OpenCV UI elements. Always render essential application keyboard shortcuts (e.g., "[ESC] Quit") persistently on-screen.
