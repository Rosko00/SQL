# Update Table
# You can update existing records in a table by using the "UPDATE" statement
# Overwrite the address column from "Dlhe Luky 6004" to "Okruzna 1426":

import mysql.connector

my_data = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = my_data.cursor()

sq12 = "UPDATE customers SET address = 'Okruzna 1426' WHERE address = 'Dlhe Luky 6004'"

mycursor.execute(sq12)

my_data.commit()

print(mycursor.rowcount, "record(s) affected")
