import joblib
import xgboost as xgb
from pathlib import Path

def migrate():
    p = Path('models/rf_model.pkl')
    if p.exists():
        model = joblib.load(p)
        model.save_model('models/rf_model.json')
        print("Migrated models/rf_model.pkl to .json")
    else:
        print(f"File {p} not found.")

if __name__ == "__main__":
    migrate()
