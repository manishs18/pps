class Person:

    def __init__(self,name,age,g,phno):
        print("Constr Person")
        self.name = name
        self.age = age
        self.gender = g
        self.phno = phno

    # do here getters and setters

    def dispPerson(self):
        print(f'Name: {self.name}\n'
              f'Age: {self.age}\n'
              f'Gender: {self.gender}\n'
              f'Phno: {self.phno}')

    def setValPerson(self):
        pass


class Employee(Person):

    def __init__(self, id, sal, d,name,age,g,phno):
        super().__init__(name,age,g,phno)
        print("Employee Constr")
        self.empId = id
        self.empSal = sal
        self.empDesg = d

    def dispEmp(self):
        self.dispPerson()
        print(f'ID: {self.empId}\n'
              f'Desgination: {self.empDesg}\n'
              f'Salary: {self.empSal}')

    def getId(self):
        return self.empId
    def setSal(self,sal):
        self.empSal = sal



def dispAllEmp(e):
    for i in e:
        print("=" * 20)
        i.dispEmp()
        print("=" * 20)


def updateSalary(e,id):
    for i in e:
        if i.getId() == id:
            i.setSal(200000)
            break


def getDetailsEmp(e,n):
    # e.append(Employee(101, 100001, "SE", "manish1", 24, "M", 9988))
    # e.append(Employee(102, 100002, "SE", "manish2", 25, "M", 9989))
    # e.append(Employee(103, 100003, "SE", "manish3", 26, "M", 9987))
    for i in range(n):
        name=input("Name: ")
        age = int(input("Age: "))
        g = input("Gender (M/F/T): ")
        phno = int(input("Phno: "))
        id = int(input("ID: "))
        sal = int(input("Salary: "))
        desg = input("Desgination: ")
        e.append(Employee(id,sal,desg,name,age,g,phno))
    else:
        print("Done with getting details of Employees")


    return None

# e1 = Employee(101,10001,"SE")
e = []
n = int(input("Employee Numbers: "))
getDetailsEmp(e,n)
id = int(input("Enter the Employee ID: "))
dispAllEmp(e)
updateSalary(e,id)


dispAllEmp(e)