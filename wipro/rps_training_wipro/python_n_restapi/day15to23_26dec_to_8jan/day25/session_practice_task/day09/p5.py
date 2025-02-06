'''
features request:

1. installation, 
2. quick start (request.get(url)),
3. validations response (status_code, header, .json())


payload => data to be sent using POST -> json format
headers => it included to specify the content type: (ex: application/json)

'''


import requests

url = "https://jsonplaceholder.typicode.com/post/1"

response =  requests.get(url)

if response.status_code == 200:
    print("Response is OK")
    data = response.json()
    print("Title: ",data['title'])
    print("Body: ",data['body'])
else:
    print(f'Failed to fetch data. Status Code: {response.status_code}')

