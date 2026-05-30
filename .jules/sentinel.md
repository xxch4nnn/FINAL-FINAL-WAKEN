## 2024-05-30 - Insecure Deserialization in ML Pipeline
**Vulnerability:** The application used `joblib` and `pickle` to load machine learning artifacts (`rf_model.pkl`, scalers, legacy models). This introduces a Critical Insecure Deserialization (CWE-502) vulnerability, as unpickling untrusted data can lead to arbitrary code execution.
**Learning:** Standard ML pipelines often default to `pickle`/`joblib` for convenience, but this is unsafe for production runtimes.
**Prevention:** Strictly prohibit `pickle` and `joblib`. Use secure serialization formats like `.json` for metadata/scalers and native `.load_model()` methods for frameworks like XGBoost.
