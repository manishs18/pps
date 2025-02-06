try:
    age=input("Enter age of person: ")
    if age.isdigit():
        age = int(age)
    else:
        raise TypeError("Age must be in numeric")

    if age<0:
        raise ValueError("Age can't be negative")
except ValueError as e:
    print("Invalid Age: ",e)
except TypeError as e:
    print("TypeConversion Error: ",e)
else:
    print("Age of the person: ",age)
