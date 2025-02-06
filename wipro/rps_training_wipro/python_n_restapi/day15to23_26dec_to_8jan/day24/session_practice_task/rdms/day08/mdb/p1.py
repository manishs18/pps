
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client['mydb']

collections = db['users']

print('Databases : ', client.list_database_names())

print('Collections : ', db.list_collection_names())

