#Logical Building Problems 



# 🔹 1. String Manipulation

# Q1: Reverse a string
def reverse_string(s: str) -> str:
    return s[::-1]

# Q2: Check if a string is a palindrome
def is_palindrome(s: str) -> bool:
    return s == s[::-1]

# Q3: Count specific character in a string
def count_char(s: str, char: str) -> int:
    return s.count(char)


# 🔹 2. Array Operations

# Q1: Find duplicates in a list
def find_duplicates(arr):
    seen, dupes = set(), set()
    for val in arr:
        if val in seen:
            dupes.add(val)
        else:
            seen.add(val)
    return list(dupes)

# Q2: Merge two arrays
def merge_arrays(a, b):
    return a + b

# Q3: Rotate array to the right by k steps
def rotate_array(arr, k):
    k = k % len(arr)
    return arr[-k:] + arr[:-k]


# 🔹 3. Mathematical Problems

# Q1: Find GCD of two numbers
def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Q2: Find LCM of two numbers
def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

# Q3: Check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


# 🔹 4. Pattern Printing

# Q1: Print right-angled triangle
def print_triangle(n):
    for i in range(1, n+1):
        print('*' * i)

# Q2: Print pyramid pattern
def print_pyramid(n):
    for i in range(n):
        print(' ' * (n - i - 1) + '*' * (2*i + 1))

# Q3: Print square with borders
def print_bordered_square(n):
    for i in range(n):
        if i == 0 or i == n-1:
            print('*' * n)
        else:
            print('*' + ' ' * (n - 2) + '*')



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






# 1. Launch Chrome WebDriver
from selenium import webdriver
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()  # Optional: Maximize the window
    driver.get("https://example.com")  # Replace with your target URL
    yield driver
    driver.quit()  # Close the browser after tests

# 2. Handle Multiple Windows / Tabs
from selenium.webdriver.common.by import By
import time

# Store parent window
parent_window = driver.current_window_handle

# Click to open new window/tab
driver.find_element(By.LINK_TEXT, "Open New Window").click()

# Optional wait to allow new window to open
time.sleep(2)

# Get all window handles
all_windows = driver.window_handles

# Switch to child window
for handle in all_windows:
    if handle != parent_window:
        driver.switch_to.window(handle)
        print("Child window title:", driver.title)
        # Do your actions in child window
        driver.close()  # Close child

# Switch back to parent
driver.switch_to.window(parent_window)
print("Back to parent window:", driver.title)


# 🔹 1. Check Website Title
from selenium import webdriver

def check_title(url: str, expected_title: str) -> bool:
    driver = webdriver.Chrome()
    driver.get(url)
    result = driver.title == expected_title
    driver.quit()
    return result


# 🔹 2. Login and Redirect Check
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def login_and_check(driver, username, password):
    driver.get("http://example.com/login")
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
    WebDriverWait(driver, 10).until(EC.url_contains("/dashboard"))
    return "/dashboard" in driver.current_url


# 🔹 3. Click When Button Becomes Enabled
def click_enabled_button(driver):
    driver.get("http://example.com/button-page")
    WebDriverWait(driver, 10).until(
        lambda d: d.find_element(By.ID, "delayed-button").is_enabled()
    )
    driver.find_element(By.ID, "delayed-button").click()
    return True


# 🔹 4. Get All Product Titles
def get_product_titles(driver):
    driver.get("http://example.com/products")
    titles = [e.text for e in driver.find_elements(By.CSS_SELECTOR, "div.product h3")]
    return titles


# 🔹 5. Verify Table is Sorted
def is_table_sorted(driver):
    driver.get("http://example.com/sortable-table")
    driver.find_element(By.ID, "sort-name").click()
    WebDriverWait(driver, 5).until(lambda d: d.find_element(By.CSS_SELECTOR, "table"))
    rows = driver.find_elements(By.CSS_SELECTOR, "table tbody tr td.name")
    names = [r.text for r in rows]
    return names == sorted(names)


# 🔹 6. File Upload Automation
def upload_file(driver, file_path):
    driver.get("http://example.com/upload")
    upload_input = driver.find_element(By.ID, "file-upload")
    upload_input.send_keys(file_path)
    driver.find_element(By.ID, "submit-upload").click()
    success = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.ID, "upload-success"))
    )
    return success.text == "Upload complete"


# 🔹 7. Dropdown Selection
from selenium.webdriver.support.ui import Select

select = Select(driver.find_element(By.ID, "dropdown_id"))
select.select_by_visible_text("OptionText")


# 🔹 8. Alert Handling
alert = driver.switch_to.alert
alert.accept()   # Accept alert
alert.dismiss()  # Dismiss alert


# 🔹 9. Implicit Wait
driver.implicitly_wait(10)


# 🔹 10. Explicit Wait for Visibility
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

wait = WebDriverWait(driver, 10)
element = wait.until(EC.visibility_of_element_located((By.ID, "element_id")))
