## 2024-05-25 - Insecure Deserialization Vulnerability
**Vulnerability:** The machine learning models and data scalers were being loaded using `joblib.load()` and `pickle.load()` on `.pkl` files.
**Learning:** These methods execute arbitrary code when deserializing. If an attacker could modify the `.pkl` files, they could achieve Remote Code Execution (RCE).
**Prevention:** Use secure JSON formats for loading machine learning models (e.g., `xgboost.XGBClassifier.load_model('model.json')`) and data configurations (e.g., loading scalers/features with `json.load`). Never use `pickle` or `joblib` for deserializing untrusted or external files.
