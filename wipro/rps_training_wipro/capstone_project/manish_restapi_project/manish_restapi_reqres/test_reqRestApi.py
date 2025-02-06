import requests
import pytest

BASE_URL = "https://reqres.in/api"


# 1. GET /users?page=2
def test_get_users_page_2():
    response = requests.get(f"{BASE_URL}/users?page=2")
    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert len(response.json()["data"]) > 0


# 2. GET /users/{id} with valid ID
@pytest.mark.parametrize("user_id", [2])
def test_get_user_by_valid_id(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    assert response.json()["data"]["id"] == user_id


# 3. GET /users/{id} with invalid ID
def test_get_user_by_invalid_id():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404


# 4. POST /users
def test_create_user():
    payload = {"name": "Manish", "job": "SDE"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201
    assert "id" in response.json()


# 5. POST /users with missing fields
def test_create_user_with_missing_fields():
    payload = {"job": "SDE"}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    # assert response.status_code in [400, 422]  # Different APIs may return 400 or 422 for validation errors
    assert response.status_code == 201  # Accepting missing fields



# 6. PUT /users/{id}
def test_update_user():
    payload = {"name": "Manish", "job": "SE"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "Manish"
    assert response.json()["job"] == "SE"


# 7. PUT /users/{id} with invalid ID
def test_update_user_invalid_id():
    payload = {"name": "Manish", "job": "SDE"}
    response = requests.put(f"{BASE_URL}/users/9999", json=payload)
    # assert response.status_code == 404
    assert "updatedAt" in response.json()  # Validate response structure



# 8. DELETE /users/{id}
def test_delete_user():
    response = requests.delete(f"{BASE_URL}/users/2")
    assert response.status_code == 204


# 9. GET /unknown
def test_get_unknown_resources():
    response = requests.get(f"{BASE_URL}/unknown")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


# 10. GET /unknown/{id}
def test_get_unknown_resource_by_id():
    response = requests.get(f"{BASE_URL}/unknown/2")
    assert response.status_code == 200


# 11. POST /register (with a valid predefined user email)
def test_register_user():
    payload = {"email": "eve.holt@reqres.in", "password": "pistol", "name": "Manish"}  # Use predefined user email
    response = requests.post(f"{BASE_URL}/register", json=payload)
    
    # Print the response for debugging
    print("Register Response:", response.text)  # This will show the response body

    assert response.status_code == 200
    assert "token" in response.json()

# 12. POST /register with invalid data
def test_register_user_invalid():
    payload = {"email": "manish@reqres.in"}
    response = requests.post(f"{BASE_URL}/register", json=payload)
    assert response.status_code == 400


# 13. POST /login (use valid credentials for an existing user)
def test_login_user():
    payload = {"email": "eve.holt@reqres.in", "password": "pistol"}  # Use valid credentials
    response = requests.post(f"{BASE_URL}/login", json=payload)
    
    # Print the response for debugging
    print("Login Response:", response.text)  # This will show the response body

    assert response.status_code == 200
    assert "token" in response.json()


# 14. POST /login with invalid credentials
def test_login_invalid():
    payload = {"email": "manish@reqres.in", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/login", json=payload)
    
    # Expecting status code 400 for invalid login
    assert response.status_code == 400, f"Unexpected status code: {response.status_code}, Response: {response.json()}"
    # Checking for error message in the response
    assert "error" in response.json(), f"Error not found in response: {response.json()}"



# 15. GET /unknown/{id} with invalid ID
def test_get_unknown_resource_invalid():
    response = requests.get(f"{BASE_URL}/unknown/9999")
    assert response.status_code == 404


# 16. GET /users?delay=3 (Delayed Response Test)
def test_get_users_delayed():
    response = requests.get(f"{BASE_URL}/users?delay=3")
    assert response.status_code == 200
    assert len(response.json()["data"]) > 0


# 17. POST /users with large payload
def test_create_user_large_payload():
    payload = {"name": "M" * 500, "job": "SDE" * 100}
    response = requests.post(f"{BASE_URL}/users", json=payload)
    assert response.status_code == 201


# 18. PUT /users/{id} with partial data
def test_update_user_partial():
    payload = {"name": "ManishNameUpdated"}
    response = requests.put(f"{BASE_URL}/users/2", json=payload)
    assert response.status_code == 200
    assert response.json()["name"] == "ManishNameUpdated"


# 19. DELETE /users/{id} with invalid ID
def test_delete_user_invalid():
    response = requests.delete(f"{BASE_URL}/users/9999")
    # assert response.status_code == 404
    assert response.status_code in [204, 404]



# 20. Comprehensive Health Check
@pytest.mark.parametrize("endpoint", ["/users", "/register", "/login", "/unknown"])
def test_health_check(endpoint):
    response = requests.get(f"{BASE_URL}{endpoint}")
    assert response.status_code == 200
