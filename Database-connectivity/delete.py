import mysql.connector
conn = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="student"
)
mycr = conn.cursor()
sql = "DELETE FROM detail  WHERE id = 5"
mycr.execute(sql)
conn.commit()
print(mycr.rowcount, "row deleted.")
