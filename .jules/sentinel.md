## 2024-05-18 - [CRITICAL] Replace insecure deserialization with secure JSON

**Vulnerability:** Deserialization of untrusted data via `pickle.load` and `joblib.load` across `src/runtime/vision_engine.py`, `main_runtime.py`, and `src/training/train_gpu.py`. This allows arbitrary code execution if a maliciously crafted `.pkl` or `.joblib` model/scaler file is loaded.
**Learning:** Legacy ML saving practices often used `pickle` or `joblib` for convenience, but these mechanisms invoke arbitrary python methods when reconstructing object instances, posing a severe security risk, especially in pipelines where models are swapped or downloaded.
**Prevention:** Always use secure, language-agnostic serialization formats (like JSON) or framework-specific safe loaders (e.g., native XGBoost `.json` save/load). Use explicit dict configurations for simple structures like lists or parameter scalers rather than pickling the python objects.
