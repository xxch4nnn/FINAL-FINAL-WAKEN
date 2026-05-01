## 2024-05-01 - Insecure Deserialization (pickle/joblib)
**Vulnerability:** Core ML artifacts (`rf_model.pkl`, `scaler.pkl`, `selected_features.pkl`) were being deserialized using `pickle.load` and `joblib.load` during live runtime across multiple scripts (`main_runtime.py`, `src/runtime/vision_engine.py`).
**Learning:** These modules can execute arbitrary code if a malicious or tampered model file is provided. This existed likely due to legacy scikit-learn standard practices being carried over to XGBoost without realizing the security risks.
**Prevention:** Always use safe, native serialization formats like `.json` for ML models (e.g., `XGBClassifier.load_model('model.json')`) and configuration/scaler data. Avoid `joblib` and `pickle` in production runtimes.
