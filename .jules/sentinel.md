## 2024-05-30 - Prevent Insecure Deserialization in Model Loading
**Vulnerability:** XGBoost models were being serialized and deserialized using `joblib` and `pickle` (`.pkl` files), which are known to be vulnerable to insecure deserialization attacks if the model file is tampered with.
**Learning:** `joblib` and `pickle` can execute arbitrary code during deserialization. Machine learning models should be saved and loaded using secure formats like JSON, especially since XGBoost natively supports it.
**Prevention:** Use `clf.save_model("model.json")` and `model.load_model("model.json")` instead of `joblib.dump` and `pickle.load`. Explicitly block the loading of `.pkl` files by raising an exception to enforce this policy.
