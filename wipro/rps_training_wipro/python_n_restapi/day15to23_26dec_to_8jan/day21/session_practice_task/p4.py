class Emp:

    def __init__(self,name="",id=0):
        print("Constr Called")
        self.name = name
        self.id = id

    def __str__(self):
        # return "This is an Employee Class"
        return f"Employee {self.id}'s Name is {self.name}"

    def disp(self):
        print(f"Employee {self.id}'s Name is {self.name}")


objE = Emp(id=101,name="bhima")

print(objE)
objE.disp()
