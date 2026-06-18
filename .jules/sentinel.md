## 2025-03-09 - Insecure Object Deserialization

**Vulnerability:** The application used insecure `pickle` and `joblib` libraries to deserialize machine learning artifacts directly into executable objects, exposing it to Remote Code Execution (RCE) via insecure object deserialization (CWE-502).
**Learning:** XGBoost and Scikit-learn models serialized using joblib/pickle can execute arbitrary code upon loading. Mitigation requires using secure formats like JSON for weights and custom loading logic for scalers to ensure data is treated strictly as data.
**Prevention:** Always use `json` or native secure methods (like `xgb.save_model()`/`load_model()`) for serializing and deserializing data.
