# Python MySQL Drop Table / (Delete the table "customers")

import mysql.connector

my_data = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = my_data.cursor()

sq10 = "DROP TABLE customers"

mycursor.execute(sq10)

# Drop Only if Exist
# If the table you want to delete is already deleted, or for any other reason does not exist, 
# you can use the IF EXISTS keyword to avoid getting an error.

mycursor = my_data.cursor()

sq11 = "DROP TABLE IF EXISTS customers"

mycursor.execute(sq11)
