## 2024-05-24 - Fix Insecure Deserialization in ML Pipeline
**Vulnerability:** The machine learning pipeline used `joblib` and `pickle` to serialize and deserialize ML models, scalers, and features (`rf_model.pkl`, `scaler.pkl`). This exposes the application to Remote Code Execution (RCE) via insecure deserialization if a malicious model artifact is loaded.
**Learning:** Legacy Python serialization formats like `pickle` (used directly or via `joblib`) are inherently insecure for untrusted data. They were used for convenience during initial development.
**Prevention:** Always use safe serialization formats like `.json` for simple data and native framework methods (e.g., XGBoost's `save_model` / `load_model`) for ML models to avoid executing arbitrary code during the loading process.
