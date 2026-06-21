import pandas as pd

email = pd.read_csv(
    "datasets/raw/email.csv"
)

# Total Emails Per User
email_count = (
    email.groupby('user')
    .size()
    .reset_index(name='email_count')
)

# Total Attachments
attachment_count = (
    email.groupby('user')['attachments']
    .sum()
    .reset_index(name='attachment_count')
)

# Total Email Size
email_size_total = (
    email.groupby('user')['size']
    .sum()
    .reset_index(name='email_size_total')
)

# Average Email Size
avg_email_size = (
    email.groupby('user')['size']
    .mean()
    .reset_index(name='avg_email_size')
)

# Merge Features
email_features = email_count.merge(
    attachment_count,
    on='user'
)

email_features = email_features.merge(
    email_size_total,
    on='user'
)

email_features = email_features.merge(
    avg_email_size,
    on='user'
)

print(email_features.head())

print("\nShape:")
print(email_features.shape)

email_features.to_csv(
    "datasets/processed/email_features.csv",
    index=False
)