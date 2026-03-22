## 2024-05-24 - ML Model Deserialization Vulnerabilities
**Vulnerability:** Insecure deserialization of XGBoost models via `pickle` and `joblib`.
**Learning:** `joblib` and `pickle` can be abused to execute arbitrary code during model loading if the model file is tampered with by a malicious actor. This application was saving models as `.pkl` and reloading them using `pickle`.
**Prevention:** Always use the native `.save_model()` and `.load_model()` methods provided by libraries like XGBoost (with a `.json` extension) to ensure models are serialized securely without the risk of arbitrary code execution upon loading.
