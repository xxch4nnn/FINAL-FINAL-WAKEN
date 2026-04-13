## 2024-05-25 - Prevent Insecure ML Model Deserialization
**Vulnerability:** The codebase was saving and loading XGBoost models using `pickle` and `joblib` in `.pkl` format (e.g., `src/runtime/vision_engine.py` and `src/training/train_gpu.py`).
**Learning:** `pickle` and `joblib` are inherently insecure for deserializing unverified data. If an attacker could replace the model file with a maliciously crafted pickle payload, they could achieve Arbitrary Code Execution (RCE) when the model is loaded.
**Prevention:** Always use safe, format-specific methods for saving and loading machine learning models. For XGBoost, always use its native `.json` model saving and loading (`save_model` and `load_model`), and explicitly block `.pkl` file loading in runtime environments.
