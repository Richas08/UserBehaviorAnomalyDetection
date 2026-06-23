# ==================================================
# load_features_to_mysql.py
# Purpose:
# Read final_features_clean.csv
# Insert data into MySQL user_features table
# ==================================================

import pandas as pd
import mysql.connector

# --------------------------------------------------
# STEP 1: Read CSV file
# --------------------------------------------------

df = pd.read_csv(
    "datasets/processed/final_features_clean.csv"
)

print("CSV Loaded Successfully")
print(df.head())

# --------------------------------------------------
# STEP 2: Rename column
# CSV has 'user'
# Database has 'user_id'
# --------------------------------------------------

df.rename(
    columns={"user": "user_id"},
    inplace=True
)

# --------------------------------------------------
# STEP 3: Connect to MySQL
# --------------------------------------------------

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="richa123",
    database="anomaly_db"
)

cursor = connection.cursor()

print("Connected to MySQL")

# --------------------------------------------------
# STEP 4: Insert each row into table
# --------------------------------------------------

query = """
INSERT INTO user_features
(
user_id,
login_count,
night_login_count,
weekend_login_count,
usb_connect_count,
usb_disconnect_count,
usb_usage_count,
email_count,
attachment_count,
email_size_total,
avg_email_size,
file_access_count,
unique_file_count,
pdf_count,
doc_count,
image_count,
website_visit_count,
unique_website_count,
after_hours_web_activity
)
VALUES
(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
 %s,%s,%s,%s,%s,%s,%s,%s,%s)
"""

for index, row in df.iterrows():

    values = (
        row["user_id"],
        row["login_count"],
        row["night_login_count"],
        row["weekend_login_count"],
        row["usb_connect_count"],
        row["usb_disconnect_count"],
        row["usb_usage_count"],
        row["email_count"],
        row["attachment_count"],
        row["email_size_total"],
        row["avg_email_size"],
        row["file_access_count"],
        row["unique_file_count"],
        row["pdf_count"],
        row["doc_count"],
        row["image_count"],
        row["website_visit_count"],
        row["unique_website_count"],
        row["after_hours_web_activity"]
    )

    cursor.execute(query, values)

# --------------------------------------------------
# STEP 5: Save changes
# --------------------------------------------------

connection.commit()

print("Data Inserted Successfully")

# --------------------------------------------------
# STEP 6: Close connection
# --------------------------------------------------

cursor.close()
connection.close()

print("MySQL Connection Closed")