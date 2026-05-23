1. **Fix Insecure Deserialization in `main_runtime.py`**:
   - Replace `.pkl` defaults with `.json` defaults in `CONFIG` dictionary (`SCALER_NAME`, `MODEL_NAME`, `FEATURES_NAME`).
   - Change `joblib.load(s_path)` to load `scaler.json` and reconstruct `JSONScaler`.
   - Change `joblib.load(f_path)` to load `selected_features.json` via native JSON.
   - Change `joblib.load(m_path)` to load `rf_model.json` using `xgb.XGBClassifier().load_model()`.
2. **Fix Insecure Deserialization in `src/runtime/vision_engine.py`**:
   - Change `model_path="models/rf_model.pkl"` to `model_path="models/rf_model.json"`.
   - Update `_load_model` method to replace `.pkl` with `.json` in the path, use `xgb.XGBClassifier().load_model(str(p))` instead of `pickle.load`.
3. **Fix Insecure Serialization in `src/training/train_gpu.py`**:
   - Change `MODEL_PATH = MODEL_DIR / "rf_model.pkl"` to `MODEL_PATH = MODEL_DIR / "rf_model.json"`.
   - Update `joblib.dump(clf, MODEL_PATH)` to `clf.save_model(MODEL_PATH)`.
4. **Create `migrate_models.py`**:
   - A migration script that securely translates legacy `.pkl` artifacts (like `dt_model.pkl` or old `rf_model.pkl`) to `.json`.
5. **Verify with test execution**:
   - Make sure no regressions are introduced using `-m py_compile`.
6. **Pre-commit and submit**:
   - Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
