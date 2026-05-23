## 2025-05-22 - Insecure Deserialization in ML Pipeline
**Vulnerability:** The runtime engine (`src/runtime/vision_engine.py` and `main_runtime.py` - via `joblib.load` or `pickle.load`) dynamically loads serialized `.pkl` machine learning artifacts using Python's native `pickle` library, which allows arbitrary code execution.
**Learning:** Legacy ML models (e.g. Scikit-learn or XGBoost previously using pickle) were serialized insecurely. An attacker providing a malicious `.pkl` file to the path loaded by the vision engine could achieve RCE.
**Prevention:** ML artifacts must be migrated away from `pickle` or `joblib`. Scikit-learn scalers/features should use JSON. XGBoost models should use native `save_model/load_model` which defaults to `.json`.
