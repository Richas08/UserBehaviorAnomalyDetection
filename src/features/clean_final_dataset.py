# my dataset contains duplicate columns, which means some merge scripts were executed 
# multiple times. like merge_email_features.py or merge_http_features.py file was run 
# multiple times on the same final_features.csv. so I have to cleanup the data

import pandas as pd

df = pd.read_csv(
    "datasets/processed/final_features.csv"
)

# Columns to keep
keep_columns = [
    'user',

    'login_count',
    'night_login_count',
    'weekend_login_count',

    'usb_connect_count',
    'usb_disconnect_count',
    'usb_usage_count',

    'email_count',
    'attachment_count',
    'email_size_total',
    'avg_email_size',

    'file_access_count',
    'unique_file_count',
    'pdf_count',
    'doc_count',
    'image_count',

    'website_visit_count',
    'unique_website_count',
    'after_hours_web_activity'
]

df = df[keep_columns]

print(df.head())
print("\nShape:", df.shape)

df.to_csv(
    "datasets/processed/final_features_clean.csv",
    index=False
)