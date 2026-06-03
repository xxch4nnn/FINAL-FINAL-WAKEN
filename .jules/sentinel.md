## 2024-06-03 - Insecure Deserialization of ML Artifacts
**Vulnerability:** The codebase was using `pickle` and `joblib` to deserialize ML artifacts (`rf_model.pkl`, `scaler.pkl`) in `vision_engine.py` and `main_runtime.py`, exposing the system to arbitrary code execution (CWE-502).
**Learning:** Legacy ML models serialized via `joblib` introduce critical deserialization risks.
**Prevention:** Always use secure formats like `.json` and native secure methods (`xgb.XGBClassifier().load_model()`).
