## 2024-05-14 - Fix Insecure Deserialization via pickle/joblib
**Vulnerability:** The codebase was utilizing `pickle` and `joblib` for deserializing machine learning artifacts (models, scalers, and features) at runtime. This poses a critical arbitrary code execution risk if malicious files are loaded.
**Learning:** `joblib` and `pickle` execute arbitrary code when reconstructing Python objects. Standard serialization formats like `.pkl` cannot be safely loaded from untrusted sources. Scikit-learn doesn't have a built-in secure cross-platform JSON scaler representation, leading to reliance on `joblib`.
**Prevention:**
1. Migrate ML models to use XGBoost's native `.json` serialization via `save_model` and `load_model`.
2. Extract scaler parameters (`mean_`, `scale_`) and store them as simple `.json` dictionaries. Reconstruct the scaler interface at runtime with a custom wrapper class (`JSONScaler`) that loads these values.
3. Completely remove `pickle` and `joblib` imports from all runtime execution paths (`main_runtime.py`, `src/runtime/vision_engine.py`, `src/training/train_gpu.py`).
4. Ensure a one-time migration script is used to convert legacy artifacts without placing `joblib` in the active pipeline.
