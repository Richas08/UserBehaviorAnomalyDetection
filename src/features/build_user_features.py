import pandas as pd

# Load dataset
logon = pd.read_csv("datasets/raw/logon.csv")

# Convert date
logon['date'] = pd.to_datetime(logon['date'])

# Keep only Logon activity
logon_only = logon[
    logon['activity'] == 'Logon'
]

# -----------------------
# Login Count
# -----------------------

login_count = (
    logon_only
    .groupby('user')
    .size()
    .reset_index(name='login_count')
)

# -----------------------
# Night Login Count
# -----------------------

logon_only['hour'] = (
    logon_only['date']
    .dt.hour
)

night_logins = logon_only[
    (logon_only['hour'] < 6) |
    (logon_only['hour'] >= 22)
]

night_login_count = (
    night_logins
    .groupby('user')
    .size()
    .reset_index(name='night_login_count')
)

# -----------------------
# Weekend Login Count
# -----------------------

logon_only['weekday'] = (
    logon_only['date']
    .dt.dayofweek
)

weekend_logins = logon_only[
    logon_only['weekday'] >= 5
]

weekend_login_count = (
    weekend_logins
    .groupby('user')
    .size()
    .reset_index(name='weekend_login_count')
)

# -----------------------
# Merge Features
# -----------------------

features = login_count.merge(
    night_login_count,
    on='user',
    how='left'
)

features = features.merge(
    weekend_login_count,
    on='user',
    how='left'
)

# Replace NaN with 0
features.fillna(0, inplace=True)

print(features.head())
print(features.shape)

features.to_csv(
    "datasets/processed/user_features.csv",
    index=False
)