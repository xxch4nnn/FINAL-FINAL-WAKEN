import joblib
import json
import numpy as np
import xgboost as xgb
from pathlib import Path

def migrate_scaler(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    scaler = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump({'mean': scaler.mean_.tolist(), 'scale': scaler.scale_.tolist()}, f)
    print(f"Migrated {pkl_path} to {json_path}")

def migrate_features(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    features = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump(features, f)
    print(f"Migrated {pkl_path} to {json_path}")

def migrate_xgboost(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    model = joblib.load(pkl_path)
    model.save_model(str(json_path))
    print(f"Migrated {pkl_path} to {json_path}")

if __name__ == "__main__":
    migrate_scaler("models/scaler.pkl", "models/scaler.json")
    migrate_features("models/selected_features.pkl", "models/selected_features.json")
    migrate_xgboost("models/rf_model.pkl", "models/rf_model.json")
