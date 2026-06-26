import joblib
import xgboost as xgb
import json
import numpy as np
from pathlib import Path

def migrate_legacy_model(pkl_path="models/rf_model.pkl", json_path="models/rf_model.json"):
    p = Path(pkl_path)
    if p.exists():
        model = joblib.load(p)
        model.save_model(str(Path(json_path)))
        print(f"Migrated {pkl_path} to {json_path}")
    else:
        print(f"File not found: {pkl_path}")

if __name__ == "__main__":
    migrate_legacy_model()
