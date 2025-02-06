'''
Q1. develop a script in python which get the details of the Employee details from the user input and store them in MySQL.

1. you need to do CRUD operations as different functions for each operations
2. try to get the sorted data from the db and print it on the screen

'''

import mysql.connector
from mysql.connector import Error

class EmployeeMySQL:
    def _init_(self, host, user, password, database):
        try:
            self.connection = mysql.connector.connect(
                host=host,
                user=user,
                password=password,
                database=database
            )
            self.cursor = self.connection.cursor()
            self._create_table()
            print("Connected to the database successfully.")
        except Error as e:
            print(f"Error connecting to the database: {e}")
            self.connection = None
            self.cursor = None

    def _create_table(self):
        try:
            self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                age INT,
                department VARCHAR(255)
            )
            """)
            self.connection.commit()
        except Error as e:
            print(f"Error creating table: {e}")

    def create_employee(self, name, age, department):
        try:
            query = "INSERT INTO employees (name, age, department) VALUES (%s, %s, %s)"
            self.cursor.execute(query, (name, age, department))
            self.connection.commit()
            print("Employee added successfully.")
        except Error as e:
            print(f"Error adding employee: {e}")

    def read_employees(self):
        try:
            query = "SELECT * FROM employees ORDER BY name"
            self.cursor.execute(query)
            for row in self.cursor.fetchall():
                print(row)
        except Error as e:
            print(f"Error reading employees: {e}")

    def update_employee(self, emp_id, name=None, age=None, department=None):
        try:
            updates = []
            params = []
            if name:
                updates.append("name = %s")
                params.append(name)
            if age:
                updates.append("age = %s")
                params.append(age)
            if department:
                updates.append("department = %s")
                params.append(department)
            params.append(emp_id)
            query = f"UPDATE employees SET {', '.join(updates)} WHERE id = %s"
            self.cursor.execute(query, tuple(params))
            self.connection.commit()
            print("Employee updated successfully.")
        except Error as e:
            print(f"Error updating employee: {e}")

    def delete_employee(self, emp_id):
        try:
            query = "DELETE FROM employees WHERE id = %s"
            self.cursor.execute(query, (emp_id,))
            self.connection.commit()
            print("Employee deleted successfully.")
        except Error as e:
            print(f"Error deleting employee: {e}")

    def close(self):
        try:
            if self.cursor:
                self.cursor.close()
            if self.connection:
                self.connection.close()
            print("Database connection closed.")
        except Error as e:
            print(f"Error closing the database connection: {e}")


# Usage
if __name__ == "_main_":
    db = EmployeeMySQL("localhost", "manish18", "Manish@18", "manishdb")
    if db.connection:
        db.create_employee("Bhima Sir", 45, "Python Trainer")
        db.read_employees()
        db.update_employee(1, age=31)
        db.read_employees()
        db.delete_employee(1)
        db.read_employees()
        db.close()