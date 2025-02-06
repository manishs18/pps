'''
Task 2: Write a Python program that handles HTTP errors gracefully (e.g., 404 or 500 errors) when making API requests."

'''


import requests

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx and 5xx)
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # Example: 404 Not Found
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")  # Handles other requests exceptions

# Example usage
url = "https://api.github.com/nonexistent"  # Intentionally incorrect endpoint
result = fetch_data(url)
if result:
    print("Response Content:", result)
