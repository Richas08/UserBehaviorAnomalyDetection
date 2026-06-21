import pandas as pd

logon = pd.read_csv("datasets/raw/logon.csv" )

print("Columns:")
print(logon.columns)

print("\nShape:") #How many records exist
print(logon.shape)

print("\nMissing Values:")
print(logon.isnull().sum())

print("\nUnique Users:") #It will find how many use exists
print(logon['user'].nunique())

print("\nActivities:") #How many Logons vs Logoffs?
print(logon['activity'].value_counts())