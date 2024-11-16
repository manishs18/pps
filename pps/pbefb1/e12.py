#Exercise 12: Calculate income tax
tax_payable = 0
def incomeTax(n):
    if n <= 10000:
        print("Tax Payable is 0")
    elif n <= 20000:
        x = n - 10000
        tax_payable = x * 10 / 100
        print("Total tax payable is ", tax_payable)
    else:
        tax_payable = 0
        tax_payable = 10000 * 10 / 100
        tax_payable = tax_payable + (n - 20000) * 20 / 100
        print("Total tax to pay is: ", tax_payable)

s = int(input("Enter Salary: "))
d = incomeTax(s)