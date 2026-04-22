import joblib
import json
import xgboost as xgb
from pathlib import Path
import sys
import os

def migrate(models_dir):
    models_dir = Path(models_dir)
    if not models_dir.exists():
        print(f"Directory {models_dir} does not exist.")
        return

    m_path = models_dir / "rf_model.pkl"
    s_path = models_dir / "scaler.pkl"
    f_path = models_dir / "selected_features.pkl"

    if m_path.exists():
        try:
            model = joblib.load(m_path)
            model.save_model(models_dir / "rf_model.json")
            print(f"Migrated model {m_path} to rf_model.json")
        except Exception as e:
            print(f"Failed to migrate model: {e}")

    if s_path.exists():
        try:
            scaler = joblib.load(s_path)
            if hasattr(scaler, 'mean_') and hasattr(scaler, 'scale_'):
                scaler_data = {
                    "mean": scaler.mean_.tolist(),
                    "scale": scaler.scale_.tolist()
                }
                with open(models_dir / "scaler.json", "w") as f:
                    json.dump(scaler_data, f)
                print(f"Migrated scaler {s_path} to scaler.json")
            else:
                print("Could not migrate scaler, missing mean_ or scale_ attribute")
        except Exception as e:
            print(f"Failed to migrate scaler: {e}")

    if f_path.exists():
        try:
            features = joblib.load(f_path)
            with open(models_dir / "selected_features.json", "w") as f:
                json.dump(features, f)
            print(f"Migrated features {f_path} to selected_features.json")
        except Exception as e:
            print(f"Failed to migrate features: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        migrate(sys.argv[1])
    else:
        migrate("models")
        migrate("Machine_Learning_Course/Data/PianoMotion10M/models")
