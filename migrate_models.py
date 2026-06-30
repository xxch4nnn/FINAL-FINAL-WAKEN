import joblib
import json
import xgboost as xgb
from pathlib import Path
import numpy as np
from sklearn.preprocessing import StandardScaler

def migrate():
    print("Starting migration of ML artifacts from .pkl to .json...")

    # 1. train_gpu.py model
    model_dir = Path("models")
    rf_pkl = model_dir / "rf_model.pkl"
    rf_json = model_dir / "rf_model.json"

    if rf_pkl.exists():
        try:
            print(f"Migrating {rf_pkl}...")
            model = joblib.load(rf_pkl)
            model.save_model(str(rf_json))
            print(f"✅ Successfully created {rf_json}")
        except Exception as e:
            print(f"❌ Failed to migrate {rf_pkl}: {e}")

    # 2. main_runtime.py models
    rt_model_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    rt_rf_pkl = rt_model_dir / "rf_model.pkl"
    rt_rf_json = rt_model_dir / "rf_model.json"

    if rt_rf_pkl.exists():
         try:
             print(f"Migrating {rt_rf_pkl}...")
             model = joblib.load(rt_rf_pkl)
             model.save_model(str(rt_rf_json))
             print(f"✅ Successfully created {rt_rf_json}")
         except Exception as e:
             print(f"❌ Failed to migrate {rt_rf_pkl}: {e}")

    # 3. Scaler
    scaler_pkl = rt_model_dir / "scaler.pkl"
    scaler_json = rt_model_dir / "scaler.json"
    if scaler_pkl.exists():
        try:
            print(f"Migrating {scaler_pkl}...")
            scaler = joblib.load(scaler_pkl)
            scaler_data = {
                "mean_": scaler.mean_.tolist() if hasattr(scaler.mean_, 'tolist') else scaler.mean_,
                "scale_": scaler.scale_.tolist() if hasattr(scaler.scale_, 'tolist') else scaler.scale_
            }
            with open(scaler_json, 'w') as f:
                json.dump(scaler_data, f)
            print(f"✅ Successfully created {scaler_json}")
        except Exception as e:
             print(f"❌ Failed to migrate {scaler_pkl}: {e}")

    # 4. Features
    feats_pkl = rt_model_dir / "selected_features.pkl"
    feats_json = rt_model_dir / "selected_features.json"
    if feats_pkl.exists():
        try:
            print(f"Migrating {feats_pkl}...")
            feats = joblib.load(feats_pkl)
            with open(feats_json, 'w') as f:
                json.dump(feats, f)
            print(f"✅ Successfully created {feats_json}")
        except Exception as e:
             print(f"❌ Failed to migrate {feats_pkl}: {e}")

if __name__ == "__main__":
    migrate()
