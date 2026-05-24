import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate():
    models_dir = Path("models")
    if not models_dir.exists(): return

    # 1. Scaler
    s_pkl = models_dir / "scaler.pkl"
    if s_pkl.exists():
        scaler = joblib.load(s_pkl)
        with open(models_dir / "scaler.json", "w") as f:
            json.dump({"mean": scaler.mean_.tolist(), "scale": scaler.scale_.tolist()}, f)

    # 2. Features
    f_pkl = models_dir / "selected_features.pkl"
    if f_pkl.exists():
        feats = joblib.load(f_pkl)
        with open(models_dir / "selected_features.json", "w") as f:
            json.dump(feats, f)

    # 3. Model
    m_pkl = models_dir / "rf_model.pkl"
    if m_pkl.exists():
        model = joblib.load(m_pkl)
        model.save_model(str(models_dir / "rf_model.json"))

if __name__ == "__main__":
    migrate()
