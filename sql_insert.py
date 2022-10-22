# Insert Into Table / ("INSERT INTO")

import mysql.connector

my_data = mysql.connector.connect (
    host = "localhost",
    user = "yourusername",
    password = "yourpassword",
    database = "mydatabase"
)

mycursor = my_data.coursor ()

# Insert a record in

sq1 = "INSERT INTO CUSTOMERS (name,address) VALUES (%s, %s)"
va1 = ("Marian", "Dlhe Luky 6004")
mycursor.execute (sq1, va1)

my_data.commit ()

print (mycursor.rowcount, "recerd inserted")

# Insert Multiple Rows
# To insert multiple rows into a table, use the executemany() method.

sq2 = "INSERT INTO CUSTOMERS (name, address) VALUES (%s, %s)"
va2 = [
    ('Marian', 'Dlhe Luky 6004'),
    ('Hanka', 'Dlhe Luky 6004'),
    ('Eva', 'Okruzna 1426'),
    ('Fero', 'Snp 1')
    ('Father', 'Dlha ulica 52')
]

mycursor.executemany (sq2, va2)

my_data.commit ()
print (mycursor.rowcount, "inserted.")

# Insert one row, and return the ID:

sq3 = "INSERT INTO customers (name, adress) VALUES (%s, %s)"
va3 = ("Marian", "Dlhe Luky 6004")
mycursor.execute (sq3, va3)

my_data.commit ()

print ("1 record inserted, ID:", mycursor.lastrowid)
