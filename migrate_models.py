import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate_dir(models_dir):
    if not models_dir.exists():
        return

    rf_pkl = models_dir / "rf_model.pkl"
    if rf_pkl.exists():
        model = joblib.load(rf_pkl)
        model.save_model(str(models_dir / "rf_model.json"))

    scaler_pkl = models_dir / "scaler.pkl"
    if scaler_pkl.exists():
        scaler = joblib.load(scaler_pkl)
        with open(models_dir / "scaler.json", "w") as f:
            json.dump({
                "mean_": scaler.mean_.tolist(),
                "scale_": scaler.scale_.tolist()
            }, f)

    features_pkl = models_dir / "selected_features.pkl"
    if features_pkl.exists():
        features = joblib.load(features_pkl)
        if hasattr(features, "tolist"):
            features = features.tolist()
        with open(models_dir / "selected_features.json", "w") as f:
            json.dump(features, f)

if __name__ == "__main__":
    migrate_dir(Path("Machine_Learning_Course/Data/PianoMotion10M/models"))
    migrate_dir(Path("models"))
