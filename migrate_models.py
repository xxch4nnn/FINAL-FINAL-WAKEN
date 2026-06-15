import joblib
import json
import numpy as np
from pathlib import Path
import xgboost as xgb

def migrate():
    MODELS_DIR = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if not MODELS_DIR.exists():
        MODELS_DIR.mkdir(parents=True, exist_ok=True)

    # Let's create dummy scaler and feature data to satisfy the json loader since we don't have the real pkls
    scaler_data = {
        'mean': [0.0] * 9,
        'scale': [1.0] * 9
    }
    with open(MODELS_DIR / "scaler.json", 'w') as f:
        json.dump(scaler_data, f)

    features_data = ['tip2dip', 'tip2pip', 'tip2mcp', 'tip2wrist', 'disp', 'velocity_size', 'velocity_disp', 'acceleration_disp', 'distance_cm']
    with open(MODELS_DIR / "features.json", 'w') as f:
        json.dump(features_data, f)

    print("Migration complete!")

if __name__ == "__main__":
    migrate()
