'''
Task 1: Use the requests library in Python to make a GET request to a public API and print the response.
'''

import requests

import requests

url = "https://api.github.com"  
response = requests.get(url)

print("Status Code:", response.status_code)
print("Response Content:", response.json())  
