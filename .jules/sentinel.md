## 2024-06-06 - Insecure Deserialization in ML Pipeline
**Vulnerability:** Pickle and joblib were used to load external machine learning models and scalers, introducing severe arbitrary code execution risks.
**Learning:** Using `joblib.load()` or `pickle.load()` on untrusted artifact files is natively vulnerable to CWE-502. Even "internal" models could be maliciously replaced.
**Prevention:** Migrate serialization pipelines strictly to safer formats such as pure JSON (for scalers and features) and vendor-specific safe loading (like `xgboost.XGBClassifier().load_model()`).
