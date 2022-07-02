import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="student"
)
mycr = conn.cursor()
mycr.execute("SELECT * FROM detail")

myresult = mycr.fetchall()
for x in myresult:
    print(x)
