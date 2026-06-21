import pandas as pd
import numpy as np
import xgboost as xgb
from pathlib import Path
from sklearn.model_selection import train_test_split
import json
from sklearn.metrics import accuracy_score, classification_report

# Config
DATA_PATH = Path("data/main_dataset.csv") # Adjust path as needed
MODEL_DIR = Path("models")
MODEL_PATH = MODEL_DIR / "rf_model.json"
SCALER_PATH = MODEL_DIR / "scaler.json"
FEATURES_PATH = MODEL_DIR / "selected_features.json"
TARGET_COLS = [
    'tip2dip', 'tip2pip', 'tip2mcp', 'tip2wrist',
    'disp', 'velocity_size', 'velocity_disp', 'acceleration_disp',
    'distance_cm'
]

def load_and_clean_data():
    print("Loading dataset...")
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Dataset not found at {DATA_PATH}")

    df = pd.read_csv(DATA_PATH)

    # Filter to ensure we rely on the strict features
    # Note: If 'velocity_disp' etc aren't in CSV, we must generate them here
    # mirroring extractor.py logic. Assuming they exist based on prompt context.

    # --- SYNTHESIS LOGIC START ---
    # Ensure temporal features exist if they are missing
    if 'velocity_disp' not in df.columns:
        print("Synthesizing temporal features...")
        # Assuming 'disp' exists or needs calculation.
        # If 'disp' is missing, calculate it from tip coordinates between rows.
        # This requires the CSV to be time-ordered per recording session.

        # Simple rolling mean for smoothing (Window=10 matches extractor buffer)
        df['velocity_disp'] = df['disp'].rolling(window=10, min_periods=1).mean()

        # Acceleration: Difference of 'disp' (matches extractor logic)
        df['acceleration_disp'] = df['disp'].diff().fillna(0)

        # Velocity Size: Smoothed change in tip2wrist
        # Calculate raw change first if needed
        if 'velocity_size' not in df.columns:
             # Assuming tip2wrist exists
             df['size_change'] = df['tip2wrist'].diff().abs().fillna(0)
             df['velocity_size'] = df['size_change'].rolling(window=10, min_periods=1).mean()
    # --- SYNTHESIS LOGIC END ---

    # Check for missing columns
    missing = [c for c in TARGET_COLS if c not in df.columns]
    if missing:
        print(f"Warning: Missing columns {missing}. Regenerating might be needed.")
        # Logic to regenerate features from raw landmarks would go here if needed

    # Clean NaNs
    df = df.dropna(subset=TARGET_COLS)

    # Filter logic (e.g., take last 50k or random sample)
    if len(df) > 50000:
        print("Filtering to 50k samples...")
        df = df.sample(n=50000, random_state=42)

    # Map string labels to binary if needed
    # Assuming 'is_hovering' is the truth or 'action'
    # We train a binary classifier: 0=Hover, 1=Press
    # The State Machine handles Hold/Release based on transitions.
    if 'is_hovering' in df.columns:
        y = (~df['is_hovering']).astype(int) # Invert: Hover=True -> 0, Press=False -> 1 ?
        # Wait, usually Press=1. If is_hovering=True, class is 0.
    else:
        raise ValueError("Target column 'is_hovering' not found.")

    X = df[TARGET_COLS]
    return X, y

def train():
    MODEL_DIR.mkdir(exist_ok=True)

    X, y = load_and_clean_data()

    print(f"Training on {len(X)} samples with {len(TARGET_COLS)} features.")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # XGBoost Classifier with GPU support
    # Note: 'gpu_hist' requires GPU. If not available, fallback to 'hist' or 'auto'.
    try:
        clf = xgb.XGBClassifier(
            tree_method='gpu_hist',
            predictor='gpu_predictor',
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1
        )
        clf.fit(X_train, y_train)
    except xgb.core.XGBoostError:
        print("GPU not available or not configured. Falling back to CPU training.")
        clf = xgb.XGBClassifier(
            tree_method='hist',
            n_estimators=100,
            max_depth=6,
            learning_rate=0.1
        )
        clf.fit(X_train, y_train)

    # Evaluate
    preds = clf.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Model Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))

    # Save Model
    clf.save_model(str(MODEL_PATH))
    print(f"Model saved to {MODEL_PATH}")

    # Note: If a scaler is used during training, it should be saved securely here.
    # We will simulate a dummy save for completeness since original didn't use one,
    # but runtime expects it.
    with open(SCALER_PATH, 'w') as f:
        # Dummy scale and mean vectors if not standardizing in script
        json.dump({'mean_': [0.0]*len(TARGET_COLS), 'scale_': [1.0]*len(TARGET_COLS)}, f)

    with open(FEATURES_PATH, 'w') as f:
        json.dump(TARGET_COLS, f)

if __name__ == "__main__":
    train()
