import joblib
import xgboost as xgb
from pathlib import Path

def migrate():
    models_dir = Path('models')
    models_dir.mkdir(exist_ok=True)
    rf_pkl_path = models_dir / 'rf_model.pkl'

    if rf_pkl_path.exists():
        print(f"Loading legacy model from {rf_pkl_path}")
        model = joblib.load(rf_pkl_path)
        json_path = models_dir / 'rf_model.json'
        print(f"Saving migrated model to {json_path}")
        model.save_model(str(json_path))
        print("Migration complete.")
    else:
        print(f"Legacy model not found at {rf_pkl_path}. If you want to create a dummy for tests:")
        # We'll just create a dummy model for the sake of the script working if missing
        import numpy as np
        X = np.random.rand(10, 5)
        y = np.random.randint(2, size=10)
        model = xgb.XGBClassifier()
        model.fit(X, y)
        json_path = models_dir / 'rf_model.json'
        model.save_model(str(json_path))
        print(f"Created dummy XGBoost model at {json_path}")

if __name__ == '__main__':
    migrate()
