import requests

BASE_URL = "https://reqres.in"

def login_and_get_token(email, password):
    
    login_url = f"{BASE_URL}/api/login"
    
    payload = {
        "email":email,
        "password":password
    }

    response = requests.post(login_url,json=payload)

    if response.status_code == 200:
        print("login successful")
        token = response.json().get("token")
        print(f"Token recieved: {token}")
        return token
    else:
        print(f"login failed SC: {response.status_code}")
        print("Response: ",response.json())
        return None
    
def fetch_protected_data(token):

    protected_url = f"{BASE_URL}/api/users?page=2"

    headers = {
        "Authorization":f"Bearer {token}"
    }

    response = requests.get(protected_url, headers=headers)

    if response.status_code == 200:
        print("Protected data fected successfully")
        print("Data: ",response.json())

    else:
        print(f"Failed to fetch protected data. SC {response.status_code}")
        print("Response: ",response.json)


if __name__ == "__main__":
    email = "eve.holt@reqres.in"
    password = "cityslicka"
    token = login_and_get_token(email, password)

    if token:
        fetch_protected_data(token)


