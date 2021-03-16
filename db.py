import pymysql

mydb = pymysql.connect(
  host='localhost',
  user='system',
  password='dipanwita',
  db='logindemo'
  )
print(mydb)
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE logindemo")
#mycursor.execute("CREATE TABLE cust(email varchar(255),password varchar(255))")
#mycursor.execute("INSERT INTO cust (email,password) VALUES('dipanwita','dipa@123')")
#mycursor.execute("INSERT INTO cust (email,password) VALUES('ritika','ritika@123')")
#mycursor.execute("SHOW TABLES")
mycursor.execute("SELECT *FROM cust")
result=mycursor.fetchall()
#mydb.commit()
print(result)
