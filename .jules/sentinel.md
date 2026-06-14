## 2024-06-14 - Insecure Deserialization in ML Models
**Vulnerability:** The `VisionEngine` class utilized `pickle.load` to deserialize ML models, which is vulnerable to arbitrary code execution (CWE-502) if an attacker tampers with the `.pkl` artifact.
**Learning:** Native framework methods like XGBoost's `load_model` can securely load models from JSON files without relying on insecure Python object serialization.
**Prevention:** Strictly prohibit `pickle` and `joblib` for model loading; always use secure serialization formats (like JSON) and native, non-executing load methods.
