import pandas as pd

file_df = pd.read_csv(
    "datasets/raw/file.csv",
    nrows=5
)

print(file_df.head())

print("\nColumns:")
print(file_df.columns.tolist())

print("\nShape:")
print(file_df.shape)