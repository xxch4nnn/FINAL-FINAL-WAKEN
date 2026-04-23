import joblib
import json
import os
import xgboost as xgb
from pathlib import Path

def migrate_dir(models_dir):
    models_dir = Path(models_dir)
    if not models_dir.exists():
        return

    print(f"Migrating artifacts in {models_dir}...")

    model_pkl = models_dir / "rf_model.pkl"
    model_json = models_dir / "rf_model.json"

    scaler_pkl = models_dir / "scaler.pkl"
    scaler_json = models_dir / "scaler.json"

    features_pkl = models_dir / "selected_features.pkl"
    features_json = models_dir / "selected_features.json"

    if model_pkl.exists():
        try:
            clf = joblib.load(model_pkl)
            if hasattr(clf, "save_model"):
                clf.save_model(model_json)
                print(f"  Successfully migrated {model_pkl} to {model_json}")
            else:
                print(f"  Skipping {model_pkl}: Not a valid XGBoost model.")
        except Exception as e:
            print(f"  Error migrating model: {e}")

    if scaler_pkl.exists():
        try:
            scaler = joblib.load(scaler_pkl)
            scaler_data = {
                "means": scaler.mean_.tolist() if hasattr(scaler, "mean_") else [0.0]*9,
                "scales": scaler.scale_.tolist() if hasattr(scaler, "scale_") else [1.0]*9
            }
            with open(scaler_json, "w") as f:
                json.dump(scaler_data, f)
            print(f"  Successfully migrated {scaler_pkl} to {scaler_json}")
        except Exception as e:
            print(f"  Error migrating scaler: {e}")

    if features_pkl.exists():
        try:
            features = joblib.load(features_pkl)
            with open(features_json, "w") as f:
                json.dump(list(features), f)
            print(f"  Successfully migrated {features_pkl} to {features_json}")
        except Exception as e:
            print(f"  Error migrating features: {e}")

if __name__ == "__main__":
    migrate_dir("models")
    migrate_dir("Machine_Learning_Course/Data/PianoMotion10M/models")