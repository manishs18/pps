import requests


def fetch_randomProducts_getProductsById():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/30"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        product_data = data["data"]
        id = product_data["id"]
        title = product_data["title"]
        brand = product_data["brand"]
        category = product_data["category"]
        price = product_data["price"]
        return id, title, brand, category, price
    else:
        raise Exception("Failed to fetch product data")
    
def main():
    try:
        id, title, brand, category, price = fetch_randomProducts_getProductsById()
        print(f"Id: {id} \n Title: {title} \n Brand: {brand} Category: {category} \n Price: {price} ")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()