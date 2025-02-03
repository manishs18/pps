#8.   When interest compounds q times per year at an annual rate of r % for n years, the principle p compounds to an amount a as per the following formula a = p ( 1 + r / q ) nq
 #    Write a program to read 10 sets of p, r, n & q and calculate the corresponding as.

for i in range(1, 11):
    print(f"\nSet {i}:")
    p = float(input("Enter the principal amount (p): "))
    r = float(input("Enter the annual interest rate (r%) as a decimal: "))
    n = int(input("Enter the number of years (n): "))
    q = int(input("Enter the number of times interest is compounded per year (q): "))

    a = p * (1 + r / q) ** (n * q)
    print(f"The compound amount (a) is: {a:.2f}")

