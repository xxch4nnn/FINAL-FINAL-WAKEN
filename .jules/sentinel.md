## 2024-05-20 - Insecure ML Model Deserialization via pickle/joblib
**Vulnerability:** Machine learning models were saved and loaded using Python's `pickle` and `joblib` libraries (`rf_model.pkl`), which are vulnerable to arbitrary code execution if an attacker provides a maliciously crafted file.
**Learning:** Legacy ML saving practices often prioritize convenience or compatibility (e.g., joblib/pickle) over security, exposing the application to significant risks if model files are tampered with or downloaded from untrusted sources.
**Prevention:** Always use the framework's native secure serialization methods. For XGBoost, this means using `.save_model()` and `.load_model()` with JSON format (`.json`) instead of pickling objects.
