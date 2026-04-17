## 2024-05-24 - Fix Insecure Deserialization of ML Artifacts
**Vulnerability:** Insecure deserialization via `pickle` and `joblib` when loading Machine Learning models, scalers, and feature lists.
**Learning:** These formats allow arbitrary code execution upon deserialization if an attacker modifies the files. Models should be saved and loaded securely using JSON-based formats.
**Prevention:** Avoid `pickle` and `joblib` completely in data pipelines. Use XGBoost's native `save_model` and `load_model` (JSON) and save simple artifacts (like scaling logic parameters) explicitly as JSON.
