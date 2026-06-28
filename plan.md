1. **Remove `joblib` and `pickle` imports and usage.**
   - Update `src/runtime/vision_engine.py` using `replace_with_git_merge_diff` with explicit blocks:
```
<<<<<<< SEARCH
import numpy as np
import pickle
from pathlib import Path
=======
import numpy as np
import xgboost as xgb
import json
from pathlib import Path
>>>>>>> REPLACE
```
```
<<<<<<< SEARCH
    def __init__(self, model_path="models/rf_model.pkl"):
        self.extractor = HandFeatureExtractor()
=======
    def __init__(self, model_path="models/rf_model.json"):
        self.extractor = HandFeatureExtractor()
>>>>>>> REPLACE
```
```
<<<<<<< SEARCH
    def _load_model(self, path):
        p = Path(path)
        if not p.exists():
            print(f"Warning: Model not found at {p}. Predictions will be dummy.")
            return None
        with open(p, 'rb') as f:
            return pickle.load(f)
=======
    def _load_model(self, path):
        p = Path(path)
        # Attempt secure fallback for legacy models
        if p.suffix == '.pkl':
            p = p.with_suffix('.json')
        if not p.exists():
            print(f"Warning: Model not found at {p}. Predictions will be dummy.")
            return None
        try:
            model = xgb.XGBClassifier()
            model.load_model(str(p))
            return model
        except Exception as e:
            print(f"Failed to load model from {p}: {e}")
            return None
>>>>>>> REPLACE
```

   - Update `main_runtime.py` using `replace_with_git_merge_diff` with explicit blocks:
```
<<<<<<< SEARCH
import mediapipe as mp
import pygame
import joblib
import time
=======
import mediapipe as mp
import pygame
import xgboost as xgb
import json
import time
>>>>>>> REPLACE
```
```
<<<<<<< SEARCH
    'MODELS_DIR': Path("Machine_Learning_Course/Data/PianoMotion10M/models"),
    'SCALER_NAME': "scaler.pkl",
    'MODEL_NAME': "rf_model.pkl",
    'FEATURES_NAME': "selected_features.pkl"
}
=======
    'MODELS_DIR': Path("Machine_Learning_Course/Data/PianoMotion10M/models"),
    'SCALER_NAME': "scaler.json",
    'MODEL_NAME': "rf_model.json",
    'FEATURES_NAME': "selected_features.json"
}

class JSONScaler:
    def __init__(self, path):
        with open(path, 'r') as f:
            data = json.load(f)
            self.mean_ = np.array(data['mean_'])
            self.scale_ = np.array(data['scale_'])

    def transform(self, X):
        X = np.asarray(X)
        return (X - self.mean_) / self.scale_
>>>>>>> REPLACE
```
```
<<<<<<< SEARCH
            if m_path.exists() and s_path.exists() and f_path.exists():
                self.model = joblib.load(m_path)
                self.scaler = joblib.load(s_path)
                self.selected_features = joblib.load(f_path)
                self.has_model = True
=======
            if m_path.exists() and s_path.exists() and f_path.exists():
                self.model = xgb.XGBClassifier()
                self.model.load_model(str(m_path))
                self.scaler = JSONScaler(s_path)
                with open(f_path, 'r') as f:
                    self.selected_features = json.load(f)
                self.has_model = True
>>>>>>> REPLACE
```

   - Update `src/training/train_gpu.py` using `replace_with_git_merge_diff` with explicit blocks:
```
<<<<<<< SEARCH
import numpy as np
import xgboost as xgb
import joblib
from pathlib import Path
=======
import numpy as np
import xgboost as xgb
from pathlib import Path
>>>>>>> REPLACE
```
```
<<<<<<< SEARCH
DATA_PATH = Path("data/main_dataset.csv") # Adjust path as needed
MODEL_DIR = Path("models")
MODEL_PATH = MODEL_DIR / "rf_model.pkl" # Naming it pkl for compatibility
TARGET_COLS = [
=======
DATA_PATH = Path("data/main_dataset.csv") # Adjust path as needed
MODEL_DIR = Path("models")
MODEL_PATH = MODEL_DIR / "rf_model.json"
TARGET_COLS = [
>>>>>>> REPLACE
```
```
<<<<<<< SEARCH
    # Save
    joblib.dump(clf, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")
=======
    # Save securely
    clf.save_model(str(MODEL_PATH))
    print(f"Model saved to {MODEL_PATH}")
>>>>>>> REPLACE
```

2. **Verify main_runtime.py updates.**
   - Run `cat main_runtime.py` to confirm the `JSONScaler` class was successfully and correctly written.

3. **Implement Migration Script.**
   - Run a bash command with exactly this `EOF` block to create `migrate_models.py`:
```bash
cat << 'EOF' > migrate_models.py
import json
import joblib
import numpy as np
import xgboost as xgb
from pathlib import Path

def convert_scaler(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    scaler = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump({
            'mean_': scaler.mean_.tolist(),
            'scale_': scaler.scale_.tolist()
        }, f)
    print(f"Converted {pkl_path} to {json_path}")

def convert_features(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    features = joblib.load(pkl_path)
    with open(json_path, 'w') as f:
        json.dump(list(features), f)
    print(f"Converted {pkl_path} to {json_path}")

def convert_model(pkl_path, json_path):
    if not Path(pkl_path).exists(): return
    try:
        model = joblib.load(pkl_path)
        if hasattr(model, 'save_model'):
            model.save_model(str(json_path))
            print(f"Converted {pkl_path} to {json_path}")
        else:
            print(f"Warning: {pkl_path} is not an XGBoost model, skipping save_model.")
    except Exception as e:
        print(f"Failed to convert model {pkl_path}: {e}")

if __name__ == "__main__":
    base_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if base_dir.exists():
        convert_scaler(base_dir / "scaler.pkl", base_dir / "scaler.json")
        convert_features(base_dir / "selected_features.pkl", base_dir / "selected_features.json")
        convert_model(base_dir / "rf_model.pkl", base_dir / "rf_model.json")

    # Check current directory just in case
    convert_model("models/rf_model.pkl", "models/rf_model.json")
    print("Migration complete.")
