## 2024-04-08 - [Insecure Deserialization of ML Models]
**Vulnerability:** XGBoost models were being saved and loaded using `pickle` and `joblib` formats (`.pkl`), which are vulnerable to arbitrary code execution during deserialization.
**Learning:** `joblib` and `pickle` are widely used for ML artifacts but inherently execute instructions to reconstruct objects, allowing malicious payloads in the artifact files to gain code execution.
**Prevention:** ML models should be serialized using secure, native data formats (e.g., XGBoost's `.json` format via `save_model()` and `load_model()`) that strictly load parameters and weights without executing arbitrary Python code.
