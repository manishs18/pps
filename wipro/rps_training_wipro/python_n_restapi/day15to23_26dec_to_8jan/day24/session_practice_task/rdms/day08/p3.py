import mysql.connector


def createDB():
    #create database
    mycur.execute('create database testdb')


def createTable():
    #create table
    sqlCmd = 'create table emp(id int, name varchar(255), sal int)'

def updateDB():
    #update operations on table
    name = input("Name: ")
    sqlCmd = f"update emp set name='{name}' where id=103"
    mycur.execute(sqlCmd)
    mycur.execute('commit')

def deleteRow():
    #delete operations on table
    id = int(input("ID: "))
    sqlCmd = f"delete from emp where id={id}"
    mycur.execute(sqlCmd)
    mycur.execute('commit')

def insertDB():
    #insert values in the table
    
    sqlCmd = "insert into emp(id,name,sal) values (102,'shankar',10002)"
    mycur.execute(sqlCmd)
    sqlCmd = "insert into emp(id,name,sal) values (103,'amit',10003)"
    mycur.execute(sqlCmd)
    sqlCmd = "insert into emp(id,name,sal) values (108,'kumar1',10009)"
    mycur.execute(sqlCmd)
    mycur.execute('commit')

def insertMany():
    #insert many values
    sqlCmd = "insert into emp(id,name,sal) values (%s, %s, %s)"
    val = [
        (105,'abc1',1001),
        (106,'abc2',1002),
        (107,'abc3',1003),
        (108,'abc4',1004)
    ]
    mycur.executemany(sqlCmd,val)
    mydb.commit()


def readDB():
    #read all the content from the table
    sqlCmd = "select * from emp"
    mycur.execute(sqlCmd)
    rows = mycur.fetchall()
    # print(rows, type(rows))
    for rec in rows:
        print(rec, type(rec))

def searchDB():
    #fetch for a rec
    id = int(input("ID: "))
    sqlCmd = f"select * from emp where id = {id}"
    mycur.execute(sqlCmd)
    rows = mycur.fetchall()
    if len(rows)<=0:
        print("No record found")
        return
    for rec in rows:
        print(rec)


def sortDBAsc():
    #sort values ASC
    sqlCmd = "select * from emp order by name"
    mycur.execute(sqlCmd)
    rows = mycur.fetchall()
    if len(rows)<=0:
        print("No record found")
        return
    for rec in rows:
        print(rec)

def sortDBDesc():
    #sort values DESC
    sqlCmd = "select * from emp order by name desc"
    mycur.execute(sqlCmd)
    rows = mycur.fetchall()
    if len(rows)<=0:
        print("No record found")
        return
    for rec in rows:
        print(rec)

mydb = mysql.connector.connect(
    host = "localhost",
    user = "newuser",
    password = "Pass@123456",
    database = 'testdb'
)

mycur = mydb.cursor()

#createDB()
#createTable()
# insertDB()
#updateDB()
#deleteRow()
# insertMany()
# print(mycur.rowcount)

readDB()
print("="*50)
# searchDB()
sortDBAsc()
print("="*50)
sortDBDesc()