## 2025-02-15 - CRITICAL: Insecure Deserialization of ML Artifacts
**Vulnerability:** The system uses `pickle.load()` and `joblib.load()` across `main_runtime.py` and `vision_engine.py` to deserialize machine learning artifacts (.pkl files), leading to arbitrary code execution if artifacts are tampered with.
**Learning:** Serializing scikit-learn models and complex objects to disk using `joblib` or `pickle` is standard but fundamentally insecure for deployment when artifacts could be substituted.
**Prevention:** Migrate all ML artifacts to JSON format. XGBoost native `.json` handles model persistence securely. Scalers must be saved as dictionaries/lists of parameters and reconstructed safely without invoking `pickle`.
