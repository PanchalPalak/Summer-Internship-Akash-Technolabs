import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='student'
)
mycr=conn.cursor()
sql = "INSERT INTO detail(id,age,name) VALUES (3, 42,'ip')"
mycr.execute(sql)
conn.commit()
print(mycr.rowcount, "row inserted.")