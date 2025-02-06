import requests

url = "https://jsonplaceholder.typicode.com/posts"

#headers
headers = {
    "Content-Type" : "application/json"
}

payload = {
    "title" : "Amit's Page",
    "body"  : "Pages Body",
    "userId": 1
}

response = requests.post(url, json=payload, headers=headers)

if response.status_code == 201:
    print("Record created successfully")
    data = response.json()
    print("Response Data: ", data)
else:
    print(f"failed to create record. Status code {response.status_code}")