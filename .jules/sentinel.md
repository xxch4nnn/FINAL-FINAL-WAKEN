## 2025-02-28 - Insecure Deserialization Vulnerability
**Vulnerability:** The application uses `pickle` and `joblib` to load machine learning models from untrusted `.pkl` files (CWE-502).
**Learning:** Using `pickle` or `joblib` allows execution of arbitrary code when deserializing malicious files. The model loader should always use secure formats like JSON and library-specific secure loaders (e.g., `xgb.load_model`).
**Prevention:** Avoid `pickle` and `joblib` entirely for ML artifacts. Use `.json` formats and secure loaders like `xgboost`'s built-in `.load_model()` and a custom `JSONScaler`.
