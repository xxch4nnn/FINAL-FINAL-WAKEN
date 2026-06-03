import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate_dir(d):
    d = Path(d)
    if not d.exists(): return
    mp = d / "rf_model.pkl"
    sp = d / "scaler.pkl"
    fp = d / "selected_features.pkl"

    if mp.exists():
        clf = joblib.load(mp)
        clf.save_model(d / "rf_model.json")
    if sp.exists():
        scaler = joblib.load(sp)
        with open(d / "scaler.json", 'w') as f:
            json.dump({'mean_': scaler.mean_.tolist(), 'scale_': scaler.scale_.tolist()}, f)
    if fp.exists():
        feats = joblib.load(fp)
        with open(d / "selected_features.json", 'w') as f:
            json.dump(list(feats), f)

if __name__ == "__main__":
    migrate_dir("models")
    migrate_dir("Machine_Learning_Course/Data/PianoMotion10M/models")
