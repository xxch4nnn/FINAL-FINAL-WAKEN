## 2024-05-30 - Fix Insecure Deserialization in ML Pipeline
**Vulnerability:** The codebase was vulnerable to insecure object deserialization (CWE-502) via the use of `pickle` and `joblib` in `src/runtime/vision_engine.py`, `main_runtime.py`, and `src/training/train_gpu.py`.
**Learning:** ML artifacts like `.pkl` files can execute arbitrary code upon deserialization. Scikit-learn scalers and arrays must be explicitly converted using `.tolist()` and stored in secure formats like `.json`.
**Prevention:** Remove `pickle` and `joblib` imports. Serialize models using XGBoost's native secure `.save_model()`/`.load_model()` to `.json`, and use a custom `JSONScaler` for scaling parameters.
