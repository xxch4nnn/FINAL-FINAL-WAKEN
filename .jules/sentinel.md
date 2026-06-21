## 2024-06-21 - Insecure Deserialization in ML Pipeline
**Vulnerability:** The project uses `pickle` and `joblib` extensively (`pickle.load`, `joblib.load`) to load ML models and scalers. This allows arbitrary code execution via insecure deserialization.
**Learning:** The ML community often uses these libraries for serialization, disregarding the inherent RCE risk. In this repository, `main_runtime.py` and `vision_engine.py` rely on them heavily to load artifacts.
**Prevention:** ML artifacts must be serialized and loaded using secure methods. XGBoost models must use `load_model()` / `save_model()`, scikit-learn compatible scalers should use `json` and implement manual `transform` logic to avoid `pickle`/`joblib`.
