## 2024-05-24 - Fix Insecure Deserialization (CWE-502)
**Vulnerability:** Insecure object deserialization via `pickle` and `joblib` in ML pipelines.
**Learning:** Loading `.pkl` files with `pickle` or `joblib` allows arbitrary code execution.
**Prevention:** Use secure serialization formats like JSON and native model loader `xgb.XGBClassifier().load_model()`.
