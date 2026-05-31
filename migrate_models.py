import joblib
import numpy as np
class DummyScaler:
    pass

import json
import sys
import xgboost as xgb
from pathlib import Path

def migrate():
    models_to_convert = [
        "dt_model.pkl",
        "svm_model_100_rbg_scale.pkl",
        "models/scaler.pkl",
        "models/selected_features.pkl",
        "models/rf_model.pkl"
    ]

    for p in models_to_convert:
        path = Path(p)
        if not path.exists():
            continue

        print(f"Migrating {p}...")
        obj = joblib.load(path)
        out_path = path.with_suffix('.json')

        if "scaler" in p:
            with open(out_path, 'w') as f:
                json.dump({
                    'mean_': obj.mean_.tolist(),
                    'scale_': obj.scale_.tolist()
                }, f)
        elif "features" in p:
            with open(out_path, 'w') as f:
                json.dump(list(obj), f)
        elif "rf_model" in p or isinstance(obj, xgb.XGBClassifier):
            if hasattr(obj, 'save_model'):
                obj.save_model(str(out_path))
        else:
            model_data = {'type': type(obj).__name__}
            if hasattr(obj, 'support_vectors_'):
                model_data['support_vectors_'] = obj.support_vectors_.tolist()
            if hasattr(obj, 'classes_'):
                model_data['classes_'] = obj.classes_.tolist()
            with open(out_path, 'w') as f:
                json.dump(model_data, f)
        print(f"Migrated successfully to {out_path}")

if __name__ == "__main__":
    migrate()

class DummyScaler:
    pass
