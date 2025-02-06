import requests

url = "http://127.0.0.1:5000/users"

#headers
headers = {
    "Content-Type" : "application/json"
}

payload = {
    "name" : "Manish",
    "email"  : "Manish@gmail.com",
    "job": "Software Engineer"
}

response = requests.post(url,json=payload)
'''
if response.status_code == 200:
    print("Record retrived successfully")
    data = response.json()
    print("Response Data: ", data)
else:
    print(f"failed to retrive data. Status code {response.status_code}")

'''
if response.status_code == 201:
    print("Record created successfully")
    data = response.json()
    print("Response Data: ", data)
else:
    print(f"failed to create data. Status code {response.status_code}")