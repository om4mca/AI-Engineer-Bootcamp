#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Library Class
# Author: Om Roy
# Date: 15-07-2026
#--------------------------------------------

class Book:
    """Represents a unique book asset in the catalog collection."""
    def __init__(self, isbn: str, title: str, author: str):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.is_available = True

    def get_summary(self) -> str:
        status = "Available 📜" if self.is_available else "Checked Out ❌"
        return f"  [{self.isbn}] '{self.title}' by {self.author} | Status: {status}"


class Library:
    def __init__(self, library_name: str):
        """Initializes a master digital library collection manager."""
        self.library_name = library_name
        # Core storage dictionary mapping ISBN string -> Book object record
        self.catalog = {}

    def add_book(self, book: Book):
        """Registers a new Book object asset into the library archive system."""
        if book.isbn in self.catalog:
            print(f"[Archive Alert] ISBN {book.isbn} already matches an existing catalog item.")
        else:
            self.catalog[book.isbn] = book
            print(f"[Catalog Sync] Successfully indexed: '{book.title}'")

    def loan_book(self, isbn: str):
        """Processes a checkout request, mutating state flags on the targeted Book object."""
        if isbn not in self.catalog:
            print(f"[Transaction Refused] Request failed: ISBN {isbn} does not exist in our system.")
            return

        target_book = self.catalog[isbn]
        if target_book.is_available:
            target_book.is_available = False
            print(f"[Success] Enjoy your reading! '{target_book.title}' has been checked out.")
        else:
            print(f"[Transaction Refused] Sorry, '{target_book.title}' is currently checked out.")

    def return_book(self, isbn: str):
        """Restores a book asset's availability inside the catalogue."""
        if isbn in self.catalog:
            target_book = self.catalog[isbn]
            if not target_book.is_available:
                target_book.is_available = True
                print(f"[Success] Inventory restored. '{target_book.title}' is back on the shelf.")
            else:
                print(f"[Warning] Anomalous log: '{target_book.title}' was already marked as available.")
        else:
            print(f"[Error] Return failed: ISBN {isbn} does not map to this library infrastructure.")

    def search_by_author(self, author_name: str):
        """Filters the entire registry, displaying match patterns for a chosen author."""
        print(f"\n--- Search Results for Author: '{author_name}' ---")
        matches_found = False
        
        # Iterating through the collection dictionary values
        for book in self.catalog.values():
            if author_name.lower() in book.author.lower():
                print(book.get_summary())
                matches_found = True
                
        if not matches_found:
            print(f"  No catalog items matched author string parameters.")

    def display_entire_collection(self):
        """Prints the full index state matrix of the current collection framework."""
        print(f"\n{"="*15} {self.library_name} System Census {"="*15}")
        if not self.catalog:
            print("  The library catalog database is currently empty.")
            return
            
        for book in self.catalog.values():
            print(book.get_summary())
        print(f"Total Unique Titles Maintained: {len(self.catalog)}")
        print("="*55)


# --- System Integration Simulation ---
if __name__ == "__main__":
    print("Connecting to central metadata book catalog mainframe...\n")

    # 1. Instantiate the master Library controller entity
    metro_library = Library("City Central Public Library")

    # 2. Instantiate individual standalone Book objects
    b1 = Book("978-0141439517", "Pride and Prejudice", "Jane Austen")
    b2 = Book("978-0743273565", "The Great Gatsby", "F. Scott Fitzgerald")
    b3 = Book("978-0451524935", "1844", "George Orwell")

    print("--- Phase 1: populating Catalog Datastores ---")
    # 3. Passing standalone objects directly into the collection manager class
    metro_library.add_book(b1)
    metro_library.add_book(b2)
    metro_library.add_book(b3)

    # 4. Output baseline state profile mapping
    metro_library.display_entire_collection()

    print("\n--- Phase 2: Processing Borrowing Transactions ---")
    # 5. Executing state adjustments through key lookups
    metro_library.loan_book("978-0743273565") # Checking out Gatsby
    metro_library.loan_book("978-0743273565") # Intentionally running duplicate checkout block rules
    
    # 6. Checking inventory state preservation values
    metro_library.display_entire_collection()

    print("\n--- Phase 3: Executing Query Filters ---")
    # 7. Running structural loop filter functions
    metro_library.search_by_author("Austen")
    
    print("\n--- Phase 4: Closing Material Circulation Loops ---")
    # 8. Returning item assets back to default parameters cleanly
    metro_library.return_book("978-0743273565")
    metro_library.display_entire_collection()