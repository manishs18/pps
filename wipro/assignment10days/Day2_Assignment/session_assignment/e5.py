'''
5. WAP to calculate and display the interest on a loan amount(Rupees). 

You would need three variables to hold ’principal’, Rate_of_interest’(%) and ’time’ in years and can use the formula 
Interest=(principal*rate_of_interest*time)/100 
Note :Take user input '''



principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (%): "))
time = float(input("Enter the time (in years): "))

interest = (principal * rate_of_interest * time) / 100
print(f"The interest on the loan is: {interest:.2f}")
