## 2024-05-01 - Fix insecure deserialization vulnerability
**Vulnerability:** The codebase was using `pickle` and `joblib` to deserialize XGBoost models, scalers, and feature lists.
**Learning:** These modules are unsafe when loading files from untrusted sources, as malicious payloads can execute arbitrary code during the deserialization process.
**Prevention:** Avoid `pickle` and `joblib` for ML artifacts in production code. Use native `.json` serializers, such as `xgb.XGBClassifier().load_model()`, and securely convert simple artifacts like arrays or dictionaries using the standard `json` module.
