## 2024-05-20 - Insecure Deserialization in ML Pipeline
**Vulnerability:** XGBoost models were being saved and loaded using `joblib` and `pickle` (`.pkl` format) in `train_gpu.py` and `vision_engine.py`.
**Learning:** Using `joblib`/`pickle` to deserialize ML models allows arbitrary code execution if the `.pkl` file is tampered with by an attacker.
**Prevention:** Always use safe serialization formats for ML models. XGBoost provides `save_model()` and `load_model()` methods which natively export to safe `.json` format instead. Avoid `pickle` completely.
