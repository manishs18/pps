library_data = {
    "To Kill a Mockingbird": {"author": "Harper Lee", "genre": "Fiction"},
    "Moby Dick": {"author": "Herman Melville", "genre": "Adventure"},
    "Pride and Prejudice": {"author": "Jane Austen", "genre": "Romance"},
    "The Lord of the Rings": {"author": "J.R.R. Tolkien", "genre": "Fantasy"},
}

borrowed_books = set()

def search_book(title):
    if title in library_data:
        return library_data[title]
    raise KeyError(f"Book '{title}' not found.")

def borrow_book(title):
    if title in borrowed_books:
        raise ValueError(f"Book '{title}' already borrowed.")
    if title not in library_data:
        raise ValueError(f"Book '{title}' not in library.")
    borrowed_books.add(title)

def return_book(title):
    if title not in borrowed_books:
        raise ValueError(f"Book '{title}' not borrowed.")
    borrowed_books.remove(title)

if __name__ == "__main__":
    try:
        print(search_book("To Kill a Mockingbird"))
        print(search_book("The Hobbit"))  
    except KeyError as e:
        print(e)

    try:
        borrow_book("Moby Dick")
        print(f"Borrowed: {borrowed_books}")
        borrow_book("Moby Dick")  
    except ValueError as e:
        print(e)

    try:
        return_book("Moby Dick")
        print(f"Borrowed after return: {borrowed_books}")
        return_book("Moby Dick")  
    except ValueError as e:
        print(e)
