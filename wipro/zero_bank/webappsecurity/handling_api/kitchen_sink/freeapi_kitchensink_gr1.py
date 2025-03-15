import requests

def get_kitchensink_gr1():
    url = "https://api.freeapi.app/api/v1/kitchen-sink/http-methods/get"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        kitchensink_data = data["data"]
        method = kitchensink_data["method"]
        return method
    else:
        raise Exception("Failed to fetch kitchensink data")
    
def main():
    try:
        method = get_kitchensink_gr1()
        print(f"Method: {method}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()