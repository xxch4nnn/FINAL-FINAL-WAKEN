import joblib
import json
import xgboost as xgb
from pathlib import Path
import numpy as np

MODELS_DIR = Path("models")

def migrate_scaler():
    s_path = MODELS_DIR / "scaler.pkl"
    if s_path.exists():
        print("Migrating scaler...")
        scaler = joblib.load(s_path)
        scaler_data = {
            "mean_": scaler.mean_.tolist() if hasattr(scaler.mean_, 'tolist') else scaler.mean_,
            "scale_": scaler.scale_.tolist() if hasattr(scaler.scale_, 'tolist') else scaler.scale_
        }
        with open(MODELS_DIR / "scaler.json", "w") as f:
            json.dump(scaler_data, f)
        print("Scaler migrated.")
    else:
        print("scaler.pkl not found.")

def migrate_features():
    f_path = MODELS_DIR / "selected_features.pkl"
    if f_path.exists():
        print("Migrating selected_features...")
        features = joblib.load(f_path)
        # Assuming it's a list or similar
        features_data = features.tolist() if hasattr(features, 'tolist') else list(features)
        with open(MODELS_DIR / "selected_features.json", "w") as f:
            json.dump(features_data, f)
        print("Features migrated.")
    else:
        print("selected_features.pkl not found.")

def migrate_model():
    m_path = MODELS_DIR / "rf_model.pkl"
    if m_path.exists():
        print("Migrating rf_model...")
        try:
            model = joblib.load(m_path)
            if hasattr(model, 'save_model'):
                model.save_model(str(MODELS_DIR / "rf_model.json"))
                print("Model migrated.")
            else:
                print("Loaded model is not an XGBoost model with save_model method.")
        except Exception as e:
            print(f"Error migrating model: {e}")
    else:
        print("rf_model.pkl not found.")

if __name__ == "__main__":
    migrate_scaler()
    migrate_features()
    migrate_model()
