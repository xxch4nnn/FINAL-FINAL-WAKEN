import joblib
import json
from pathlib import Path

def migrate():
    for p in Path('.').rglob('*.pkl'):
        try:
            if 'scaler' in p.name:
                obj = joblib.load(p)
                with open(p.with_suffix('.json'), 'w') as f:
                    json.dump({'mean_': obj.mean_.tolist(), 'scale_': obj.scale_.tolist()}, f)
            elif 'features' in p.name:
                obj = joblib.load(p)
                with open(p.with_suffix('.json'), 'w') as f:
                    json.dump(list(obj), f)
            elif 'rf_model' in p.name:
                obj = joblib.load(p)
                obj.save_model(str(p.with_suffix('.json')))
        except Exception as e:
            print(f"Failed to migrate {p}: {e}")

if __name__ == '__main__':
    migrate()
