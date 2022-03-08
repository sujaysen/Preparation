# Mysql-Python connection
import mysql.connector
#mysql connection
mydb = mysql.connector.connect(
        host= "localhost",
        user= "justdial",
        password= "justdial",
        auth_plugin='mysql_native_password',
        database="sujay",
        buffered=True
)

mycursor = mydb.cursor()

# Show all DB
db_list = []
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    db_list.append(x[0].decode())

# Create DB
if "sujay" not in db_list:
    mycursor.execute("CREATE DATABASE sujay")
    print("Database Created Successfully")


# Show all tables
table_list = []
mycursor.execute("SHOW TABLES")
for x in mycursor:
    table_list.append(x[0].decode())

if "customers" not in table_list:
    mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
    print("Table Created Successfully")

mycursor.close()
