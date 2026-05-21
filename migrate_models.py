import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate():
    models_dir = Path("models")
    rf_pkl = models_dir / "rf_model.pkl"
    if rf_pkl.exists():
        model = joblib.load(rf_pkl)
        model.save_model(str(models_dir / "rf_model.json"))
        print("Migrated rf_model.pkl")

    scaler_pkl = models_dir / "scaler.pkl"
    if scaler_pkl.exists():
        scaler = joblib.load(scaler_pkl)
        with open(models_dir / "scaler.json", "w") as f:
            json.dump({"mean": scaler.mean_.tolist(), "scale": scaler.scale_.tolist()}, f)
        print("Migrated scaler.pkl")

    features_pkl = models_dir / "selected_features.pkl"
    if features_pkl.exists():
        features = joblib.load(features_pkl)
        with open(models_dir / "selected_features.json", "w") as f:
            json.dump(features, f)
        print("Migrated selected_features.pkl")

if __name__ == "__main__":
    migrate()