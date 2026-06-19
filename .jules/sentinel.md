## YYYY-MM-DD - Insecure Deserialization of Pickle/Joblib
**Vulnerability:** The application uses `pickle.load()` and `joblib.load()` to deserialize `.pkl` models and artifacts directly from disk. This is a critical vulnerability (CWE-502: Deserialization of Untrusted Data) because malicious pickle files can execute arbitrary python code during deserialization.
**Learning:** Machine learning artifacts are often serialized using pickle or joblib without realizing the security implications when loading untrusted or external models.
**Prevention:** Avoid `pickle` and `joblib` for deserializing models. For XGBoost, use its native `.load_model(path)` with JSON. For simple parameters, use secure formats like `json`. Replace `joblib` with secure formats or model-native serializers.
