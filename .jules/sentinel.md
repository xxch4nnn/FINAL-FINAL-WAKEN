## 2025-03-09 - Fix Insecure Deserialization (CWE-502)
**Vulnerability:** The application loads models and features using `joblib` and `pickle`, which are inherently insecure and vulnerable to arbitrary code execution if malicious `.pkl` files are loaded.
**Learning:** Found multiple instances of `pickle.load()` and `joblib.load()` loading unverified `.pkl` files for ML artifacts (models, scalers, feature lists).
**Prevention:** ML models must be saved and loaded using secure formats, such as JSON for standard structures and native secure serialization methods like `xgb.XGBClassifier().save_model()`/`.load_model()` for XGBoost.
