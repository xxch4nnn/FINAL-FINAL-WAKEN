## 2024-05-11 - Insecure Deserialization of ML Artifacts
**Vulnerability:** The application was loading machine learning artifacts (`.pkl` models, scalers, and features) using `pickle.load` and `joblib.load`. This is a critical security vulnerability because these modules can execute arbitrary code during the deserialization process.
**Learning:** This existed because `joblib` and `pickle` are common in data science pipelines for saving scikit-learn models and related objects. However, they are inherently unsafe for active runtime deserialization, especially if the models could be swapped or loaded from untrusted sources.
**Prevention:**
1. Use XGBoost's native `.json` format for models and load them via `xgb.XGBClassifier().load_model(path)` which is safe.
2. For scikit-learn scalers, serialize them to a JSON format (`scaler.json` with `mean_` and `scale_` attributes) and reconstruct them using a custom `JSONScaler` class that preserves the `transform` interface.
3. Save feature lists as standard `.json` arrays and load them using Python's built-in `json.load`.