## 2024-05-25 - Insecure Deserialization Pipeline Migration
**Vulnerability:** The machine learning pipeline (`vision_engine.py`, `main_runtime.py`, `train_gpu.py`) used `pickle` and `joblib` for model and scaler deserialization, exposing the application to critical arbitrary code execution (CWE-502).
**Learning:** Legacy ML artifacts (like scikit-learn `.pkl` files) combined with native Python deserialization create a high-risk attack surface in production applications.
**Prevention:** Strictly enforce secure data serialization formats (`.json`) and safe framework loaders (`xgb.load_model()`). Utilize custom wrapper classes (like `JSONScaler`) to preserve interfaces without risking execution.
