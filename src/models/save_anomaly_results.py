# ==================================================
# save_anomaly_results.py
# Purpose:
# 1. Read user features from MySQL
# 2. Load trained Isolation Forest model
# 3. Load Robust Scaler
# 4. Generate anomaly scores
# 5. Generate anomaly labels
# 6. Save results into anomaly_results table
# ==================================================

import joblib
import pandas as pd
import mysql.connector

# --------------------------------------------------
# STEP 1: Connect to MySQL
# --------------------------------------------------

print("Connecting to MySQL...")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="richa123",
    database="anomaly_db"
)

# --------------------------------------------------
# STEP 2: Read user_features table
# --------------------------------------------------

query = "SELECT * FROM user_features"

df = pd.read_sql(query, connection)

print(f"Retrieved {len(df)} users from database.")

# --------------------------------------------------
# STEP 3: Load saved scaler
# --------------------------------------------------

print("Loading Robust Scaler...")

scaler = joblib.load("models_saved/robust_scaler.pkl")

# --------------------------------------------------
# STEP 4: Load trained model
# --------------------------------------------------

print("Loading Isolation Forest model...")

model = joblib.load(
    "models_saved/isolation_forest_model.pkl"
)

# --------------------------------------------------
# STEP 5: Prepare feature columns
# --------------------------------------------------

# Remove columns that should not be used
exclude_cols = ["id", "user_id", "timestamp"]

feature_cols = [
    col for col in df.columns
    if col not in exclude_cols
]

X = df[feature_cols]

# --------------------------------------------------
# STEP 6: Scale features
# --------------------------------------------------

X_scaled = scaler.transform(X)

# --------------------------------------------------
# STEP 7: Generate anomaly scores
# --------------------------------------------------

raw_scores = model.score_samples(X_scaled)

df["anomaly_score"] = (
    1.0
    - (
        raw_scores - raw_scores.min()
    )
    / (
        raw_scores.max()
        - raw_scores.min()
        + 1e-6
    )
)

# --------------------------------------------------
# STEP 8: Generate anomaly labels
# --------------------------------------------------

df["anomaly_label"] = model.predict(X_scaled)

print("\nAnomaly Distribution:")

print(df["anomaly_label"].value_counts())

# --------------------------------------------------
# STEP 9: Save results into anomaly_results
# --------------------------------------------------

print("\nSaving results into anomaly_results table...")

cursor = connection.cursor()

# Delete old records first
cursor.execute("DELETE FROM anomaly_results")

insert_query = """
INSERT INTO anomaly_results
(
    user_id,
    model_name,
    anomaly_score,
    anomaly_label
)
VALUES (%s, %s, %s, %s)
"""

# Insert one row at a time
for _, row in df.iterrows():

    values = (
        row["user_id"],
        "Isolation Forest",
        round(float(row["anomaly_score"]), 4),
        int(row["anomaly_label"])
    )

    cursor.execute(insert_query, values)

connection.commit()

# --------------------------------------------------
# STEP 10: Verify inserted records
# --------------------------------------------------

cursor.execute(
    "SELECT COUNT(*) FROM anomaly_results"
)

count = cursor.fetchone()[0]

print(f"\nTotal rows saved: {count}")

# --------------------------------------------------
# STEP 11: Close connection
# --------------------------------------------------

cursor.close()
connection.close()

print("\nAnomaly results saved successfully.")