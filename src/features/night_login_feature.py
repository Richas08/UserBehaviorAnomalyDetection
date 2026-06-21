import pandas as pd

# Load data
logon = pd.read_csv(
    "datasets/raw/logon.csv"
)

# Convert date column to datetime
logon['date'] = pd.to_datetime(
    logon['date']
)

# Extract hour
logon['hour'] = logon['date'].dt.hour

# Keep only Logon events
logon_only = logon[
    logon['activity'] == 'Logon'
]

# Night login condition
night_logins = logon_only[
    (logon_only['hour'] < 6) |
    (logon_only['hour'] >= 22)
]

# Count per user
night_login_count = (
    night_logins
    .groupby('user')
    .size()
    .reset_index(
        name='night_login_count'
    )
)

print(night_login_count.head())

print("\nTotal Night Logins:")
print(len(night_logins))

night_login_count.to_csv("datasets/processed/night_login_count.csv",
    index=False
)
print(logon['date'].head())