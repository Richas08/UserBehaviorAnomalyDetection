import pandas as pd

master = pd.read_csv(
    "datasets/processed/final_features.csv"
)

email_features = pd.read_csv(
    "datasets/processed/email_features.csv"
)

master = master.merge(
    email_features,
    on='user',
    how='left'
)

master.fillna(0, inplace=True)

print(master.head())

print(master.shape)

master.to_csv(
    "datasets/processed/final_features.csv",
    index=False
)