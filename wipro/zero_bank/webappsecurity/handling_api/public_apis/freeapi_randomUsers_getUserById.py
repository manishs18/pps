import requests

def fetch_randomUsers_getUserById():
    url = f"https://api.freeapi.app/api/v1/public/randomusers/13"
    respone = requests.get(url)
    data = respone.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        user_id = user_data["id"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return user_id, username, country
    else:
        raise Exception("Failed to fetch user data")
    
def main():
    try:
        user_id, username, country  = fetch_randomUsers_getUserById()
        print(f"User ID: {user_id} \n Username: {username} \n Country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()