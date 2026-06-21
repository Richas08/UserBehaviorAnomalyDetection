import pandas as pd

email = pd.read_csv(
    "datasets/raw/email.csv",
    nrows=5
)

print(email.head())

print("\nColumns:")
print(email.columns)

print("\nShape:")
print(email.shape)

print("\nMissing Values:")
print(email.isnull().sum())