## 2024-06-15 - Insecure Deserialization (CWE-502) in Model Loading
**Vulnerability:** The application uses `pickle` and `joblib` (which uses pickle under the hood) to load machine learning models (`pickle.load(f)` in `src/runtime/vision_engine.py` and `joblib.load(m_path)` in `main_runtime.py`). Loading arbitrary objects using `pickle` from untrusted sources leads to arbitrary code execution, which is a critical security vulnerability (CWE-502).
**Learning:** `pickle` is inherently unsafe as it can execute arbitrary code during deserialization.
**Prevention:** Use safer serialization formats for machine learning models when possible. For XGBoost models, use `xgb.Booster.load_model()` and `save_model()` with JSON format instead of relying on `joblib` or `pickle`.
