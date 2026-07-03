## 2025-02-24 - Insecure Deserialization in ML Pipeline
**Vulnerability:** The application uses `pickle.load` and `joblib.load` to deserialize machine learning artifacts. This exposes the system to Arbitrary Code Execution if a malicious `.pkl` file is loaded.
**Learning:** `pickle` is inherently unsafe for untrusted data. ML pipelines should save and load models using secure formats like JSON or framework-specific safe loaders (e.g. `xgb.XGBClassifier().load_model()`).
**Prevention:** Strictly prohibit `pickle` and `joblib` in production runtime environments. Always export data to JSON.
