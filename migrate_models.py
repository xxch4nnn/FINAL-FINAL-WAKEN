import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate_model(pkl_path, json_path):
    p = Path(pkl_path)
    if p.exists():
        model = joblib.load(p)
        model.save_model(str(json_path))

def migrate_scaler(pkl_path, json_path):
    p = Path(pkl_path)
    if p.exists():
        scaler = joblib.load(p)
        with open(json_path, 'w') as f:
            json.dump({'mean_': scaler.mean_.tolist(), 'scale_': scaler.scale_.tolist()}, f)

def migrate_features(pkl_path, json_path):
    p = Path(pkl_path)
    if p.exists():
        features = joblib.load(p)
        with open(json_path, 'w') as f:
            json.dump(list(features), f)

if __name__ == "__main__":
    migrate_model("models/rf_model.pkl", "models/rf_model.json")
    base = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    migrate_model(base / "rf_model.pkl", base / "rf_model.json")
    migrate_scaler(base / "scaler.pkl", base / "scaler.json")
    migrate_features(base / "selected_features.pkl", base / "selected_features.json")
