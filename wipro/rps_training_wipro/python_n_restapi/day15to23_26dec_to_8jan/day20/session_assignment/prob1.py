# WAP to get details of the EMP and print/display for 5 employees

class Employee:
    company_name = 'Wipro'
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def display_details(self):
        print(f"Company: {Employee.company_name}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Salary: {self.salary:.2f}")

e1 = Employee
employees = []
for i in range(5):
    print("Enter details for Employee:",(i+1))
    name = input("Name: ")
    age = int(input("Age: "))
    salary = float(input("Salary: "))
    employees.append(e1(name, age, salary))
    print()  

print("\nEmployee Details:")
for emp in employees:
    print(f"\nEmployee {i}:")
    emp.display_details()
