import pandas as pd

logon = pd.read_csv(
    "datasets/raw/logon.csv",
    nrows=5
)

print(logon)