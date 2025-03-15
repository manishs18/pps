import requests

def fetch_randomProducts_getRandomProduct():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        product_data = data["data"]
        # id = product_data["id"]
        title = product_data["title"]
        brand = product_data["brand"]
        category = product_data["category"]
        # price = product_data["price"]
        return title, brand, category
    else:
        raise Exception("Failed to fetch product data")
    
def main():
    try:
        title, brand, category = fetch_randomProducts_getRandomProduct()
        print(f"Title: {title} \n Brand: {brand} \n Category: {category} ")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()