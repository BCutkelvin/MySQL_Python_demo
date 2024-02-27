import mysql.connector


#connect to db:
db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin"
    #database = "testdatabase"
)

#create a cursor object to run a query:
mycursor = db.cursor()

#create a new db:
mycursor.execute("CREATE DATABASE testdatabase")