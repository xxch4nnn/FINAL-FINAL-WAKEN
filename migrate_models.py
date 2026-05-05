import joblib
import json
import xgboost as xgb
from pathlib import Path
import os
import numpy as np

def migrate_directory(dir_path):
    p = Path(dir_path)
    if not p.exists():
        print(f"Directory {dir_path} does not exist. Skipping.")
        return

    # Model
    model_pkl = p / "rf_model.pkl"
    model_json = p / "rf_model.json"
    if model_pkl.exists():
        print(f"Migrating {model_pkl} to {model_json}...")
        model = joblib.load(model_pkl)
        # xgboost models can be saved directly
        model.save_model(str(model_json))

    # Scaler
    scaler_pkl = p / "scaler.pkl"
    scaler_json = p / "scaler.json"
    if scaler_pkl.exists():
        print(f"Migrating {scaler_pkl} to {scaler_json}...")
        scaler = joblib.load(scaler_pkl)
        with open(scaler_json, 'w') as f:
            json.dump({
                "mean_": scaler.mean_.tolist() if hasattr(scaler, 'mean_') else [],
                "scale_": scaler.scale_.tolist() if hasattr(scaler, 'scale_') else []
            }, f)

    # Selected features
    features_pkl = p / "selected_features.pkl"
    features_json = p / "selected_features.json"
    if features_pkl.exists():
        print(f"Migrating {features_pkl} to {features_json}...")
        features = joblib.load(features_pkl)
        with open(features_json, 'w') as f:
            # handle if it's an array or list
            if isinstance(features, np.ndarray):
                features = features.tolist()
            json.dump(features, f)

    print(f"Finished migrating {dir_path}")

if __name__ == "__main__":
    migrate_directory("models")
    migrate_directory("Machine_Learning_Course/Data/PianoMotion10M/models")
