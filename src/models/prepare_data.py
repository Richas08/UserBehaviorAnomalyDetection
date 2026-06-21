import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib

# Load dataset
df = pd.read_csv(
    "datasets/processed/final_features_clean.csv"
)

# Save user ids
users = df['user']

# Remove user column
X = df.drop(columns=['user'])

# Fill missing values
X.fillna(0, inplace=True)

# Scale data
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# Save scaler
joblib.dump(
    scaler,
    "models_saved/scaler.pkl"
)

# Save scaled dataset
scaled_df = pd.DataFrame(
    X_scaled,
    columns=X.columns
)

scaled_df.to_csv(
    "datasets/processed/X_scaled.csv",
    index=False
)

print("Original Shape:", X.shape)
print("Scaled Shape:", X_scaled.shape)