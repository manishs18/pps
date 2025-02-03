# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time

# nikhil =webdriver.EdgeOptions()
# avinash = webdriver.Edge(options=nikhil)
# avinash.get("https://rahulshettyacademy.com/AutomationPractice/")
# avinash.maximize_window()
# time.sleep(2)

# parent_checkbox= avinash.find_elements(By.XPATH, value="//input[@type='checkbox']")
# time.sleep(2)

# for i in parent_checkbox:
#     if i == parent_checkbox[1]:
#         i.click()
# time.sleep(2)



# Library data
library_data = {
    "To Kill a Mockingbird": {"author": "Harper Lee", "genre": "Fiction"},
    "Moby Dick": {"author": "Herman Melville", "genre": "Adventure"},
    "Pride and Prejudice": {"author": "Jane Austen", "genre": "Romance"},
    "The Lord of the Rings": {"author": "J.R.R. Tolkien", "genre": "Fantasy"},
}

# Set to keep track of borrowed books
borrowed_books = set()

# Function to search for a book by its title in the library data
def search_book(title):
    try:
        # Try to find the book in the library data
        book_info = library_data[title]
        return book_info
    except KeyError:
        # Raise a KeyError if the book is not found
        raise KeyError(f"Book '{title}' not found in the library.")

# Function to borrow a book by its title
def borrow_book(title):
    try:
        # Check if the book is already borrowed
        if title in borrowed_books:
            raise ValueError(f"Book '{title}' is already borrowed.")
        
        # Check if the book exists in the library
        if title not in library_data:
            raise ValueError(f"Book '{title}' not available in the library.")
        
        # Add the book to the borrowed_books set
        borrowed_books.add(title)
    except ValueError as ve:
        # Catch and raise ValueError for borrowing issues
        raise ve
    finally:
        # Optional: log or clean up if necessary (not used here)
        pass

# Function to return a borrowed book by its title
def return_book(title):
    try:
        # Check if the book was borrowed
        if title not in borrowed_books:
            raise ValueError(f"Book '{title}' was not borrowed.")
        
        # Remove the book from the borrowed_books set
        borrowed_books.remove(title)
    except ValueError as ve:
        # Catch and raise ValueError for return issues
        raise ve
    finally:
        # Optional: log or clean up if necessary (not used here)
        pass