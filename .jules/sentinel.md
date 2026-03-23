## 2024-05-20 - Replace Insecure Pickle Serialization with Native JSON for ML Models
**Vulnerability:** Machine learning models were saved and loaded using `joblib` and `pickle`. These formats execute arbitrary code upon deserialization, posing a critical remote code execution (RCE) risk if model files are tampered with or downloaded from untrusted sources.
**Learning:** Even internal ML pipelines are vulnerable if they rely on `pickle` for model transfer. XGBoost's native `save_model()` and `load_model()` methods support secure `.json` serialization which mitigates this risk entirely.
**Prevention:** Always use secure, language-agnostic formats like JSON or ONNX for model serialization. Avoid `pickle` and `joblib` for any artifact that might cross trust boundaries.
