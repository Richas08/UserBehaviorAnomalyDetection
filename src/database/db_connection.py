# Import MySQL library
import mysql.connector

# Create connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="richa123",
    database="anomaly_db"
)

# Check connection
if connection.is_connected():
    print("Database Connected Successfully!")

# Close connection
connection.close()