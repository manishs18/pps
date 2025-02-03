# 6. Write a Python program which accepts the radius of a circle from the user and compute the area. 



import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print(f"The area of the circle is: {area:.2f}")
