## 2024-05-16 - [Security Standard for ML Artifacts]
**Vulnerability:** Scikit-learn models and scalers were being deserialized using `pickle` and `joblib` across multiple files, introducing arbitrary code execution risks.
**Learning:** `joblib` and `pickle` are strictly prohibited for active model deserialization across the codebase due to security risks. They are only permitted for one-time migrations.
**Prevention:** Use JSON for serialization (`.json`). Scikit-learn scalers must use a custom `JSONScaler` class to recreate the `mean_` and `scale_` arrays from JSON files. XGBoost models use their native `load_model()` with `.json` files.
