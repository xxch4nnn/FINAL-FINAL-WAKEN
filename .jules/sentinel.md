## 2024-06-11 - Insecure Deserialization in ML Models
**Vulnerability:** The codebase relies on `pickle` and `joblib` for deserializing ML models (CWE-502), which can execute arbitrary code if tampered with.
**Learning:** Legacy `.pkl` artifacts were exported via `joblib` or `pickle` for XGBoost and Scikit-learn, introducing a severe risk in runtime pipelines. XGBoost natively supports safe serialization to `.json`.
**Prevention:** Strictly prohibit `pickle` and `joblib` imports in runtime pipelines. Migrate all legacy XGBoost models to `.json` using `save_model()`, and use `json` module for scalers/features. Enforce `.json` extension for all active artifacts.
