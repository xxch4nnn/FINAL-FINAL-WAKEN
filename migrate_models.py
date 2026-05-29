import joblib
import json
from pathlib import Path
import sys

def migrate():
    models_dir = Path("models")

    if not models_dir.exists():
        print("models/ directory not found.")
        sys.exit(1)

    scaler_path = models_dir / "scaler.pkl"
    features_path = models_dir / "selected_features.pkl"

    if scaler_path.exists():
        print(f"Migrating {scaler_path}...")
        scaler = joblib.load(scaler_path)
        with open(models_dir / "scaler.json", 'w') as f:
            json.dump({"mean": scaler.mean_.tolist(), "scale": scaler.scale_.tolist()}, f)

    if features_path.exists():
        print(f"Migrating {features_path}...")
        features = joblib.load(features_path)
        with open(models_dir / "selected_features.json", 'w') as f:
            json.dump(list(features), f)

    print("Migration complete!")

if __name__ == "__main__":
    migrate()