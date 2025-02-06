import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)

#verify the request

print("Status Code: ", response.status_code)
print("Response Body: ",response.json())

