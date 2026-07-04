## 2025-02-28 - Insecure Deserialization Vulnerability
**Vulnerability:** Use of insecure deserialization functions (`joblib.load` and `pickle.load`) on untrusted data files (`.pkl`), allowing for remote code execution.
**Learning:** Legacy `.pkl` files created with `joblib` or `pickle` are fundamentally insecure because they can execute arbitrary code upon loading.
**Prevention:** Avoid `joblib.load` and `pickle.load` for serialized data. When migrating from scikit-learn models (which often require pickle), switch to tree-based models with safe export formats like JSON (XGBoost/LightGBM) or ONNX, and implement data migration scripts to permanently convert existing legacy `.pkl` files to `.json`.
