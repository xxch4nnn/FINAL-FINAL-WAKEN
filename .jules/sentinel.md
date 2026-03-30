## 2024-05-18 - [Insecure Deserialization in Model Loading]
**Vulnerability:** Found `pickle.load` being used in `src/runtime/vision_engine.py` to load `.pkl` ML models, and `joblib.dump` used in `src/training/train_gpu.py` to save them. Both Pickle and Joblib are vulnerable to Arbitrary Code Execution via Insecure Deserialization if the model file is tampered with.
**Learning:** Legacy ML pipelines frequently use pickle/joblib for convenience without considering the security implications of loading untrusted serialized objects.
**Prevention:** Always use secure, language-agnostic serialization formats like JSON for ML models (e.g., `XGBClassifier.save_model` and `XGBClassifier.load_model` which use JSON format) to avoid insecure deserialization vulnerabilities.
