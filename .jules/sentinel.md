## 2024-05-18 - [CRITICAL] Replace insecure pickle/joblib deserialization with native JSON

**Vulnerability:** The application was using `joblib.load()` and `pickle.load()` to deserialize XGBoost models, scalers, and feature lists. `pickle` and `joblib` are inherently insecure against malicious payloads, leading to Arbitrary Code Execution (ACE) vulnerabilities when loading unverified `.pkl` artifacts.

**Learning:** This vulnerability existed due to the default serialization habits (using `.pkl` output) common in data science pipelines interacting with scikit-learn ecosystems, applied improperly in the production application entry points (`vision_engine.py` and `main_runtime.py`).

**Prevention:** To prevent this, strictly mandate the use of `save_model` and `load_model` (native JSON format) for tree-based models like XGBoost, and build custom JSON-based serialization classes (`JSONScaler`) and standard `json.load()` mechanisms for other configuration artifacts. Ensure the entire ML pipeline (training through to inference) avoids `joblib` and `pickle` operations.
