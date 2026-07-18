#--------------------------------------------
# AI Engineer Bootcamp
# Day 14
# Program: ---Library  Class---
# Author: Om Roy
# Date: 18-07-2026
#--------------------------------------------

class Book:
    """Represents an individual book in the library."""
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"


class Library:
    """Manages a collection of books."""
    def __init__(self, name: str):
        self.name = name
        self.books = []  # Holds Book objects

    def add_book(self, book: Book):
        """Adds a new Book instance to the library catalog."""
        self.books.append(book)
        print(f"Added: {book.title}")

    def list_available_books(self):
        """Prints all books currently available to borrow."""
        print(f"\n--- Available Books at {self.name} ---")
        available = [b for b in self.books if not b.is_borrowed]
        if not available:
            print("No books available.")
        for book in available:
            print(f"- {book.title} by {book.author}")

    def borrow_book(self, title: str) -> bool:
        """Lends a book out if it exists and is available."""
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have successfully borrowed '{book.title}'.")
                return True
        print(f"Sorry, '{title}' is unavailable or does not exist.")
        return False


# --- How to use it ---
if __name__ == "__main__":
    # Create the library
    my_city_library = Library("Central Library")

    # Add books
    my_city_library.add_book(Book("The Hobbit", "J.R.R. Tolkien"))
    my_city_library.add_book(Book("1984", "George Orwell"))

    # View and borrow books
    my_city_library.list_available_books()
    my_city_library.borrow_book("1984")
    my_city_library.list_available_books()
