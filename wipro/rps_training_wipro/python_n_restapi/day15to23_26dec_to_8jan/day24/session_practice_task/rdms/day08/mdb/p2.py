from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string if needed
db = client["mydatabase"]
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

# Example usage
if __name__ == "__main__":
    # Create
    create_document({"name": "John", "age": 30, "city": "New York"})
    
    # Read
    print("Documents in collection:")
    read_documents()
    
    # Update
    update_document({"name": "John"}, {"age": 31})
    
    # Delete
    delete_document({"name": "John"})