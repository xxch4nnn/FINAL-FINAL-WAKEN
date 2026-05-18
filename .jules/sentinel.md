## 2024-05-20 - Insecure Deserialization via Pickle

**Vulnerability:** The `VisionEngine` class in `src/runtime/vision_engine.py` used `pickle.load` to load machine learning models from `.pkl` files.
**Learning:** Using `pickle` or `joblib` for deserialization allows for arbitrary code execution if a malicious model file is provided. This is especially risky for ML artifacts.
**Prevention:** ML models and artifacts should be serialized using secure, language-agnostic formats like JSON. For XGBoost, always use `xgb.XGBClassifier().load_model()` with `.json` files instead of pickle.
