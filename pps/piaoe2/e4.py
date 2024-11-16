#Exercise 4: Display float number with 2 decimal places using print()

class DisFtoDec:
    def __init__(self, a):
        print('%.2f' % a)

s = float(input("Enter the float value: "))
o = DisFtoDec(s)
