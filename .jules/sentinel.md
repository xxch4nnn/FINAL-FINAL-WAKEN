## 2025-02-19 - Fix Insecure Deserialization in VisionEngine
**Vulnerability:** Found `pickle.load` used to load a machine learning model (`rf_model.pkl`) in `src/runtime/vision_engine.py` without validation. `pickle` is notoriously insecure against remote code execution if the pickled data is untrusted or tampered with.
**Learning:** `pickle` is often used by default for ML models due to ease of use and historical inertia, leading to pervasive unsafe deserialization. XGBoost models natively support safer JSON saving/loading methods (`xgb.XGBClassifier().load_model()`).
**Prevention:** Avoid `pickle` and `joblib` loading of untrusted files. Use native save/load functions provided by the ML library that support safer formats like JSON or safetensors.
