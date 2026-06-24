import joblib, json
from pathlib import Path
import xgboost as xgb

def migrate():
    for d in [Path("models"), Path("Machine_Learning_Course/Data/PianoMotion10M/models")]:
        if (m := d / "rf_model.pkl").exists():
            model = joblib.load(m)
            model.save_model(str(m.with_suffix('.json')))
        if (s := d / "scaler.pkl").exists():
            sc = joblib.load(s)
            with open(s.with_suffix('.json'), 'w') as f:
                json.dump({'mean_': sc.mean_.tolist(), 'scale_': sc.scale_.tolist()}, f)
        if (f := d / "selected_features.pkl").exists():
            with open(f.with_suffix('.json'), 'w') as fh:
                data = joblib.load(f)
                if hasattr(data, 'tolist'):
                    data = data.tolist()
                json.dump(data, fh)

if __name__ == '__main__':
    migrate()
