## 2024-06-18 - Fix Insecure Deserialization in Vision Engine
**Vulnerability:** The codebase was vulnerable to CWE-502 (Insecure Deserialization) by using `pickle.load()` on unverified model artifacts (`rf_model.pkl`).
**Learning:** Legacy workflows often default to `pickle` or `joblib` for model persistence, blindly loading Python objects which can execute arbitrary code during deserialization.
**Prevention:** Always serialize ML artifacts into safe formats like JSON. For XGBoost, rely exclusively on `load_model()` and `.json` files to prevent malicious code execution. Use migration scripts for legacy artifacts rather than loading them in the active runtime.
