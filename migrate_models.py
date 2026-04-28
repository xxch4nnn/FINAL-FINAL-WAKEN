import joblib
import json
import xgboost as xgb
from pathlib import Path
import os

def migrate():
    # Attempt to load and migrate the main runtime models if they exist
    CONFIG_MODELS_DIR = Path("Machine_Learning_Course/Data/PianoMotion10M/models")

    # 1. Migrate Main Runtime Scaler
    s_path = CONFIG_MODELS_DIR / "scaler.pkl"
    s_json_path = CONFIG_MODELS_DIR / "scaler.json"
    if s_path.exists():
        try:
            scaler = joblib.load(s_path)
            # Create a simple JSON representation of the scaler (assuming StandardScaler or similar)
            # A scaler has `mean_` and `scale_` attributes usually
            scaler_dict = {}
            if hasattr(scaler, 'mean_'):
                scaler_dict['mean_'] = scaler.mean_.tolist()
            if hasattr(scaler, 'scale_'):
                scaler_dict['scale_'] = scaler.scale_.tolist()
            elif hasattr(scaler, 'var_'):
                scaler_dict['var_'] = scaler.var_.tolist()

            with open(s_json_path, 'w') as f:
                json.dump(scaler_dict, f)
            print(f"Migrated {s_path} to {s_json_path}")
        except Exception as e:
            print(f"Error migrating scaler: {e}")

    # 2. Migrate Main Runtime Selected Features
    f_path = CONFIG_MODELS_DIR / "selected_features.pkl"
    f_json_path = CONFIG_MODELS_DIR / "selected_features.json"
    if f_path.exists():
        try:
            features = joblib.load(f_path)
            with open(f_json_path, 'w') as f:
                json.dump(list(features), f)
            print(f"Migrated {f_path} to {f_json_path}")
        except Exception as e:
            print(f"Error migrating features: {e}")

    # 3. Migrate XGBoost Model
    # It might be in models/ or Machine_Learning_Course/...
    model_paths = [
        Path("models/rf_model.pkl"),
        CONFIG_MODELS_DIR / "rf_model.pkl"
    ]

    for m_path in model_paths:
        if m_path.exists():
            try:
                # joblib load it, then use xgb native save
                model = joblib.load(m_path)
                m_json_path = m_path.with_suffix('.json')

                if hasattr(model, 'save_model'):
                    model.save_model(m_json_path)
                elif hasattr(model, 'get_booster'):
                    model.get_booster().save_model(m_json_path)
                else:
                    print(f"Model {m_path} doesn't seem to be an XGBoost model that can be saved directly.")
                    continue

                print(f"Migrated {m_path} to {m_json_path}")
            except Exception as e:
                print(f"Error migrating model {m_path}: {e}")

if __name__ == "__main__":
    migrate()
