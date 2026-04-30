import joblib
import json
from pathlib import Path

def migrate():
    models_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if not models_dir.exists():
        print(f"Directory {models_dir} not found. Skipping migration.")
        return

    pkl_model = models_dir / "rf_model.pkl"
    json_model = models_dir / "rf_model.json"
    if pkl_model.exists():
        clf = joblib.load(pkl_model)
        clf.save_model(json_model)
        print(f"Migrated model to {json_model}")

    pkl_scaler = models_dir / "scaler.pkl"
    json_scaler = models_dir / "scaler.json"
    if pkl_scaler.exists():
        scaler = joblib.load(pkl_scaler)
        with open(json_scaler, 'w') as f:
            json.dump({"mean": scaler.mean_.tolist(), "scale": scaler.scale_.tolist()}, f)
        print(f"Migrated scaler to {json_scaler}")

    pkl_feat = models_dir / "selected_features.pkl"
    json_feat = models_dir / "selected_features.json"
    if pkl_feat.exists():
        feat = joblib.load(pkl_feat)
        with open(json_feat, 'w') as f:
            json.dump(feat, f)
        print(f"Migrated features to {json_feat}")

if __name__ == "__main__":
    migrate()
