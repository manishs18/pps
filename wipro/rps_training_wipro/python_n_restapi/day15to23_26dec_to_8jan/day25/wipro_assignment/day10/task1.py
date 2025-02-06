'''
Task 1: Create a Python script that uses OAuth authentication to connect to a RESTful service.
'''


from requests_oauthlib import OAuth1

url = "https://api.twitter.com/1.1/account/verify_credentials.json"

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

auth = OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)

response = requests.get(url, auth=auth)

print("Status Code:", response.status_code)
print("Response Content:", response.json())
