import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate():
    MODELS_DIR = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    MODELS_DIR.mkdir(parents=True, exist_ok=True)
    legacy_model_path = MODELS_DIR / "rf_model.pkl"
    legacy_scaler_path = MODELS_DIR / "scaler.pkl"
    legacy_features_path = MODELS_DIR / "selected_features.pkl"

    if legacy_model_path.exists():
        model = joblib.load(legacy_model_path)
        if isinstance(model, xgb.XGBClassifier):
            model.save_model(str(MODELS_DIR / "rf_model.json"))

    if legacy_scaler_path.exists():
        scaler = joblib.load(legacy_scaler_path)
        scaler_data = {"mean_": scaler.mean_.tolist(), "scale_": scaler.scale_.tolist()}
        with open(MODELS_DIR / "scaler.json", "w") as f:
            json.dump(scaler_data, f)

    if legacy_features_path.exists():
        features = joblib.load(legacy_features_path)
        with open(MODELS_DIR / "selected_features.json", "w") as f:
            json.dump(list(features), f)

if __name__ == "__main__":
    migrate()
