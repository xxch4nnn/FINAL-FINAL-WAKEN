## 2024-05-24 - [Insecure Deserialization via pickle/joblib]
**Vulnerability:** Found `pickle.load` and `joblib.load` used to load machine learning models and scalers from `.pkl` files in `main_runtime.py` and `src/runtime/vision_engine.py`. This allows arbitrary code execution if a malicious `.pkl` file is loaded.
**Learning:** Legacy ML pipelines often default to `pickle` or `joblib` for serialization, prioritizing convenience over security.
**Prevention:** Always use secure, language-agnostic serialization formats like `.json` for parameters, and native framework methods (e.g., `xgboost.save_model()`) that use secure formats instead of standard Python deserialization.
