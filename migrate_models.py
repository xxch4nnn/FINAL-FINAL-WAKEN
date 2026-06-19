import joblib
import xgboost as xgb
from pathlib import Path

def migrate():
    legacy_model_path = Path("models/rf_model.pkl")
    new_model_path = Path("models/rf_model.json")

    if legacy_model_path.exists():
        print(f"Migrating {legacy_model_path} to {new_model_path}")
        model = joblib.load(legacy_model_path)
        model.save_model(str(new_model_path))
        print("Migration complete.")
    else:
        print(f"No legacy model found at {legacy_model_path}")

if __name__ == "__main__":
    migrate()
