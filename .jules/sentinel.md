## 2024-06-13 - Insecure Deserialization in ML Pipeline
**Vulnerability:** The system insecurely loads machine learning models and artifacts using `pickle` and `joblib`, which exposes the application to remote code execution if a malicious `.pkl` file is provided (CWE-502).
**Learning:** Legacy data science tools frequently serialize objects with `pickle` under the hood. In high-security contexts, loading these files is fundamentally unsafe and cannot be patched.
**Prevention:** Always serialize and deserialize machine learning models and related artifacts (like scalers or feature lists) using secure, data-only formats such as JSON or framework-specific safe loaders (e.g., `xgboost.XGBClassifier().load_model()`). Prohibit `pickle` and `joblib` globally.
