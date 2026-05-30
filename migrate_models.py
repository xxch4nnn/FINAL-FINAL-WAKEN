import joblib
import json
from pathlib import Path

for p in Path('.').rglob('*.pkl'):
    m = joblib.load(p)
    out = str(p).replace('.pkl', '.json')
    if hasattr(m, 'save_model'):
        m.save_model(out)
    elif hasattr(m, 'mean_'):
        json.dump({'mean': m.mean_.tolist(), 'scale': m.scale_.tolist()}, open(out, 'w'))
    elif isinstance(m, list):
        json.dump(m, open(out, 'w'))
    else:
        try:
            json.dump(m.get_params(), open(out, 'w'))
        except:
            pass
