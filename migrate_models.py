import joblib
import json
import xgboost as xgb
from pathlib import Path

def migrate_artifacts(models_dir="models"):
    print(f"Starting migration of ML artifacts in {models_dir}...")
    models_path = Path(models_dir)

    if not models_path.exists():
        print(f"Directory {models_dir} not found. Skipping migration.")
        return

    # Migrate Model
    pkl_model_path = models_path / "rf_model.pkl"
    json_model_path = models_path / "rf_model.json"

    if pkl_model_path.exists():
        try:
            print(f"Found {pkl_model_path}, migrating to {json_model_path}...")
            # Load legacy model
            model = joblib.load(pkl_model_path)

            # Save using native XGBoost format
            if hasattr(model, 'save_model'):
                model.save_model(str(json_model_path))
                print(f"Successfully migrated model to {json_model_path}")
            else:
                print("Error: Model does not have a save_model method (may not be XGBoost).")
        except Exception as e:
            print(f"Failed to migrate model: {e}")

    # Migrate Scaler
    pkl_scaler_path = models_path / "scaler.pkl"
    json_scaler_path = models_path / "scaler.json"

    if pkl_scaler_path.exists():
        try:
            print(f"Found {pkl_scaler_path}, migrating to {json_scaler_path}...")
            scaler = joblib.load(pkl_scaler_path)

            # Extract relevant attributes (assuming StandardScaler or similar)
            # Make sure we don't save out an empty dummy scaler if mean_ and scale_ are missing
            scaler_data = {}
            if hasattr(scaler, 'mean_') and scaler.mean_ is not None:
                scaler_data['mean'] = scaler.mean_.tolist()
            if hasattr(scaler, 'scale_') and scaler.scale_ is not None:
                scaler_data['scale'] = scaler.scale_.tolist()

            if scaler_data:
                with open(json_scaler_path, 'w') as f:
                    json.dump(scaler_data, f)
                print(f"Successfully migrated scaler to {json_scaler_path}")
            else:
                print("Error: Could not extract mean_ or scale_ from scaler.")
        except Exception as e:
            print(f"Failed to migrate scaler: {e}")

    # Migrate Features
    pkl_features_path = models_path / "selected_features.pkl"
    json_features_path = models_path / "selected_features.json"

    if pkl_features_path.exists():
        try:
            print(f"Found {pkl_features_path}, migrating to {json_features_path}...")
            features = joblib.load(pkl_features_path)

            # Assuming features is a list
            if isinstance(features, list) or isinstance(features, (tuple, set)):
                with open(json_features_path, 'w') as f:
                    json.dump(list(features), f)
                print(f"Successfully migrated features to {json_features_path}")
            else:
                # If it's a numpy array, convert to list
                if hasattr(features, 'tolist'):
                    with open(json_features_path, 'w') as f:
                        json.dump(features.tolist(), f)
                    print(f"Successfully migrated features to {json_features_path}")
                else:
                    print("Error: Features object is not a list or convertible to list.")
        except Exception as e:
            print(f"Failed to migrate features: {e}")

if __name__ == "__main__":
    # Also check the models directory inside the larger course if it exists
    migrate_artifacts("models")
    migrate_artifacts("Machine_Learning_Course/Data/PianoMotion10M/models")
