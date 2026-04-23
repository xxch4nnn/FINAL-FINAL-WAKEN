import joblib
import xgboost as xgb
import json
from pathlib import Path

models_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
if not models_dir.exists():
    models_dir.mkdir(parents=True)

pkl_model_path = models_dir / "rf_model.pkl"
json_model_path = models_dir / "rf_model.json"

if pkl_model_path.exists():
    model = joblib.load(pkl_model_path)
    model.save_model(json_model_path)
    print("Migrated rf_model.pkl to rf_model.json")
else:
    print(f"No existing .pkl model found at {pkl_model_path}")

# Create dummy scaler/features to prevent pipeline breakage
TARGET_COLS = [
    'tip2dip', 'tip2pip', 'tip2mcp', 'tip2wrist',
    'disp', 'velocity_size', 'velocity_disp', 'acceleration_disp',
    'distance_cm'
]
scaler_data = {"mean_": [0.0]*len(TARGET_COLS), "scale_": [1.0]*len(TARGET_COLS)}
with open(models_dir / "scaler.json", "w") as f:
    json.dump(scaler_data, f)
with open(models_dir / "selected_features.json", "w") as f:
    json.dump(TARGET_COLS, f)
print("Created identity scaler and feature list in JSON")
