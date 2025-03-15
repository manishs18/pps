import requests


def fetch_randomProducts_getProducts():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    response = requests.get(url)
    data = response.json()
    if data["success"] and "data" in data:
        product_data = data["data"]["data"][4]
        category = product_data["category"]
        title = product_data["title"]
        price = product_data["price"]
        return category, title, price
    else:
        raise Exception("Failed to fetch product data")
    
def main():
    try:
        category, price, title = fetch_randomProducts_getProducts()
        print(f"Category: {category} \n Title: {title} \n Price: {price} ")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()