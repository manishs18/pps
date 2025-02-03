'''
10. A university has the following rules for a student to qualify for a degree with A as the main subject and B as the subsidiary subject:
    (a) He should get 55 percent or more in A and 45 percent or more in B.
    (b) If he gets than 55 percent in A he should get 55 percent or more in B. However, he should get at least 45 percent in A.
    (c) If he gets less than 45 percent in B and 65 percent or more in A he is allowed to reappear in an examination in B to qualify.
    (d) In all other cases he is declared to have failed.
    '''

def check_qualification(percentage_A, percentage_B):

    if percentage_A >= 55 and percentage_B >= 45:
        return "Qualified for the degree."
    elif percentage_A >= 45 and percentage_A < 55 and percentage_B >= 55:
        return "Qualified for the degree."
    elif percentage_A >= 65 and percentage_B < 45:
        return "Allowed to reappear in examination for subject B."
    else:
        return "Failed."

def main():

    percentage_A = float(input("Enter percentage in subject A: "))
    percentage_B = float(input("Enter percentage in subject B: "))

    result = check_qualification(percentage_A, percentage_B)
    print(result)


main()
