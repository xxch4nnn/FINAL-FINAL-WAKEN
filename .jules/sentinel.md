## YYYY-MM-DD - Sentinel Findings
**Vulnerability:** Insecure Object Deserialization via pickle/joblib.
**Learning:** Python `pickle` and `joblib` are vulnerable to arbitrary code execution if loading untrusted or tampered model files. The codebase currently loads `.pkl` files natively using these insecure libraries.
**Prevention:** Use a secure serialization format like JSON for configuration and state, and library-specific secure loaders (like `xgb.XGBClassifier().load_model()`) or `safetensors` for ML models. Do not use `pickle` or `joblib` for deserialization without guaranteed provenance, and never on runtime edge devices where files can be swapped.
