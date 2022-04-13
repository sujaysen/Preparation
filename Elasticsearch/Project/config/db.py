# Write all db details
import mysql.connector

#mysql connection
testDB = mysql.connector.connect(
	host= "hostname",
  	user= "username",
  	password= "password",
  	database= "dbname"
)
