## 2024-07-01 - Fix Insecure Deserialization in VisionEngine
**Vulnerability:** The VisionEngine class was loading XGBoost models using python's `pickle.load()` on `.pkl` files (CWE-502), which allows arbitrary code execution if a malicious file is supplied.
**Learning:** Legacy ML models serialized using `joblib` or `pickle` are fundamentally insecure for runtime deserialization. `vision_engine.py` was directly importing and using `pickle`.
**Prevention:** Always use the framework's native secure serialization methods. For XGBoost, always use `.save_model()` and `.load_model()` with `.json` formats, and aggressively remove `pickle` imports from runtime code.
