import joblib
import xgboost as xgb
from pathlib import Path
import json

def migrate():
    # Migrate rf_model.pkl
    p = Path("models/rf_model.pkl")
    if p.exists():
        model = joblib.load(p)
        model.save_model("models/rf_model.json")
        print("Migrated rf_model.pkl to rf_model.json")

    # Migrate svm_model_100_rbg_scale.pkl (if needed to JSON, but sklearn doesn't support save_model)
    # Memory says: "Sklearn models (e.g., svm_model_100_rbg_scale.pkl) cannot be migrated to JSON using XGBoost's native save_model method."
    # We will just migrate rf_model.pkl for now.

if __name__ == "__main__":
    migrate()
