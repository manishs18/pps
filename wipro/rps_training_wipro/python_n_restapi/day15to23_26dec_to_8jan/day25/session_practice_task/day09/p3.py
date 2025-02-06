import requests


url = "https://jsonplaceholder.typicode.com/posts/1"

#REST API
response = requests.get(url)

print(response.json())






