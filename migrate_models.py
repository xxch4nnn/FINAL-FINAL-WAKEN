import joblib
import json
import xgboost as xgb
from pathlib import Path
import numpy as np

def migrate():
    paths_to_check = [
        Path("models"),
        Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    ]

    for base_dir in paths_to_check:
        if not base_dir.exists():
            continue

        # Migrate rf_model.pkl
        rf_path = base_dir / "rf_model.pkl"
        if rf_path.exists():
            clf = joblib.load(rf_path)
            clf.save_model(str(base_dir / "rf_model.json"))
            print(f"Migrated {rf_path} to .json")

        # Migrate scaler.pkl
        scaler_path = base_dir / "scaler.pkl"
        if scaler_path.exists():
            scaler = joblib.load(scaler_path)
            scaler_data = {
                'mean_': scaler.mean_.tolist() if hasattr(scaler.mean_, 'tolist') else scaler.mean_,
                'scale_': scaler.scale_.tolist() if hasattr(scaler.scale_, 'tolist') else scaler.scale_
            }
            with open(base_dir / "scaler.json", 'w') as f:
                json.dump(scaler_data, f)
            print(f"Migrated {scaler_path} to .json")

        # Migrate selected_features.pkl
        feats_path = base_dir / "selected_features.pkl"
        if feats_path.exists():
            feats = joblib.load(feats_path)
            if hasattr(feats, 'tolist'):
                feats = feats.tolist()
            with open(base_dir / "selected_features.json", 'w') as f:
                json.dump(feats, f)
            print(f"Migrated {feats_path} to .json")

if __name__ == "__main__":
    migrate()
