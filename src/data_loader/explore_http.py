import pandas as pd

http_df = pd.read_csv(
    "datasets/raw/http.csv",
    nrows=5
)

print(http_df.head())

print("\nColumns:")
print(http_df.columns.tolist())

print("\nShape:")
print(http_df.shape)