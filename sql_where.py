# Select With a Filter
# When selecting records from a table, you can filter the selection by using the "WHERE" statement

import mysql.connector

my_data = mysql.connector.connect(
    host="localhost",
    user="ypourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = my_data.cursor()

sq4 = "SELECT * FROM customers WHERE address = 'Park Lane 10'"

mycursor.execute (sq4)

myresult = mycursor.fetchall ()

for x in myresult:
    print (x)

# You can also select the records that starts, includes, or ends with a given letter or phrase
# Use the %  to represent wildcard characters

mycursor = my_data.cursor()

sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Prevent SQL Injection
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# Escape query values by using the placholder %s method

mycursor = my_data.cursor()

sq5 = "SELECT * FROM customers WHERE address = %s"
ad5 = ("Yellow Garden 2", )

mycursor.execute(sq5, ad5)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

