## 2024-04-02 - Insecure Deserialization in ML Pipeline
**Vulnerability:** Training pipeline (`src/training/train_gpu.py`) and runtime engine (`src/runtime/vision_engine.py`) used `joblib.dump` and `pickle.load` for saving and loading XGBoost models.
**Learning:** `joblib` and `pickle` are susceptible to arbitrary code execution if an attacker provides a maliciously crafted `.pkl` file. Machine learning artifacts must be serialized using secure formats.
**Prevention:** Use native, secure serialization methods provided by ML libraries (e.g., `save_model` and `load_model` with `.json` format for XGBoost) instead of general-purpose object serialization like `pickle`.
