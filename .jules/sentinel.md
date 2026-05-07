## 2024-05-20 - Insecure Deserialization in ML Artifact Loading
**Vulnerability:** The `VisionEngine` class was using Python's `pickle.load()` to deserialize machine learning models, which allows for arbitrary code execution if a malicious model file is provided.
**Learning:** Legacy ML pipelines often default to `pickle` or `joblib` for ease of serialization without considering the security implications of loading untrusted model artifacts.
**Prevention:** Always use safe native serialization formats (like `.json` for XGBoost models) and native loading methods (`load_model()`) that do not execute arbitrary code during deserialization.
