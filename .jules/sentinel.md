## 2024-05-18 - Fix Insecure Deserialization (CWE-502)
**Vulnerability:** Use of `pickle` and `joblib` for ML model artifacts allows arbitrary code execution upon deserialization.
**Learning:** XGBoost provides native, secure `save_model` and `load_model` methods (using JSON format) which must be used instead of standard object serialization. Sklearn scalers can be securely stored by extracting the `mean_` and `scale_` parameters and serializing them in JSON.
**Prevention:** Never import `pickle` or `joblib` in runtime/production code. Always use framework-specific secure persistence methods or structured data formats (like JSON) for ML configuration.
