import pandas as pd

master = pd.read_csv(
    "datasets/processed/final_features.csv"
)

file_features = pd.read_csv(
    "datasets/processed/file_features.csv"
)

master = master.merge(
    file_features,
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