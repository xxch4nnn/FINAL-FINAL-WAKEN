import joblib
import json
from pathlib import Path

# Paths to check
paths = [Path("models"), Path("Machine_Learning_Course/Data/PianoMotion10M/models")]

for p in paths:
    if not p.exists(): continue

    m_path = p / "rf_model.pkl"
    s_path = p / "scaler.pkl"
    f_path = p / "selected_features.pkl"

    if m_path.exists():
        model = joblib.load(m_path)
        model.save_model(p / "rf_model.json")
        print(f"Migrated model in {p}")

    if s_path.exists():
        scaler = joblib.load(s_path)
        with open(p / "scaler.json", "w") as f:
            json.dump({"mean": scaler.mean_.tolist(), "scale": scaler.scale_.tolist()}, f)
        print(f"Migrated scaler in {p}")

    if f_path.exists():
        features = joblib.load(f_path)
        with open(p / "selected_features.json", "w") as f:
            json.dump(features, f)
        print(f"Migrated features in {p}")
