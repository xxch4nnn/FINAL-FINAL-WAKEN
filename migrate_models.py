import joblib
import json
import xgboost as xgb
from pathlib import Path
import sys
import numpy as np

def migrate():
    models_dir = Path("models")
    if not models_dir.exists():
        print(f"Skipping migration, {models_dir} does not exist.")
        return

    # 1. Migrate Model (XGBoost)
    pkl_model_path = models_dir / "rf_model.pkl"
    json_model_path = models_dir / "rf_model.json"
    if pkl_model_path.exists() and not json_model_path.exists():
        try:
            clf = joblib.load(pkl_model_path)
            clf.save_model(str(json_model_path))
            print("Migrated model to JSON.")
        except Exception as e:
            print(f"Error migrating model: {e}")

    # 2. Migrate Scaler
    pkl_scaler_path = models_dir / "scaler.pkl"
    json_scaler_path = models_dir / "scaler.json"
    if pkl_scaler_path.exists() and not json_scaler_path.exists():
        try:
            scaler = joblib.load(pkl_scaler_path)
            scaler_data = {
                'mean': scaler.mean_.tolist(),
                'scale': scaler.scale_.tolist()
            }
            with open(json_scaler_path, 'w') as f:
                json.dump(scaler_data, f)
            print("Migrated scaler to JSON.")
        except Exception as e:
            print(f"Error migrating scaler: {e}")

    # 3. Migrate Features
    pkl_features_path = models_dir / "selected_features.pkl"
    json_features_path = models_dir / "selected_features.json"
    if pkl_features_path.exists() and not json_features_path.exists():
        try:
            features = joblib.load(pkl_features_path)
            if isinstance(features, np.ndarray):
                features = features.tolist()
            with open(json_features_path, 'w') as f:
                json.dump(features, f)
            print("Migrated features to JSON.")
        except Exception as e:
            print(f"Error migrating features: {e}")

if __name__ == "__main__":
    migrate()
