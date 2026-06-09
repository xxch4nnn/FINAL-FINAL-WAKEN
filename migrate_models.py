import joblib
import xgboost as xgb
import json
from pathlib import Path
import numpy as np

def migrate():
    models_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if not models_dir.exists():
        models_dir = Path("models")
    if not models_dir.exists():
        models_dir.mkdir(exist_ok=True, parents=True)

    rf_pkl = models_dir / "rf_model.pkl"
    rf_json = models_dir / "rf_model.json"
    if rf_pkl.exists():
        clf = joblib.load(rf_pkl)
        clf.save_model(str(rf_json))

    scaler_pkl = models_dir / "scaler.pkl"
    scaler_json = models_dir / "scaler.json"
    if scaler_pkl.exists():
        scaler = joblib.load(scaler_pkl)
        scaler_dict = {
            'mean_': scaler.mean_.tolist() if hasattr(scaler.mean_, 'tolist') else list(scaler.mean_),
            'scale_': scaler.scale_.tolist() if hasattr(scaler.scale_, 'tolist') else list(scaler.scale_)
        }
        with open(scaler_json, 'w') as f:
            json.dump(scaler_dict, f)

    feat_pkl = models_dir / "selected_features.pkl"
    feat_json = models_dir / "selected_features.json"
    if feat_pkl.exists():
        feats = joblib.load(feat_pkl)
        with open(feat_json, 'w') as f:
            json.dump(feats, f)

if __name__ == "__main__":
    migrate()
