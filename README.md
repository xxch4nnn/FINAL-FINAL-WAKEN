# PianoMotion: Hand Tracking & Classification

A robust computer vision pipeline for classifying piano hand gestures (Hover, Press, Hold, Release) using MediaPipe and XGBoost.

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2.  **Train the Model** (Requires NVIDIA GPU):

    ```bash
    python src/training/train_gpu.py
    ```

    This will generate `models/rf_model.pkl`.

3.  **Run Live Engine**:

    ```bash
    python src/runtime/vision_engine.py
    ```

## Architecture

  - **`src/features/extractor.py`**: The shared "Source of Truth". Converts raw MediaPipe landmarks into the 9-dimensional feature vector used by the model. Ensures parity between training data and live inference.
  - **`src/runtime/`**: Contains the `VisionEngine` which runs the camera loop and the `PianoStateMachine` which translates binary model predictions into temporal states (e.g., Press -\> Hold).
  - **`src/training/`**: GPU-accelerated training script using XGBoost.

## Feature Logic

Distances are calculated in pixel space (1280x720 reference) to match training data distributions.
