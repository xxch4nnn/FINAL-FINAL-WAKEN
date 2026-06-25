## 2024-06-25 - Fix Insecure Deserialization in ML Pipeline
**Vulnerability:** The application was using `pickle` and `joblib` to deserialize machine learning models and artifacts (CWE-502), which allows arbitrary code execution if a malicious `.pkl` file is loaded.
**Learning:** Legacy workflows in ML commonly use `pickle`/`joblib` without recognizing the security implications in a production runtime environment.
**Prevention:** Always use secure serialization formats like JSON, or framework-specific safe loading methods (e.g., `xgb.XGBClassifier().load_model()`) that do not allow arbitrary object instantiation.
