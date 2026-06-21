import pandas as pd

logon = pd.read_csv("datasets/raw/logon.csv")

login_count = (
    logon[logon['activity'] == 'Logon']
    .groupby('user')
    .size()
    .reset_index(name='login_count')
)

print(login_count.head())

login_count.to_csv("datasets/processed/login_count.csv",
    index=False
)