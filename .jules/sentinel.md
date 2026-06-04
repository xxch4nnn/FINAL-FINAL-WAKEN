## 2024-06-03 - Insecure Deserialization of ML Artifacts
**Vulnerability:** The runtime and training pipelines use `pickle` and `joblib` for deserialization of ML models and scalers, allowing arbitrary code execution (CWE-502).
**Learning:** Machine learning artifacts in legacy code often use insecure serialization formats by default.
**Prevention:** Ensure all models and scalers are loaded explicitly via secure mechanisms like JSON and `xgb.XGBClassifier().load_model()`.
