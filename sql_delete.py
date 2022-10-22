# Delete Record
# You can delete records from an existing table by using the "DELETE FROM" statement
# Delete any record where the address is "Dlhe Luky 6004":

import mysql.connector

my_data = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = my_data.cursor()

sq8 = "DELETE FROM customers WHERE address = 'Dlhe Luky 6004'"

mycursor.execute(sq8)

my_data.commit()

print(mycursor.rowcount, "record(s) deleted")

# Prevent SQL Injection
# The mysql.connector module uses the placeholder %s to escape values in the delete statement

mycursor = my_data.cursor()

sq9 = "DELETE FROM customers WHERE address = %s"
ad9 = ("Dlhe Luky 6004", )

mycursor.execute(sq9, ad9)

my_data.commit()

print(mycursor.rowcount, "record(s) deleted")

