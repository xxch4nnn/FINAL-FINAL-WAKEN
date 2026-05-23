import joblib
import json
from pathlib import Path
import xgboost as xgb

MODELS_DIR = Path("models")

def migrate_scaler():
    pkl_path = MODELS_DIR / "scaler.pkl"
    json_path = MODELS_DIR / "scaler.json"
    if pkl_path.exists() and not json_path.exists():
        scaler = joblib.load(pkl_path)
        with open(json_path, 'w') as f:
            json.dump({'mean': scaler.mean_.tolist(), 'scale': scaler.scale_.tolist()}, f)
        print(f"Migrated {pkl_path} to {json_path}")

def migrate_features():
    pkl_path = MODELS_DIR / "selected_features.pkl"
    json_path = MODELS_DIR / "selected_features.json"
    if pkl_path.exists() and not json_path.exists():
        features = joblib.load(pkl_path)
        with open(json_path, 'w') as f:
            json.dump(features, f)
        print(f"Migrated {pkl_path} to {json_path}")

def migrate_rf_model():
    pkl_path = MODELS_DIR / "rf_model.pkl"
    json_path = MODELS_DIR / "rf_model.json"
    if pkl_path.exists() and not json_path.exists():
        model = joblib.load(pkl_path)
        model.save_model(str(json_path))
        print(f"Migrated {pkl_path} to {json_path}")

if __name__ == "__main__":
    print("Starting ML Model Migration...")
    migrate_scaler()
    migrate_features()
    migrate_rf_model()
    print("Migration Complete.")
