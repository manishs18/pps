from selenium import webdriver
from selenium.webdriver.common.by import By
import time

optional = webdriver.EdgeOptions()
driver = webdriver.Edge(options=optional)
driver.maximize_window()
driver.get('https://www.saucedemo.com/')

time.sleep(2)
username = driver.find_element(By.NAME, "user-name")
username.send_keys("standard_user")

time.sleep(2)

password = driver.find_element(By.NAME, "password")
password.send_keys("secret_sauce")

time.sleep(2)
login = driver.find_element(By.NAME, "login-button")
login.click()

time.sleep(2)
addCart = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
addCart.click()

time.sleep(2) 
cart = driver.find_element(By.XPATH, "//a[@class='shopping_cart_link']")
cart.click()

checkout = driver.find_element(By.NAME, "checkout")
checkout.click()

time.sleep(2)
firstname = driver.find_element(By.NAME, "firstName")
firstname.send_keys("Manish")

time.sleep(2)
lastname = driver.find_element(By.NAME, "lastName")
lastname.send_keys("Shrestha")

time.sleep(2)
postalcode = driver.find_element(By.NAME, "postalCode")
postalcode.send_keys("123564")

time.sleep(2)
cont = driver.find_element(By.XPATH, "//input[@id='continue']")
cont.click()

time.sleep(2)
finish = driver.find_element(By.NAME, "finish")
finish.click()
time.sleep(2)

driver.quit()












































'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Reusable login function
def login(driver, username="standard_user", password="secret_sauce"):
    """Logs in with provided credentials"""
    try:
        driver.get('https://www.saucedemo.com/')
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "user-name")))
        
        driver.find_element(By.NAME, "user-name").send_keys(username)
        driver.find_element(By.NAME, "password").send_keys(password)
        driver.find_element(By.NAME, "login-button").click()
        
        WebDriverWait(driver, 10).until(EC.url_to_be('https://www.saucedemo.com/inventory.html'))
    except Exception as e:
        print(f"Login failed: {e}")

# Reusable function to add an item to the cart
def add_item_to_cart(driver, item_name="sauce-labs-backpack"):
    """Adds an item to the cart"""
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, f"add-to-cart-{item_name}")))
        driver.find_element(By.NAME, f"add-to-cart-{item_name}").click()
    except Exception as e:
        print(f"Failed to add item to cart: {e}")

# Reusable checkout function
def checkout(driver, firstname="John", lastname="Doe", postalcode="123456"):
    """Proceeds with the checkout process"""
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "checkout")))
        driver.find_element(By.NAME, "checkout").click()

        driver.find_element(By.NAME, "firstName").send_keys(firstname)
        driver.find_element(By.NAME, "lastName").send_keys(lastname)
        driver.find_element(By.NAME, "postalCode").send_keys(postalcode)

        driver.find_element(By.XPATH, "//input[@id='continue']").click()
        driver.find_element(By.NAME, "finish").click()
    except Exception as e:
        print(f"Checkout failed: {e}")

'''



































































































































'''
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.EdgeOptions()
driver = webdriver.Edge(options=options)  
driver.maximize_window()

driver.get('https://ogmt.koyeb.app/')

time.sleep(2)

signin= driver.find_element(By.XPATH, value='//button[@class="btn btn-primary mx-1"]')
signin.click()
time.sleep(4)

username = driver.find_element(By.ID, "loginusername")
username.send_keys("mkuma")
time.sleep(3)

password = driver.find_element(By.ID, "loginpassword")
password.send_keys("admin123")
time.sleep(3)

submit = driver.find_element(By.ID, "gridCheck1")
submit.click()
time.sleep(3)

login= driver.find_element(By.XPATH, value='//button[@class="btn btn-success"]')
login.click()
time.sleep(3)

driver.quit()


'''



























































'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AuthValidation:
    def __init__(self):
        """Initialize the WebDriver."""
        options = webdriver.EdgeOptions()
        self.driver = webdriver.Edge(options=options)
        self.driver.maximize_window()

    def open_app(self, url):
        """Open the application URL."""
        self.driver.get(url)

    def login(self, username, password):
        """Perform login with provided credentials."""
        # Click on the Sign In button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-primary mx-1"]'))
        ).click()

        # Enter username
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginusername"))
        ).send_keys(username)

        # Enter password
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "loginpassword"))
        ).send_keys(password)

        # Click the "Remember Me" checkbox
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "gridCheck1"))
        ).click()

        # Click on the Login button
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[@class="btn btn-success"]'))
        ).click()

    def is_logged_in(self):
        """Check if login was successful."""
        try:
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.ID, "dashboard"))  # Update with an actual post-login element
            )
            return True
        except:
            return False

    def close_app(self):
        """Close the browser."""
        self.driver.quit()

        '''