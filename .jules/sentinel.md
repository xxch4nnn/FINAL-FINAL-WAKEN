## 2024-05-21 - Insecure Deserialization via pickle/joblib
**Vulnerability:** ML models and artifacts (`rf_model.pkl`, `scaler.pkl`) were being deserialized at runtime using `pickle.load()` and `joblib.load()`, allowing arbitrary code execution if artifacts are tampered with.
**Learning:** The pipeline defaulted to `.pkl` for convenience without considering the security implications of executing untrusted model payloads in a production runtime environment.
**Prevention:** Use secure serialization formats like `.json` for XGBoost models (`.save_model()`) and custom JSON serializers for scikit-learn artifacts (e.g., `JSONScaler`) to prevent insecure deserialization.
