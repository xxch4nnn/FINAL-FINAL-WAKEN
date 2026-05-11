## 2025-05-10 - Insecure Deserialization via pickle/joblib
**Vulnerability:** The codebase relies on `pickle` and `joblib` (which uses pickle under the hood) to load models (`rf_model.pkl`) and ML artifacts. This is an insecure deserialization vulnerability, as loading untrusted `.pkl` files can lead to arbitrary code execution.
**Learning:** Legacy ML models from Scikit-Learn or XGBoost are often saved as `.pkl` files, exposing the application to severe RCE risks if the models are tampered with or loaded from unverified paths.
**Prevention:** Always serialize models to secure formats like JSON. For Scikit-Learn models, extract the weights/parameters and save them as JSON. For XGBoost models, use `.save_model('model.json')` and `.load_model('model.json')`.
