import joblib
import xgboost as xgb
import json
import numpy as np
from pathlib import Path

def migrate():
    models_dir = Path("models")
    pkl_path = models_dir / "rf_model.pkl"
    json_path = models_dir / "rf_model.json"

    if pkl_path.exists():
        model = joblib.load(pkl_path)
        model.save_model(str(json_path))
        print(f"Migrated {pkl_path} to {json_path}")
    else:
        print("No .pkl model found to migrate.")

    scaler_pkl = models_dir / "scaler.pkl"
    scaler_json = models_dir / "scaler.json"
    if scaler_pkl.exists():
        scaler = joblib.load(scaler_pkl)
        with open(scaler_json, 'w') as f:
            json.dump({'mean_': scaler.mean_.tolist(), 'scale_': scaler.scale_.tolist()}, f)
        print(f"Migrated {scaler_pkl} to {scaler_json}")

    feat_pkl = models_dir / "selected_features.pkl"
    feat_json = models_dir / "selected_features.json"
    if feat_pkl.exists():
        features = joblib.load(feat_pkl)
        with open(feat_json, 'w') as f:
            json.dump(features, f)
        print(f"Migrated {feat_pkl} to {feat_json}")

if __name__ == "__main__":
    migrate()
