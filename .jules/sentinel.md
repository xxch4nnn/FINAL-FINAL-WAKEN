## 2023-10-26 - Insecure Deserialization in VisionEngine
**Vulnerability:** The application used `pickle` to deserialize objects from `.pkl` files, exposing it to arbitrary code execution if a malicious model file was loaded (CWE-502).
**Learning:** The ML models must be exclusively loaded via secure formats like JSON and the `xgb.XGBClassifier().load_model()` method.
**Prevention:** Strictly enforce the prohibition of `pickle` and `joblib` for model deserialization across all runtime pipelines. Use JSON format serialization for model artifacts.
