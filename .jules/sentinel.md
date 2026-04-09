## 2024-06-12 - Insecure Deserialization in ML Model Loading
**Vulnerability:** The application used `pickle.load()` and `joblib.load()` to deserialize `.pkl` model files, which allows arbitrary code execution if a malicious model file is loaded.
**Learning:** Machine learning models loaded via pickle/joblib are inherently insecure. Using native, secure formats like XGBoost's JSON is required to prevent Remote Code Execution (RCE).
**Prevention:** Always use secure serialization formats (e.g., `.json` for XGBoost models, `.safetensors` for PyTorch) and enforce file extension/format checks before loading artifacts.
