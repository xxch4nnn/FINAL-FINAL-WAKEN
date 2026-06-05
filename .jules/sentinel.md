## 2024-06-05 - Insecure Deserialization (CWE-502) in ML Pipelines
**Vulnerability:** Machine learning models and scalers were being loaded using `pickle` and `joblib` directly from disk (`rf_model.pkl`, `scaler.pkl`), creating a critical remote code execution vector.
**Learning:** Using legacy serialization formats across the model pipeline (training and runtime) exposes systems to arbitrary code execution if artifacts are manipulated.
**Prevention:** Migrate all ML artifacts to secure serialization formats (`.json`) using explicit `.save_model()` and `.load_model()` methods. For scalers, manually manage the attributes (e.g., `mean_`, `scale_`) and inject them securely.
