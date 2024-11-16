#Exercise 15: Get an int value of base raises to the power of exponent
def powerExponent(base, exp):
    num = exp
    result = 1
    while num > 0:
        result = result * base
        num = num -1
    print(base, "raises to the power of", exp, "is: ", result)


n = int(input(" Enter the Base Digit: "))
e = int(input(" Enter the digit Exponent Power: "))
powerExponent(n, e)
