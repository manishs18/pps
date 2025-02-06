import pytest
def search_products(query):
    # Mock data for testing
    products = {"laptop": 5, "phone": 10}
    return products.get(query, 0)

@pytest.mark.parametrize("query,expected_count", [
    ("laptop", 5),
    ("phone", 10),
])
def test_product_search(db_connection, query, expected_count):
    result_count = search_products(query)
    assert result_count == expected_count
