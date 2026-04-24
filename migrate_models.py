import json
import joblib
import xgboost as xgb
from pathlib import Path
import os
import glob

def migrate():
    # 1. Models dir (training output)
    models_dir = Path("models")
    if models_dir.exists():
        for pkl_file in glob.glob(str(models_dir / "*.pkl")):
            try:
                print(f"Migrating {pkl_file}...")
                model = joblib.load(pkl_file)
                if isinstance(model, xgb.XGBClassifier) or isinstance(model, xgb.Booster):
                    json_path = pkl_file.replace(".pkl", ".json")
                    model.save_model(json_path)
                    print(f"  -> Saved to {json_path}")
            except Exception as e:
                print(f"  Failed to migrate {pkl_file}: {e}")

    # 2. Machine Learning Course dir (runtime models)
    runtime_models_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if runtime_models_dir.exists():
        # Model
        m_path = runtime_models_dir / "rf_model.pkl"
        if m_path.exists():
            try:
                print(f"Migrating {m_path}...")
                model = joblib.load(m_path)
                if isinstance(model, xgb.XGBClassifier) or isinstance(model, xgb.Booster):
                    json_path = str(m_path).replace(".pkl", ".json")
                    model.save_model(json_path)
                    print(f"  -> Saved to {json_path}")
            except Exception as e:
                print(f"  Failed to migrate {m_path}: {e}")

        # Scaler
        s_path = runtime_models_dir / "scaler.pkl"
        if s_path.exists():
            try:
                print(f"Migrating {s_path}...")
                scaler = joblib.load(s_path)
                # Assuming StandardScaler or similar with mean_ and scale_
                if hasattr(scaler, 'mean_') and hasattr(scaler, 'scale_'):
                    scaler_data = {
                        "mean_": scaler.mean_.tolist(),
                        "scale_": scaler.scale_.tolist()
                    }
                    json_path = str(s_path).replace(".pkl", ".json")
                    with open(json_path, 'w') as f:
                        json.dump(scaler_data, f)
                    print(f"  -> Saved to {json_path}")
            except Exception as e:
                print(f"  Failed to migrate {s_path}: {e}")

        # Features
        f_path = runtime_models_dir / "selected_features.pkl"
        if f_path.exists():
            try:
                print(f"Migrating {f_path}...")
                features = joblib.load(f_path)
                json_path = str(f_path).replace(".pkl", ".json")
                with open(json_path, 'w') as f:
                    json.dump(list(features), f)
                print(f"  -> Saved to {json_path}")
            except Exception as e:
                print(f"  Failed to migrate {f_path}: {e}")

if __name__ == "__main__":
    migrate()
