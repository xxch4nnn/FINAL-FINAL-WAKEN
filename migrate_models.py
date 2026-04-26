import json
import joblib
import xgboost as xgb
from pathlib import Path
import os
import argparse

def migrate_model(pkl_path, json_path):
    if not os.path.exists(pkl_path):
        print(f"Skipping {pkl_path}, does not exist.")
        return
    print(f"Migrating model {pkl_path} -> {json_path}")
    try:
        model = joblib.load(pkl_path)
        # Assuming it's an xgboost model
        model.save_model(json_path)
        print("Success.")
    except Exception as e:
        print(f"Failed to migrate model {pkl_path}: {e}")

def migrate_scaler(pkl_path, json_path):
    if not os.path.exists(pkl_path):
        print(f"Skipping {pkl_path}, does not exist.")
        return
    print(f"Migrating scaler {pkl_path} -> {json_path}")
    try:
        scaler = joblib.load(pkl_path)
        # Assuming standard scaler or similar with mean_ and scale_
        scaler_data = {
            "mean_": scaler.mean_.tolist() if hasattr(scaler, "mean_") else None,
            "scale_": scaler.scale_.tolist() if hasattr(scaler, "scale_") else None
        }
        with open(json_path, 'w') as f:
            json.dump(scaler_data, f)
        print("Success.")
    except Exception as e:
        print(f"Failed to migrate scaler {pkl_path}: {e}")

def migrate_features(pkl_path, json_path):
    if not os.path.exists(pkl_path):
        print(f"Skipping {pkl_path}, does not exist.")
        return
    print(f"Migrating features {pkl_path} -> {json_path}")
    try:
        features = joblib.load(pkl_path)
        with open(json_path, 'w') as f:
            json.dump(list(features), f)
        print("Success.")
    except Exception as e:
        print(f"Failed to migrate features {pkl_path}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Migrate joblib/pickle models to JSON")
    parser.add_argument("--models-dir", default="models", help="Directory containing models")
    args = parser.parse_args()

    base_dir = Path(args.models_dir)
    migrate_model(base_dir / "rf_model.pkl", base_dir / "rf_model.json")
    migrate_scaler(base_dir / "scaler.pkl", base_dir / "scaler.json")
    migrate_features(base_dir / "selected_features.pkl", base_dir / "selected_features.json")
