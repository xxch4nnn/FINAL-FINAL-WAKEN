import joblib
import xgboost as xgb
import json
import numpy as np
from pathlib import Path

# Paths for models (we will check multiple places to be sure)
model_dirs = [Path("models"), Path("Machine_Learning_Course/Data/PianoMotion10M/models")]

for model_dir in model_dirs:
    if not model_dir.exists():
        continue

    print(f"Migrating models in {model_dir}...")

    # 1. XGBoost Model
    rf_pkl = model_dir / "rf_model.pkl"
    rf_json = model_dir / "rf_model.json"
    if rf_pkl.exists():
        try:
            print(f"Loading {rf_pkl}...")
            clf = joblib.load(rf_pkl)
            if hasattr(clf, "save_model"):
                clf.save_model(rf_json)
                print(f"Successfully converted to {rf_json}")
            else:
                print(f"Model {rf_pkl} is not an XGBoost model, cannot use save_model.")
        except Exception as e:
            print(f"Failed to migrate {rf_pkl}: {e}")

    # 2. Scaler
    scaler_pkl = model_dir / "scaler.pkl"
    scaler_json = model_dir / "scaler.json"
    if scaler_pkl.exists():
        try:
            print(f"Loading {scaler_pkl}...")
            scaler = joblib.load(scaler_pkl)
            scaler_data = {
                "mean_": scaler.mean_.tolist() if hasattr(scaler, "mean_") else [0.0],
                "scale_": scaler.scale_.tolist() if hasattr(scaler, "scale_") else [1.0]
            }
            with open(scaler_json, "w") as f:
                json.dump(scaler_data, f)
            print(f"Successfully converted to {scaler_json}")
        except Exception as e:
            print(f"Failed to migrate {scaler_pkl}: {e}")

    # 3. Selected Features
    feat_pkl = model_dir / "selected_features.pkl"
    feat_json = model_dir / "selected_features.json"
    if feat_pkl.exists():
        try:
            print(f"Loading {feat_pkl}...")
            feats = joblib.load(feat_pkl)
            if isinstance(feats, np.ndarray):
                feats = feats.tolist()
            with open(feat_json, "w") as f:
                json.dump(feats, f)
            print(f"Successfully converted to {feat_json}")
        except Exception as e:
            print(f"Failed to migrate {feat_pkl}: {e}")
