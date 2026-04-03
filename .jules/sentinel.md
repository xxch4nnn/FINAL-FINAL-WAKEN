## 2024-05-24 - [Fix insecure deserialization in ML Model]
**Vulnerability:** Found insecure `joblib.dump` and `pickle.load` being used for saving and loading the XGBoost ML model (`rf_model.pkl`), posing a critical Remote Code Execution (RCE) risk through insecure deserialization if the model file is tampered with.
**Learning:** `joblib` and `pickle` are inherently insecure for loading files from untrusted sources. Many ML libraries have secure native options.
**Prevention:** Use native, secure serialization wrappers like XGBoost's `.save_model()` and `.load_model()` with `.json` formats instead of generic pickling for ML models.
