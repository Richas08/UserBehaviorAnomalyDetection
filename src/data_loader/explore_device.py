import pandas as pd

device = pd.read_csv(
    "datasets/raw/device.csv",
    nrows=10
)

print(device.head())

print("\nColumns:")
print(device.columns)

print("\nShape:")
print(device.shape)

print("\nMissing Values:")
print(device.isnull().sum())