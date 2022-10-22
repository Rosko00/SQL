# Sort the Result
# Use the ORDER BY statement to sort the result in ascending or descending order.

import mysql.connector

my_data = mysql.connector.connect (
    host = "localhost",
    user = "yourusername",
    password = "yourpassword",
    database = "yourdatabase"
)

mycursor = my_data.cursor ()

sq6 = "SELECT + FROM customers ORDER BY name"

mycursor.execute (sq6)

myresult = mycursor.fetchall ()

for x in myresult:
    print (x)

# ORDER BY DESC
# Use the DESC keyword to sort the result in a descending order.

mycursor = my_data.cursor()

sq7 = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sq7)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
