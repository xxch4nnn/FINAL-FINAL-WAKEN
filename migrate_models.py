import json
import joblib
import numpy as np
import xgboost as xgb
from pathlib import Path

def convert_scaler(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    scaler = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump({
            'mean_': scaler.mean_.tolist(),
            'scale_': scaler.scale_.tolist()
        }, f)
    print(f"Converted {pkl_path} to {json_path}")

def convert_features(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    features = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump(list(features), f)
    print(f"Converted {pkl_path} to {json_path}")

def convert_model(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    try:
        model = joblib.load(pkl_path)
        if hasattr(model, 'save_model'):
            model.save_model(str(json_path))
            print(f"Converted {pkl_path} to {json_path}")
        else:
            print(f"Warning: {pkl_path} is not an XGBoost model, skipping save_model.")
    except Exception as e:
        print(f"Failed to convert model {pkl_path}: {e}")

if __name__ == "__main__":
    base_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if base_dir.exists():
        convert_scaler(base_dir / "scaler.pkl", base_dir / "scaler.json")
        convert_features(base_dir / "selected_features.pkl", base_dir / "selected_features.json")
        convert_model(base_dir / "rf_model.pkl", base_dir / "rf_model.json")

    # Check current directory just in case
    convert_model("models/rf_model.pkl", "models/rf_model.json")

    convert_model("dt_model.pkl", "dt_model.json")
    convert_model("svm_model_100_rbg_scale.pkl", "svm_model_100_rbg_scale.json")
    print("Migration complete.")
