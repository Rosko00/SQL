# To create a database in MySQL
# CREATE DATABASE

import mysql.connector

my_data = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    password= "yourpassword"
)
mycursor = my_data.cursor ()
mycursor.execute ("CREATE DATABASE my_data")
# If the code executed without errors, you have successfully created the database.

# Check database ("SHOW DATABASES") - list all datavases

mycursor.execute ("SHOW DATABASES")

for x in mycursor:
    print (x)
    
# Or you can try to access the database when making the connection:
# Try connecting to the database "my_data"

my_data = mysql.connector.connect (
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database = "my_data"    
)

# If the database does not exist, you will get an error.
