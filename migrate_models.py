import joblib
import xgboost as xgb
import os
import json

def migrate_rf():
    if os.path.exists('models/rf_model.pkl'):
        model = joblib.load('models/rf_model.pkl')
        model.save_model('models/rf_model.json')
        print("Migrated rf_model.pkl to rf_model.json")
    else:
        print("models/rf_model.pkl not found")

migrate_rf()
