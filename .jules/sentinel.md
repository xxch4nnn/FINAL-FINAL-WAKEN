## 2024-04-18 - [CRITICAL] Fix insecure deserialization of ML artifacts
**Vulnerability:** The application was using `joblib` and `pickle` to deserialize ML artifacts (`rf_model.pkl`, `scaler.pkl`, `selected_features.pkl`).
**Learning:** Insecure deserialization via `joblib` and `pickle` allows arbitrary code execution if an attacker can tamper with the serialized files.
**Prevention:** ML artifacts must be serialized and deserialized using secure formats such as standard JSON (`json.dump` / `json.load`) and native, secure loading functions provided by the ML library (e.g., `xgb.Booster.load_model` or `xgb.XGBClassifier.load_model` for XGBoost models).
