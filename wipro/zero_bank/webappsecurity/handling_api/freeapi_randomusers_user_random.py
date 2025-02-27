import requests

def fetch_randomusers_user_random():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    respone = requests.get(url)
    print(respone)
    data = respone.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch user data")
    

def main():
    try:
        username, country  = fetch_randomusers_user_random()
        print(f"Username: {username} \n Country: {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()

        