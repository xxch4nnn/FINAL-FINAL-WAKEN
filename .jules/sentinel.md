## 2024-04-01 - [CRITICAL] Insecure Deserialization in ML Pipeline
**Vulnerability:** The machine learning pipeline utilized `joblib` and `pickle` for model serialization and deserialization (`rf_model.pkl`). This introduced a critical insecure deserialization vulnerability, as loading a malicious pickle file allows arbitrary code execution.
**Learning:** Python's native serialization tools (Pickle, Joblib) are fundamentally insecure and should never be used for exchanging artifacts or models across boundaries where trust cannot be strictly guaranteed.
**Prevention:** Always use secure, framework-native formats that serialize to pure data objects. For XGBoost, always use `save_model()` and `load_model()` with `.json` extensions instead of serializing the wrapper class via pickle.
