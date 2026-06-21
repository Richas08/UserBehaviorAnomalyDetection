import pandas as pd

# Load HTTP data
http_df = pd.read_csv(
    "datasets/raw/http.csv"
)

# Convert date
http_df['date'] = pd.to_datetime(
    http_df['date']
)

# Website Visit Count
website_visit_count = (
    http_df.groupby('user')
    .size()
    .reset_index(
        name='website_visit_count'
    )
)

# Unique Website Count
unique_website_count = (
    http_df.groupby('user')['url']
    .nunique()
    .reset_index(
        name='unique_website_count'
    )
)

# Extract Hour
http_df['hour'] = (
    http_df['date']
    .dt.hour
)

# After Hours Browsing
after_hours = http_df[
    (http_df['hour'] < 6) |
    (http_df['hour'] >= 22)
]

after_hours_web_activity = (
    after_hours.groupby('user')
    .size()
    .reset_index(
        name='after_hours_web_activity'
    )
)

# Merge Features
http_features = website_visit_count.merge(
    unique_website_count,
    on='user',
    how='left'
)

http_features = http_features.merge(
    after_hours_web_activity,
    on='user',
    how='left'
)

http_features.fillna(0, inplace=True)

print(http_features.head())

print("\nShape:")
print(http_features.shape)

http_features.to_csv(
    "datasets/processed/http_features.csv",
    index=False
)