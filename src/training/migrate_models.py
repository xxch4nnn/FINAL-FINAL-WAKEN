import joblib
import json
import xgboost as xgb
from pathlib import Path
import numpy as np

def migrate():
    # Migrate XGBoost model
    p = Path("models/rf_model.pkl")
    if p.exists():
        model = joblib.load(p)
        model.save_model(str(p.with_suffix(".json")))
        print(f"Migrated {p} to JSON.")

    # Migrate scaler or other non-XGBoost objects as example
    s = Path("models/scaler.pkl")
    if s.exists():
        scaler = joblib.load(s)
        data = {}
        for attr in ['mean_', 'scale_']:
            if hasattr(scaler, attr):
                val = getattr(scaler, attr)
                data[attr] = val.tolist() if hasattr(val, 'tolist') else val
        with open(s.with_suffix(".json"), "w") as f:
            json.dump(data, f)
        print(f"Migrated {s} to JSON.")

if __name__ == "__main__":
    migrate()
