#Logical Building Problems 

#1. Reverse a String Without Using Built-in Functions. 
def reverse_string(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

print(reverse_string("hello"))  


#2. Find the Second Largest Number in a List 
def second_largest(numbers):
    unique_numbers = list(set(numbers))  
    unique_numbers.sort(reverse=True)
    return unique_numbers[1] if len(unique_numbers) > 1 else None

print(second_largest([3, 5, 1, 5, 9, 3]))  

#3. Print numbers from 1 to 100. For multiples of 3, print "Fizz"; for 
#multiples of 5, print "Buzz"; for multiples of both, print "FizzBuzz". 
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


#4. Check if Two Strings are Anagrams 
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

print(are_anagrams("listen", "silent"))  

#5. Find All Prime Numbers in a Range 
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                primes.append(num)
    return primes

print(find_primes(10, 50))  

#6. Generate Fibonacci Sequence 
def fibonacci(n):
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(10))  

#7. Find the Most Frequent Element in a List 
def most_frequent_element(lst):
    frequency = {}
    for item in lst:
        frequency[item] = frequency.get(item, 0) + 1
    return max(frequency, key=frequency.get)

print(most_frequent_element([1, 2, 3, 2, 2, 4, 3]))  

#8. Check if a Number is Armstrong 
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    return sum(d ** len(digits) for d in digits) == num

print(is_armstrong(153)) 

#9. Merge Two Sorted Lists 
def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
    return merged_list

print(merge_sorted_lists([1, 3, 5], [2, 4, 6]))  



#10.Find the Longest Word in a String
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

print(longest_word("Find the longest word in this sentence")) 






 