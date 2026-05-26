## 2024-05-26 - Fix Insecure ML Model Deserialization (CWE-502)
**Vulnerability:** The runtime and training pipelines use `joblib.load()` and `pickle.load()` to deserialize `.pkl` models and scalers. This is vulnerable to arbitrary code execution (CWE-502).
**Learning:** Scikit-learn and XGBoost artifacts must be serialized in secure formats. `pickle` is unsafe for untrusted runtime environments.
**Prevention:** Use XGBoost's native `.json` model saving/loading methods (`clf.save_model()`, `xgb.XGBClassifier().load_model()`). For scalers and feature lists, serialize them as standard JSON. Migrate existing `.pkl` models using a dedicated conversion script, explicitly disabling `pickle` in runtime code.
