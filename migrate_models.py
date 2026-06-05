import joblib
import json
import xgboost as xgb
import numpy as np
from pathlib import Path

models_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")

def migrate():
    if not models_dir.exists():
        print("Models directory not found.")
        return

    m_path_pkl = models_dir / "rf_model.pkl"
    m_path_json = models_dir / "rf_model.json"
    s_path_pkl = models_dir / "scaler.pkl"
    s_path_json = models_dir / "scaler.json"
    f_path_pkl = models_dir / "selected_features.pkl"
    f_path_json = models_dir / "selected_features.json"

    if m_path_pkl.exists():
        model = joblib.load(m_path_pkl)
        model.save_model(str(m_path_json))
        print(f"Migrated model to {m_path_json}")

    if s_path_pkl.exists():
        scaler = joblib.load(s_path_pkl)
        with open(s_path_json, 'w') as f:
            json.dump({'mean_': scaler.mean_.tolist(), 'scale_': scaler.scale_.tolist()}, f)
        print(f"Migrated scaler to {s_path_json}")

    if f_path_pkl.exists():
        features = joblib.load(f_path_pkl)
        with open(f_path_json, 'w') as f:
            json.dump(features, f)
        print(f"Migrated features to {f_path_json}")

if __name__ == "__main__":
    migrate()
