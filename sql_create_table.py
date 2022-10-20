# Creating a Table - "CREATE TABLE"
# Create a table named "conti_nr":
import mysql.connector

my_data = mysql.connector.connect (
    host ="locahost",
    user ="yourusername",
    password ="zourpassword",
    database ="my_date"    
)

mycursor = my_data.cursor ()

mycursor.execute ("CREATE TABE customers (Colors VARCHAR(255), Wc INTEGER (30))")
# If the above code was executed with no errors, you have now successfully created a table.

# Exists table - ("SHOW TABLES")

mycursor.execute ("SHOW TABLES")

for x in mycursor:
    print (x)

# Primary key / ("INT AUTO_INCREMENT PRIMARY KEY")
# When creating a table, you should also create a column with a unique key for each record.
# This can be done by defining a PRIMARY KEY.

mycursor.execute ("CREATE TABLE customs (id INT AUTO_INCREMENT PRIMARY KEY, Colors VARCHAR (255), Wc INTEGER (30))")

# If the table already exists, use the ALTER TABLE keyword:
mycursor.execute("ALTER TABLE customs (id INT AUTO_INCREMENT PRIMARY KEY, Colors VARCHAR (255), Wc INTEGER (30))")
