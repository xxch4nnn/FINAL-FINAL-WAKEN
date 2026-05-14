import joblib
import json
import xgboost as xgb
from pathlib import Path
import numpy as np

def migrate_model(pkl_path, json_path):
    print(f"Migrating model from {pkl_path} to {json_path}")
    try:
        model = joblib.load(pkl_path)
        if hasattr(model, 'save_model'):
            # It's an xgboost model
            model.save_model(json_path)
            print("Successfully migrated xgboost model.")
        else:
            print("Warning: Model is not an xgboost model, native save_model not available.")
    except Exception as e:
        print(f"Error migrating model: {e}")

def migrate_scaler(pkl_path, json_path):
    print(f"Migrating scaler from {pkl_path} to {json_path}")
    try:
        scaler = joblib.load(pkl_path)
        if hasattr(scaler, 'mean_') and hasattr(scaler, 'scale_'):
            data = {
                'mean_': scaler.mean_.tolist(),
                'scale_': scaler.scale_.tolist()
            }
            with open(json_path, 'w') as f:
                json.dump(data, f)
            print("Successfully migrated scaler.")
        else:
            print("Warning: Scaler does not have mean_ and scale_ attributes.")
    except Exception as e:
        print(f"Error migrating scaler: {e}")

def migrate_features(pkl_path, json_path):
    print(f"Migrating features from {pkl_path} to {json_path}")
    try:
        features = joblib.load(pkl_path)
        if isinstance(features, (list, np.ndarray)):
            if isinstance(features, np.ndarray):
                features = features.tolist()
            with open(json_path, 'w') as f:
                json.dump(features, f)
            print("Successfully migrated features.")
        else:
             print("Warning: Features format not recognized.")
    except Exception as e:
        print(f"Error migrating features: {e}")

if __name__ == "__main__":
    MODELS_DIR = Path("models")
    if not MODELS_DIR.exists():
        print(f"Models directory not found at {MODELS_DIR}")
    else:
        for pkl_file in MODELS_DIR.glob("*.pkl"):
            json_file = pkl_file.with_suffix('.json')
            if 'rf_model' in pkl_file.name:
                 migrate_model(pkl_file, json_file)
            elif 'scaler' in pkl_file.name:
                 migrate_scaler(pkl_file, json_file)
            elif 'features' in pkl_file.name:
                 migrate_features(pkl_file, json_file)
            else:
                 print(f"Unknown pkl file: {pkl_file.name}, skipping.")
