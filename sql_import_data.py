import mysql.connector
import pandas as pd # import library 
# work from databases
data_conti = pd.read_csv('172_17_0_1.csv') # import data
print (data_conti) # print data

# connection localhost
my_data = mysql.connector.connect (
    host = "/tmp/mysql80.sock",  # sql address on the server
    user = "yourusername", # often root or admin
    password = "yourpassword"  
)
print(my_data)
