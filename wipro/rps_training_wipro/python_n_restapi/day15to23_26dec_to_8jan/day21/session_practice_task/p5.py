class Employee:

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f'Employee Name: {self.name}'

    def __add__(self, other):
        name = self.name.upper()

        return Employee(name + other.name)



e1 = Employee("Manish")
e2 = Employee("Singh")

print(e1)
print(e2)
e3 = e1+e2
print(e3)