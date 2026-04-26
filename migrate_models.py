import joblib
import pickle
import json
import xgboost as xgb
from pathlib import Path
import numpy as np
import sys

TARGET_COLS = [
    'tip2dip', 'tip2pip', 'tip2mcp', 'tip2wrist',
    'disp', 'velocity_size', 'velocity_disp', 'acceleration_disp',
    'distance_cm'
]

def migrate_directory(model_dir: Path):
    if not model_dir.exists():
        print(f"Directory {model_dir} does not exist. Skipping.")
        return

    # 1. Model
    model_pkl = model_dir / "rf_model.pkl"
    model_json = model_dir / "rf_model.json"
    if model_pkl.exists() and not model_json.exists():
        try:
            print(f"Migrating model in {model_dir}...")
            # We must load it carefully. For safety and backwards compatibility,
            # this script allows `joblib.load` purely for the one-time migration.
            clf = joblib.load(model_pkl)
            if hasattr(clf, 'save_model'):
                clf.save_model(model_json)
                print(f"  -> Saved {model_json}")
            else:
                print(f"  -> Expected XGBClassifier with save_model, got {type(clf)}")
        except Exception as e:
            print(f"  -> Failed to migrate model: {e}")

    # 2. Scaler
    scaler_pkl = model_dir / "scaler.pkl"
    scaler_json = model_dir / "scaler.json"
    if scaler_pkl.exists() and not scaler_json.exists():
        try:
            print(f"Migrating scaler in {model_dir}...")
            scaler = joblib.load(scaler_pkl)
            scaler_data = {
                'mean_': scaler.mean_.tolist() if hasattr(scaler, 'mean_') else [0.0]*len(TARGET_COLS),
                'scale_': scaler.scale_.tolist() if hasattr(scaler, 'scale_') else [1.0]*len(TARGET_COLS)
            }
            with open(scaler_json, "w") as f:
                json.dump(scaler_data, f)
            print(f"  -> Saved {scaler_json}")
        except Exception as e:
            print(f"  -> Failed to migrate scaler: {e}")

    # 3. Features
    feat_pkl = model_dir / "selected_features.pkl"
    feat_json = model_dir / "selected_features.json"
    if feat_pkl.exists() and not feat_json.exists():
        try:
            print(f"Migrating selected_features in {model_dir}...")
            features = joblib.load(feat_pkl)
            # Ensure it is a basic list of strings
            if isinstance(features, np.ndarray):
                features = features.tolist()
            with open(feat_json, "w") as f:
                json.dump(features, f)
            print(f"  -> Saved {feat_json}")
        except Exception as e:
            print(f"  -> Failed to migrate features: {e}")

if __name__ == "__main__":
    dirs_to_check = [
        Path("models"),
        Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    ]
    print("Starting secure model migration...")
    for d in dirs_to_check:
        migrate_directory(d)
    print("Migration complete.")
