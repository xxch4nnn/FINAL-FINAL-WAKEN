1. **Remove `joblib` from `main_runtime.py` and replace with secure `.json` loading**
   - Update `_load_artifacts` to use `json.load` for the model, scaler, and features.
   - For XGBoost model, use `xgb.XGBClassifier().load_model(str(m_path))`.
   - For Scaler, write or use a custom `JSONScaler` class (as per memory: "Scalers are reconstructed using a custom `JSONScaler` class that converts JSON `mean`/`scale` lists to NumPy arrays").
   - Update `CONFIG` to point to `.json` files instead of `.pkl`.

2. **Remove `pickle` from `src/runtime/vision_engine.py`**
   - Update `_load_model` to load an XGBoost model from `.json` using `xgb.XGBClassifier().load_model()`.
   - Remove `import pickle` and use secure loading logic.
   - Change default `model_path` to `"models/rf_model.json"`.

3. **Update training script (`src/training/train_gpu.py`) to save models securely**
   - Remove `joblib`.
   - Update to use `.save_model(MODEL_PATH)` for the XGBoost classifier.
   - Change `MODEL_PATH` from `.pkl` to `.json`.

4. **Implement Migration Script (`migrate_models.py`)**
   - Create a script that uses `joblib` to load existing `.pkl` files and securely resave them as `.json` (for the model, scaler, and selected features) so that functionality is preserved. (Note: Only XGBoost models can easily be saved to JSON, so if they are RF/SVM, we need to handle that, but `train_gpu.py` trains an XGBoost classifier).

5. **Create Tests for Security Enhancements**
   - Since we are modifying serialization formats, create tests to ensure `JSONScaler` correctly applies the transform and XGBoost model loads properly.

6. **Complete pre-commit steps**
   - Ensure proper testing, verification, review, and reflection are done.

7. **Submit changes**
   - Commit and push to branch.
