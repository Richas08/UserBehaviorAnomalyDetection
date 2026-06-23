# ==================================================
# train_anomaly_detector.py
# Purpose: Fetch user features from MySQL, train an 
#          Isolation Forest model, and save the artifact.
# ==================================================

import os
import joblib
import pandas as pd
import mysql.connector
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler

# --------------------------------------------------
# STEP 1: Fetch Features from MySQL Database
# --------------------------------------------------
print("Fetching feature vectors from MySQL...")
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="richa123",
        database="anomaly_db"
    )
    
    # Query all numerical behavioral counts
    query = "SELECT * FROM user_features"
    df = pd.read_sql(query, connection)
    print(f"Successfully retrieved {len(df)} user behavior records.")

except mysql.connector.Error as e:
    print(f"Database error: {e}")
    exit()
finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()

# --------------------------------------------------
# STEP 2: Separate Identifiers from Features
# --------------------------------------------------
# Exclude metadata columns that aren't analytical features
exclude_cols = ["id", "user_id", "timestamp"] 
feature_cols = [col for col in df.columns if col not in exclude_cols]

X = df[feature_cols]

# --------------------------------------------------
# STEP 3: Feature Scaling (Robust against heavy outliers)
# --------------------------------------------------
print("Standardizing feature dimensions...")
scaler = RobustScaler()
X_scaled = scaler.fit_transform(X)

# --------------------------------------------------
# STEP 4: Train Unsupervised Isolation Forest
# --------------------------------------------------
print("Initializing and fitting Isolation Forest model...")
# contamination=0.02 assumes roughly 2% of our dataset might contain anomalous activity
model = IsolationForest(contamination=0.02, random_state=42, n_estimators=100)
model.fit(X_scaled)
print("Model training completed successfully.")

# --------------------------------------------------
# STEP 5: Generate Raw Anomaly Scores
# --------------------------------------------------
# score_samples returns negative values (lower = more anomalous)
# We invert it so higher score = higher anomaly probability
raw_scores = model.score_samples(X_scaled)
df['ml_anomaly_score'] = 1.0 - (raw_scores - raw_scores.min()) / (raw_scores.max() - raw_scores.min() + 1e-6)

print("\nSample of computed ML Anomaly Scores:")
print(df[['user_id', 'ml_anomaly_score']].head())

# --------------------------------------------------
# STEP 6: Serialize and Save Model & Scaler Artifacts
# --------------------------------------------------
# Create folder structure dynamically if it doesn't exist
os.makedirs("models_saved", exist_ok=True)

joblib.dump(model, "models_saved/isolation_forest_model.pkl")
joblib.dump(scaler, "models_saved/robust_scaler.pkl")
print("\nArtifacts saved successfully in 'models_saved/' directory.")