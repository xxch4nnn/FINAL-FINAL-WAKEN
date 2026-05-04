import joblib
import json
import xgboost as xgb
from pathlib import Path
import os
import sys

def migrate(models_dir):
    p = Path(models_dir)
    if not p.exists():
        print(f"Directory {models_dir} does not exist.")
        return

    # Migrate model
    model_pkl = p / "rf_model.pkl"
    model_json = p / "rf_model.json"
    if model_pkl.exists():
        print(f"Migrating {model_pkl} to {model_json}...")
        try:
            model = joblib.load(model_pkl)
            # Assuming XGBClassifier
            if hasattr(model, 'save_model'):
                model.save_model(str(model_json))
                print(f"Successfully migrated model to {model_json}")
            else:
                print("Model does not have save_model method.")
        except Exception as e:
            print(f"Failed to migrate model: {e}")

    # Migrate scaler
    scaler_pkl = p / "scaler.pkl"
    scaler_json = p / "scaler.json"
    if scaler_pkl.exists():
        print(f"Migrating {scaler_pkl} to {scaler_json}...")
        try:
            scaler = joblib.load(scaler_pkl)
            scaler_data = {
                'mean_': scaler.mean_.tolist() if hasattr(scaler, 'mean_') else [],
                'scale_': scaler.scale_.tolist() if hasattr(scaler, 'scale_') else []
            }
            with open(scaler_json, 'w') as f:
                json.dump(scaler_data, f)
            print(f"Successfully migrated scaler to {scaler_json}")
        except Exception as e:
            print(f"Failed to migrate scaler: {e}")

    # Migrate selected features
    feat_pkl = p / "selected_features.pkl"
    feat_json = p / "selected_features.json"
    if feat_pkl.exists():
        print(f"Migrating {feat_pkl} to {feat_json}...")
        try:
            features = joblib.load(feat_pkl)
            with open(feat_json, 'w') as f:
                json.dump(list(features), f)
            print(f"Successfully migrated features to {feat_json}")
        except Exception as e:
            print(f"Failed to migrate features: {e}")

if __name__ == "__main__":
    dirs_to_check = [
        "models",
        "Machine_Learning_Course/Data/PianoMotion10M/models",
        "."
    ]
    for d in dirs_to_check:
        migrate(d)
