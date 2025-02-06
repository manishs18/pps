'''
Task 2: Write a Python script to send a POST request with JSON data and handle the JSON response.
'''

import requests

url = "https://jsonplaceholder.typicode.com/posts" 

data = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Content:", response.json())  
