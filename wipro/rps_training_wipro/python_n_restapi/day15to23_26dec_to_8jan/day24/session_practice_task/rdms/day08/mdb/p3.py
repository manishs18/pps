from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string if needed
db = client["myda"]
collection = db["mycollection"]

# CREATE
def create_document(data):
    result = collection.insert_one(data)
    print("Inserted document with ID:", result.inserted_id)

# READ
def read_documents():
    documents = collection.find()
    for doc in documents:
        print(doc)

# UPDATE
def update_document(filter_query, update_query):
    result = collection.update_one(filter_query, {"$set": update_query})
    print("Matched:", result.matched_count, "Modified:", result.modified_count)

# DELETE
def delete_document(filter_query):
    result = collection.delete_one(filter_query)
    print("Deleted documents:", result.deleted_count)

def delete_many(filter_query):
    result = collection.delete_many(filter_query)
    #print("Deleted documents:", result.deleted_count)
    
def insertMany(lVals):
    result = collection.insert_many(lVals)
    # print("Inserted document with ID:", result.inserted_id)

# Example usage
if __name__ == "__main__":
    # Create
    #create_document({"name": "Bhima", "age": 45, "city": "Bangalore"})
    
    # Read
    # print("Documents in collection:")
    # read_documents()
    
    # Update
    #update_document({"name": "Bhima"}, {"name": "xyz"})
    
    # Delete
    # delete_document({"name": "xyz"})

    data = [
        {"_id":1,"name": "Bhima1", "age": 45, "city": "Bangalore1"},
        {"_id":2,"name": "Bhima2", "age": 45, "city": "Bangalore2"},
        {"_id":3,"name": "Bhima3", "age": 45, "city": "Bangalore3"}
    ]
    insertMany(data)
    # delete_many({"name":"John"})


