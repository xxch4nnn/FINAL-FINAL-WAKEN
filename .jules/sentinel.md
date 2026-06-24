## 2024-06-24 - Fix Insecure Deserialization
**Vulnerability:** Models and scalers were loaded using `pickle.load` and `joblib.load`, which is vulnerable to insecure object deserialization (CWE-502).
**Learning:** Legacy ML models serialized as `.pkl` allow arbitrary code execution during loading.
**Prevention:** Always serialize artifacts to strictly defined formats like `.json` or use secure loaders like XGBoost's `load_model`.
