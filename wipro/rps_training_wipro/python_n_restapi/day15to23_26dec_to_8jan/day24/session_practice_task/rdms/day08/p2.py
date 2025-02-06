import mysql.connector


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Rps@123456"
)

mycur = mydb.cursor()

#mycur.execute('create database testdb1')

mycur.execute('show databases')

for i in mycur:
    print(i)
    if i[0] == 'testdb1':
        print("Found")
