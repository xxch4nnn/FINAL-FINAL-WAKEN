## 2024-05-24 - [CRITICAL] Prevent Insecure Deserialization via pickle/joblib
**Vulnerability:** XGBoost models were saved/loaded using `pickle` and `joblib`.
**Learning:** `pickle` is vulnerable to arbitrary code execution if the serialized file is tampered with.
**Prevention:** Use native, secure JSON serialization methods like `save_model` and `load_model` provided by the library.
