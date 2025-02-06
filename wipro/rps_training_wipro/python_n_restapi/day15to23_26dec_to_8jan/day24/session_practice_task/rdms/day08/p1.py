'''
test mysql-connector
'''
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "manish18",
    password = "Manish@18"
)

mycur = mydb.cursor()

mycur.execute('create database testdb')