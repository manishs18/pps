from pymongo import MongoClient


myclient = MongoClient('mongodb://localhost:27017')

mydb = myclient["mydb"]