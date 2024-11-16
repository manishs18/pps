#Exercise 9: Check Palindrome Number



def palindromeOrNot(a):
    print("Orignal number is: ", a)
    original_a = a
    rev_a=0
    while a > 0:
        i_num = a % 10
        rev_a = (rev_a*10) + i_num
        a = a // 10
    if original_a == rev_a:
        print(original_a, ": Number is palindrome")
    else:
        print(original_a, ": number is not palindrome") 

a1 = int(input("Enter the value: "))
palindromeOrNot(a1)
