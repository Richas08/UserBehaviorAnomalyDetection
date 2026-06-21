import pandas as pd

user_features = pd.read_csv(
    "datasets/processed/user_features.csv"
)

usb_features = pd.read_csv(
    "datasets/processed/usb_features.csv"
)

final_features = user_features.merge(
    usb_features,
    on='user',
    how='left'
)

final_features.fillna(0, inplace=True)

print(final_features.head())

print("\nShape:")
print(final_features.shape)

final_features.to_csv(
    "datasets/processed/final_features.csv",
    index=False
)

print(final_features.describe())

print(
    final_features['usb_usage_count']
    .value_counts()
    .head(20)
)
