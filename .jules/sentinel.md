## 2024-07-06 - Insecure Deserialization in VisionEngine
**Vulnerability:** Unsafe deserialization of machine learning models via `pickle.load()` on `.pkl` files.
**Learning:** Legacy Python serialization formats like `pickle` (and by extension `joblib` in some cases) allow arbitrary code execution when unpickling malicious payloads.
**Prevention:** Avoid `pickle.load()`. Use secure, data-only formats like JSON for serialization (e.g., XGBoost's native `.json` model saving and loading methods).
