# Select From a Table, 
# To select from a table in MySQL, use the "SELECT" statement

import mysql.connector

my_data = mysql.connector.connect (
    host = "localhost",
    user = "ypourusername",
    password = "yourpassword",
    database = "mydatabase"
)

mycursor = my_data.cursor ()

mycursor.execute ("SELECT * FROM customers")

myresult = mycursor.fetchall ()

for x in myresult:
    print (x)
    
# Note: We use the fetchall() method, which fetches all rows from the last executed statement.

# Selecting Columns
# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):

mycursor = my_data.cursor ()

mycursor.execute ("SELECT name, addres FROM customers")

myresult = mycursor.fetchall ()

for x in myresult:
    print (x)

# Using the fetchone() Method
# If you are only interested in one row, you can use the fetchone() method.
# The fetchone() method will return the first row of the result:

mycursor = my_data.cursor ()

mycursor.execute ("SELECT * FROM customers")

myresult = mycursor.fetchone ()

print (myresult)

