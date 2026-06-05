import joblib
import json
import xgboost as xgb
import numpy as np
from pathlib import Path

def migrate_scaler(pkl_path, json_path):
    if not Path(pkl_path).exists():
        return
    scaler = joblib.load(pkl_path)
    data = {
        'mean_': scaler.mean_.tolist(),
        'scale_': scaler.scale_.tolist()
    }
    with open(json_path, 'w') as f:
        json.dump(data, f)

def migrate_model(pkl_path, json_path):
    if not Path(pkl_path).exists():
        return
    model = joblib.load(pkl_path)
    model.save_model(str(json_path))

def migrate_features(pkl_path, json_path):
    if not Path(pkl_path).exists():
        return
    features = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump(features, f)

if __name__ == "__main__":
    MODELS_DIR = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if not MODELS_DIR.exists():
        MODELS_DIR = Path("models")
    migrate_model(MODELS_DIR / "rf_model.pkl", MODELS_DIR / "rf_model.json")
    migrate_scaler(MODELS_DIR / "scaler.pkl", MODELS_DIR / "scaler.json")
    migrate_features(MODELS_DIR / "selected_features.pkl", MODELS_DIR / "selected_features.json")
