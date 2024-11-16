#Exercise 3: Convert Decimal number to octal using print() output formatting


class DisNtoOct:
    def __init__(self, a):
        c = a
        print('%o' % c )

s= int(input("Enter the digit: "))
o = DisNtoOct(s)