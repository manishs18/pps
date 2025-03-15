import requests

def fetch_randomUsers_getUsers():
    url = "https://api.freeapi.app/api/v1/public/randomusers?page=1&limit=10"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]["data"][4]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failled to fetch to user data")

def main():
    try:
        username, country = fetch_randomUsers_getUsers()
        print(f"username: {username} \n country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

