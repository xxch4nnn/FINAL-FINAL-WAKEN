## 2024-04-23 - [CRITICAL] Fix Insecure ML Model Deserialization
**Vulnerability:** The application was loading XGBoost machine learning models, scalers, and feature lists using `pickle` and `joblib.load()`. This is a critical insecure deserialization vulnerability that could allow arbitrary code execution if a malicious `.pkl` file was provided.
**Learning:** Legacy ML saving practices (like Pickling) were used by default without considering the security implications of loading untrusted model files.
**Prevention:** Always serialize and deserialize machine learning models and configuration data using secure formats like JSON. For XGBoost, use its native `.save_model()` and `.load_model()` with `.json` extensions. Avoid `pickle` or `joblib` for any data that could be modified by users.
