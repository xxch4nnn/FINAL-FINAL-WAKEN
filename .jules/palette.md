## 2024-04-09 - Text Legibility in Live CV Interfaces
**Learning:** Standard text rendering (`cv2.putText`) often lacks contrast against unpredictable live camera feeds, making critical state information difficult or impossible to read. Additionally, hidden keyboard shortcuts (like pressing ESC to quit) make the interface hard to discover for new users.
**Action:** Always apply a "text outline" technique (a thick dark stroke behind the text) to ensure legibility across all backgrounds, and explicitly render essential shortcuts on-screen.
