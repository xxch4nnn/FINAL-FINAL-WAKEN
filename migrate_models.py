import joblib
import json
import xgboost as xgb
from pathlib import Path
import numpy as np

def migrate():
    print("Starting migration of legacy ML artifacts...")
    model_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if not model_dir.exists():
        model_dir = Path("models")

    m_path_pkl = model_dir / "rf_model.pkl"
    s_path_pkl = model_dir / "scaler.pkl"
    f_path_pkl = model_dir / "selected_features.pkl"

    m_path_json = model_dir / "rf_model.json"
    s_path_json = model_dir / "scaler.json"
    f_path_json = model_dir / "selected_features.json"

    # Migrate Model
    if m_path_pkl.exists():
        try:
            print(f"Migrating model {m_path_pkl} to JSON...")
            model = joblib.load(m_path_pkl)

            # Reconstruct XGBoost model and save
            if hasattr(model, 'save_model'):
                model.save_model(str(m_path_json))
                print(f"Successfully migrated model to {m_path_json}")
            else:
                print("Warning: Loaded model doesn't have save_model method. Ensure it is an XGBoost model.")
        except Exception as e:
            print(f"Error migrating model: {e}")
    else:
        print(f"Model file {m_path_pkl} not found. Skipping model migration.")

    # Migrate Scaler
    if s_path_pkl.exists():
        try:
            print(f"Migrating scaler {s_path_pkl} to JSON...")
            scaler = joblib.load(s_path_pkl)
            scaler_data = {
                'mean_': scaler.mean_.tolist(),
                'scale_': scaler.scale_.tolist()
            }
            with open(s_path_json, 'w') as f:
                json.dump(scaler_data, f)
            print(f"Successfully migrated scaler to {s_path_json}")
        except Exception as e:
            print(f"Error migrating scaler: {e}")
    else:
        print(f"Scaler file {s_path_pkl} not found. Skipping scaler migration.")

    # Migrate Features
    if f_path_pkl.exists():
        try:
            print(f"Migrating features {f_path_pkl} to JSON...")
            features = joblib.load(f_path_pkl)
            if isinstance(features, np.ndarray):
                features = features.tolist()
            elif hasattr(features, 'to_list'):
                features = features.to_list()
            with open(f_path_json, 'w') as f:
                json.dump(features, f)
            print(f"Successfully migrated features to {f_path_json}")
        except Exception as e:
            print(f"Error migrating features: {e}")
    else:
        print(f"Features file {f_path_pkl} not found. Skipping features migration.")

if __name__ == "__main__":
    migrate()
