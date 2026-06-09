## 2024-05-18 - Insecure Deserialization Vulnerability
**Vulnerability:** The application was using `pickle` and `joblib` for loading ML artifacts (`rf_model.pkl`, `scaler.pkl`), which allows arbitrary code execution via insecure deserialization.
**Learning:** Legacy ML models often use standard Python object serialization tools which are inherently insecure for untrusted inputs.
**Prevention:** Always serialize and deserialize machine learning models and artifacts using native secure formats (e.g. `.json` for XGBoost models and explicitly parsed configurations for custom scalers).
