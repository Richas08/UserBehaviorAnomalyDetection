import pandas as pd

# Load data
logon = pd.read_csv(
    "datasets/raw/logon.csv"
)

# Convert date column
logon['date'] = pd.to_datetime(
    logon['date']
)

# Keep only Logon events
logon_only = logon[
    logon['activity'] == 'Logon'
]

# Extract weekday
logon_only['weekday'] = (
    logon_only['date']
    .dt.dayofweek
)

# Saturday=5 Sunday=6
weekend_logins = logon_only[
    logon_only['weekday'] >= 5
]

# Count per user
weekend_login_count = (
    weekend_logins
    .groupby('user')
    .size()
    .reset_index(
        name='weekend_login_count'
    )
)

print(weekend_login_count.head())

print("\nTotal Weekend Logins:")
print(len(weekend_logins))

weekend_login_count.to_csv(
    "datasets/processed/weekend_login_count.csv",
    index=False
)