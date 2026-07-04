import joblib
import xgboost as xgb
from pathlib import Path
import os

rf_model_path = Path("models/rf_model.pkl")
new_rf_model_path = Path("models/rf_model.json")

print("Checking models...")
if rf_model_path.exists():
    try:
        model = joblib.load(rf_model_path)
        print("Loaded rf_model.pkl")
        model.save_model(str(new_rf_model_path))
        print("Saved rf_model.json")
    except Exception as e:
        print(f"Error: {e}")
