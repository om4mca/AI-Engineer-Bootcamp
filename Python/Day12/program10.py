#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Book Class
# Author: Om Roy
# Date: 12-07-2026
#--------------------------------------------

class Book:
    def __init__(self, isbn: str, title: str, author: str, total_pages: int):
        """Initializes a library book catalog profile."""
        self.isbn = isbn
        self.title = title
        self.author = author
        self.total_pages = total_pages
        
        # Track active usage states
        self.is_checked_out = False
        self.current_page = 0

    def display_info(self):
        """Prints the book's current metadata and availability status."""
        status = "Checked Out ❌" if self.is_checked_out else "Available on Shelf 📜"
        print(f"\n--- Book Cataloging Info ---")
        print(f"Title:        {self.title}")
        print(f"Author:       {self.author}")
        print(f"ISBN Reference: {self.isbn}")
        print(f"Length:       {self.total_pages} pages")
        print(f"Status:       {status}")
        if self.current_page > 0:
            progress = (self.current_page / self.total_pages) * 100
            print(f"Reading Track: Page {self.current_page}/{self.total_pages} ({progress:.1f}% read)")

    def check_out(self):
        """Borrows the book from the system library."""
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"[Library System] Success! '{self.title}' has been checked out.")
        else:
            print(f"[Library Alert] Sorry, '{self.title}' is already checked out by another borrower.")

    def return_book(self):
        """Returns the book back to the library shelf resource."""
        if self.is_checked_out:
            self.is_checked_out = False
            self.current_page = 0  # Reset reading bookmark progress
            print(f"[Library System] '{self.title}' has been successfully returned.")
        else:
            print("[Library Warning] This book is already sitting in the database as available.")

    def update_reading_progress(self, page: int):
        """Saves your current page bookmark location."""
        if not self.is_checked_out:
            print("[System Error] You must check out the book before tracking reading pages!")
            return

        if 0 <= page <= self.total_pages:
            self.current_page = page
            print(f"[Bookmark Logged] Progress updated for '{self.title}'.")
        else:
            print(f"[Error] Invalid page context. Value must map between 0 and {self.total_pages}.")


# --- Demonstration Workflow ---
if __name__ == "__main__":
    print("Opening Digital Library Catalog Archive...")

    # Instantiating various standard Book object records
    book1 = Book("978-0141439517", "Pride and Prejudice", "Jane Austen", 432)
    book2 = Book("978-0743273565", "The Great Gatsby", "F. Scott Fitzgerald", 180)

    # Reviewing initial status configurations
    book1.display_info()

    print("\n" + "="*40 + "\nSimulating Reader Borrowing Interactions...")

    # Running safe logical system sequences
    book1.check_out()
    book1.update_reading_progress(120)  # Reading roughly a quarter of the book
    
    # Check updated live profile information tracking
    book1.display_info()

    print("\n" + "="*40 + "\nTesting Library Rule Enforcement...")
    book2.update_reading_progress(50)  # Should error since it hasn't been checked out yet
    book1.check_out()                  # Should error out as duplicate checkout

    # Returning items cleanly
    print("\n" + "="*40 + "\nReturning Inventory...")
    book1.return_book()
    book1.display_info()