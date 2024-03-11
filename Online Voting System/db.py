import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="project"
)

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM voters")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
  print(x[0])
  print(x[1])
