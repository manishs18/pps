
'''
Q2. develop a script in python which get the details of the Employee details from the user input and store them in NoSQL.

1. you need to do CRUD operations as different functions for each operations
2. try to get the sorted data from the db and print it on the screen


Note: use OOPS concepts in the above codes
'''

from pymongo import MongoClient

class EmployeeNoSQL:
    def __init__(self, uri, database_name, collection_name):
        self.client = MongoClient(uri)
        self.database = self.client[database_name]
        self.collection = self.database[collection_name]

    def create_employee(self, name, age, department):
        employee = {"name": name, "age": age, "department": department}
        self.collection.insert_one(employee)
        print("Employee added successfully.")

    def read_employees(self):
        employees = self.collection.find().sort("name", 1)
        for emp in employees:
            print(emp)

    def update_employee(self, emp_id, name=None, age=None, department=None):
        updates = {}
        if name:
            updates["name"] = name
        if age:
            updates["age"] = age
        if department:
            updates["department"] = department
        self.collection.update_one({"_id": emp_id}, {"$set": updates})
        print("Employee updated successfully.")

    def delete_employee(self, emp_id):
        self.collection.delete_one({"_id": emp_id})
        print("Employee deleted successfully.")

    def close(self):
        self.client.close()


# Usage
if __name__ == "__main__":
    db = EmployeeNoSQL("mongodb://localhost:27017/", "manish18", "employees")
    db.create_employee("Manish", 25, "STE")
    db.read_employees()
    # Replace the ObjectId value with the actual _id from the database to test update and delete
    # db.update_employee(ObjectId("..."), age=26)
    # db.delete_employee(ObjectId("..."))
    db.read_employees()
    db.close()

