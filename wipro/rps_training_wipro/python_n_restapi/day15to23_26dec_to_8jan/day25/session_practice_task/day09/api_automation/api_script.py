import requests
import json
from config import BASE_URL, HEADERS

def get_response(resource_id):
    """Fetch a record using GET request"""
    url = f"{BASE_URL}/posts/{resource_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f'Failed to fetch record. Status Code: {response.status_code}')
    

def create_record(payload_path):
    """create a record using POST request"""
    url = f'{BASE_URL}/posts'

    with open(payload_path, "r") as file:
        payload = json.load(file)
    
    response = requests.post(url, json=payload, headers=HEADERS) 
    if response.status_code == 201:
        return response.json()
    else:
        raise Exception(f'Failed to create a record. Status Code: {response.status_code}')
    

if __name__ == "__main__":
    try:
        #GET request
        resource = get_response(1)
        print("Feteched Record: ",resource)

        #POST request
        new_resource = create_record("payload.json")
        print("Created record: ",new_resource)

    except Exception as e:
        print(e)
