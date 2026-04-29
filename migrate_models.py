import joblib
import json
import os
from pathlib import Path

def migrate():
    print("Starting secure model migration...")

    # Define paths
    models_dir = Path("Machine_Learning_Course/Data/PianoMotion10M/models")
    if not models_dir.exists():
        models_dir = Path("models") # fallback

    old_model_path = models_dir / "rf_model.pkl"
    new_model_path = models_dir / "rf_model.json"

    old_scaler_path = models_dir / "scaler.pkl"
    new_scaler_path = models_dir / "scaler.json"

    old_features_path = models_dir / "selected_features.pkl"
    new_features_path = models_dir / "selected_features.json"

    # Migrate Model
    if old_model_path.exists():
        try:
            print(f"Loading legacy model: {old_model_path}")
            clf = joblib.load(old_model_path)
            clf.save_model(new_model_path)
            print(f"✅ Successfully migrated model to {new_model_path}")
        except Exception as e:
            print(f"❌ Failed to migrate model: {e}")

    # Migrate Scaler
    if old_scaler_path.exists():
        try:
            print(f"Loading legacy scaler: {old_scaler_path}")
            scaler = joblib.load(old_scaler_path)
            # Assuming it's a StandardScaler with mean_ and scale_
            scaler_data = {
                "means": scaler.mean_.tolist() if hasattr(scaler, 'mean_') else [0.0] * 9,
                "scales": scaler.scale_.tolist() if hasattr(scaler, 'scale_') else [1.0] * 9
            }
            with open(new_scaler_path, 'w') as f:
                json.dump(scaler_data, f)
            print(f"✅ Successfully migrated scaler to {new_scaler_path}")
        except Exception as e:
            print(f"❌ Failed to migrate scaler: {e}")

    # Migrate Features
    if old_features_path.exists():
        try:
            print(f"Loading legacy features: {old_features_path}")
            features = joblib.load(old_features_path)
            with open(new_features_path, 'w') as f:
                json.dump(features, f)
            print(f"✅ Successfully migrated features to {new_features_path}")
        except Exception as e:
            print(f"❌ Failed to migrate features: {e}")

    print("Migration complete. You can now safely delete the .pkl files.")

if __name__ == "__main__":
    migrate()
