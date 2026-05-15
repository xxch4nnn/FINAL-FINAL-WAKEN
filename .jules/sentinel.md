## 2023-10-27 - Insecure Deserialization in ML Models
**Vulnerability:** Found `pickle.load()` and `joblib.load()` being used for loading ML models and scalers. This is a critical insecure deserialization vulnerability that allows arbitrary code execution.
**Learning:** Legacy ML pipelines often default to `pickle` or `joblib` for serialization, prioritizing convenience over security.
**Prevention:** Use secure formats like JSON for scalers/metadata and native model formats (e.g., XGBoost's `.json` or ONNX) for model weights instead of raw `pickle`. Provide migration scripts to convert existing `.pkl` artifacts.
