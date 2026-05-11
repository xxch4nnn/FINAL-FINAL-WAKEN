import joblib
import json
import xgboost as xgb
import numpy as np
from pathlib import Path
import warnings

# Suppress inconsistent version warnings during migration
warnings.filterwarnings("ignore", category=UserWarning)

def migrate():
    print("Starting ML Model Migration to secure JSON formats...")
    for p in Path(".").rglob("*.pkl"):
        # Skip temporary files
        if "venv" in str(p) or ".pyenv" in str(p):
            continue

        print(f"Processing {p}...")
        try:
            obj = joblib.load(p)

            # Identify what we loaded
            if isinstance(obj, xgb.XGBClassifier):
                out_path = p.with_suffix('.json')
                obj.save_model(str(out_path))
                print(f" -> Migrated XGBClassifier to {out_path}")

            elif hasattr(obj, 'mean_') and hasattr(obj, 'scale_'):
                # It's likely a Scaler
                out_path = p.with_suffix('.json')
                scaler_data = {
                    'mean': obj.mean_.tolist(),
                    'scale': obj.scale_.tolist()
                }
                with open(out_path, 'w') as f:
                    json.dump(scaler_data, f, indent=2)
                print(f" -> Migrated Scaler to {out_path}")

            elif isinstance(obj, list) and len(obj) > 0 and isinstance(obj[0], str):
                # Likely feature list
                out_path = p.with_suffix('.json')
                with open(out_path, 'w') as f:
                    json.dump(obj, f, indent=2)
                print(f" -> Migrated Feature List to {out_path}")

            else:
                print(f" -> Skipping {p}: Unknown or unsupported object type: {type(obj)}")

        except Exception as e:
            print(f" -> Failed to process {p}: {e}")

if __name__ == "__main__":
    migrate()
