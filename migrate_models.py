import joblib, json
from pathlib import Path

def migrate():
    for f in Path(".").rglob("*.pkl"):
        try:
            obj = joblib.load(f)
            out = f.with_suffix(".json")
            if "scaler" in f.name:
                with open(out, "w") as jf:
                    json.dump({"mean": obj.mean_.tolist(), "scale": obj.scale_.tolist()}, jf)
            elif "features" in f.name:
                with open(out, "w") as jf:
                    json.dump(obj, jf)
            elif hasattr(obj, "save_model"):
                obj.save_model(str(out))
            else:
                print(f"Custom JSON migration required for {f.name}")
        except Exception as e:
            print(f"Error migrating {f.name}: {e}")

if __name__ == "__main__": migrate()