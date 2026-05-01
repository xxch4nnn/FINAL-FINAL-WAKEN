import joblib
import json
import xgboost as xgb
import numpy as np
from pathlib import Path
import os

def migrate():
    dirs_to_check = [
        Path("models"),
        Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    ]

    for d in dirs_to_check:
        if not d.exists():
            continue

        print(f"Migrating models in {d}...")

        model_pkl = d / "rf_model.pkl"
        model_json = d / "rf_model.json"
        if model_pkl.exists():
            print(f"Loading {model_pkl}...")
            model = joblib.load(model_pkl)
            # It's an XGBClassifier, we can save using save_model
            model.save_model(model_json)
            print(f"Saved {model_json}")

        scaler_pkl = d / "scaler.pkl"
        scaler_json = d / "scaler.json"
        if scaler_pkl.exists():
            print(f"Loading {scaler_pkl}...")
            scaler = joblib.load(scaler_pkl)
            scaler_data = {
                "mean_": scaler.mean_.tolist() if hasattr(scaler, "mean_") else [],
                "scale_": scaler.scale_.tolist() if hasattr(scaler, "scale_") else []
            }
            with open(scaler_json, 'w') as f:
                json.dump(scaler_data, f)
            print(f"Saved {scaler_json}")

        features_pkl = d / "selected_features.pkl"
        features_json = d / "selected_features.json"
        if features_pkl.exists():
            print(f"Loading {features_pkl}...")
            features = joblib.load(features_pkl)
            with open(features_json, 'w') as f:
                json.dump(list(features), f)
            print(f"Saved {features_json}")

if __name__ == "__main__":
    migrate()
