## 2024-06-01 - Insecure Deserialization Vulnerability
**Vulnerability:** The project uses `pickle` and `joblib` for deserializing machine learning models and artifacts, exposing it to arbitrary code execution if an attacker replaces a `.pkl` file.
**Learning:** Legacy ML pipelines frequently used `pickle` and `joblib` as convenient serialization methods, but they are insecure and should not be used in runtime code. We need to secure the deserialization pipeline by migrating from `.pkl` to `.json` or similar safe formats.
**Prevention:** Eliminate the use of `pickle` and `joblib` for deserializing untrusted data. Use secure serialization formats (like JSON) or secure methods like `xgb.XGBClassifier().load_model()` and convert existing artifacts appropriately.
