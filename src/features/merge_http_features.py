import pandas as pd

master = pd.read_csv(
    "datasets/processed/final_features.csv"
)

http_features = pd.read_csv(
    "datasets/processed/http_features.csv"
)

master = master.merge(
    http_features,
    on='user',
    how='left'
)

master.fillna(0, inplace=True)

print(master.head())

print("\nShape:")
print(master.shape)

master.to_csv(
    "datasets/processed/final_features.csv",
    index=False
)


df = pd.read_csv("datasets/processed/final_features.csv")

print(df.columns.tolist())