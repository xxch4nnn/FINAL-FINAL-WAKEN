import joblib
import json
import xgboost as xgb
from pathlib import Path

models_dir = Path("models")
models_dir.mkdir(exist_ok=True)

# Ensure models_dir also exists for main_runtime config test if needed
Path("Machine_Learning_Course/Data/PianoMotion10M/models").mkdir(parents=True, exist_ok=True)
models_dir_legacy = Path("Machine_Learning_Course/Data/PianoMotion10M/models")

for m_dir in [models_dir, models_dir_legacy]:
    # Migrate scaler
    scaler_pkl = m_dir / "scaler.pkl"
    if scaler_pkl.exists():
        scaler = joblib.load(scaler_pkl)
        with open(m_dir / "scaler.json", "w") as f:
            json.dump({"mean_": scaler.mean_.tolist(), "scale_": scaler.scale_.tolist()}, f)

    # Migrate features
    feat_pkl = m_dir / "selected_features.pkl"
    if feat_pkl.exists():
        feats = joblib.load(feat_pkl)
        with open(m_dir / "selected_features.json", "w") as f:
            json.dump(feats, f)

    # Migrate model
    model_pkl = m_dir / "rf_model.pkl"
    if model_pkl.exists():
        model = joblib.load(model_pkl)
        model.save_model(str(m_dir / "rf_model.json"))

print("Migration complete.")
