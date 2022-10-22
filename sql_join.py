# Join Two or More Tables
# You can combine rows from two or more tables, based on a related column between them, by using a JOIN statement.
# Consider you have a "users" table and a "products" table:

import mysql.connector

my_data = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

mycursor = my_data.cursor()

sq13 = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

mycursor.execute(sq13)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
