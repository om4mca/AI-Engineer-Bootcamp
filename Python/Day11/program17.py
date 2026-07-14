#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Notes App
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------

from datetime import datetime
import os

class DuplicateNoteError(Exception):
    """Raised when trying to save a Note ID that already exists."""
    pass

class NoteNotFoundError(Exception):
    """Raised when a specified Note ID cannot be located."""
    pass

class InvalidNoteDataError(Exception):
    """Raised when incoming note content violates length or formatting constraints."""
    pass


class NotesManager:
    FILE_NAME = "notes.txt"
    VALID_CATEGORIES = ["Work", "Personal", "Ideas", "Todo", "Journal"]

    @classmethod
    def add_and_save_note(cls, note_id, category, title, content):
        # 1. Clean and normalize fields
        note_id = str(note_id).strip().upper()
        category = str(category).strip().title()
        title = str(title).strip()
        content = str(content).strip()

        # 2. Strict Input Boundary Validations
        if not note_id or not category or not title or not content:
            raise InvalidNoteDataError("All entry fields (ID, Category, Title, Content) are strictly mandatory.")

        if not (note_id.startswith("N") and note_id[1:].isdigit()):
            raise InvalidNoteDataError("Format Error: Note ID must start with 'N' followed by digits (e.g., N01).")

        if category not in cls.VALID_CATEGORIES:
            allowed = ", ".join(cls.VALID_CATEGORIES)
            raise InvalidNoteDataError(f"Category Error: Category must be one of: [{allowed}].")

        # Replace vertical pipes in user text to preserve database storage delimiters
        title = title.replace("|", "-")
        content = content.replace("|", "-").replace("\n", " ")

        if len(content) > 500:
            raise InvalidNoteDataError("Length Error: Note content cannot exceed 500 characters.")

        # 3. Ensure ID Uniqueness
        if cls._id_exists(note_id):
            raise DuplicateNoteError(f"Database Conflict: A note with ID '{note_id}' already exists.")

        # 4. Generate metadata timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # 5. Append direct to the flat-file database using pipe separators
        record_line = f"{note_id}|{category}|{timestamp}|{title}|{content}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Note '{title}' saved successfully under ID {note_id}.")
        except IOError as e:
            print(f"\n[File Access Error]: Unable to write note to disk. Details: {e}")

    @classmethod
    def display_all_notes(cls):
        records = cls._load_records()
        if not records:
            print("\n[Notes Status]: Your journal is currently empty.")
            return

        print("\n📔 === SAVED NOTES DIRECTORY ===")
        print(f"{'ID':<6} | {'Category':<10} | {'Created At':<16} | {'Title'}")
        print("-" * 65)
        for nid, cat, timestamp, title, _ in records:
            print(f"{nid:<6} | {cat:<10} | {timestamp:<16} | {title}")
        print("=" * 65)

    @classmethod
    def search_note(cls, search_id):
        search_id = str(search_id).strip().upper()
        records = cls._load_records()

        for nid, cat, timestamp, title, content in records:
            if nid == search_id:
                print(f"\n🎯 [Note Opened: {search_id}]")
                print(f" -> Category  : {cat}")
                print(f" -> Created   : {timestamp}")
                print(f" -> Title     : {title}")
                print(f"\n--- Content ---")
                print(content)
                print("---------------")
                return
                
        raise NoteNotFoundError(f"Lookup Failed: Note ID '{search_id}' does not exist.")

    # --- Secure Internal Helpers ---
    @classmethod
    def _load_records(cls):
        """Safely loads flat-file pipe-delimited notes into memory-efficient lists."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned = line.strip()
                    if cleaned:
                        parts = cleaned.split("|")
                        if len(parts) == 5:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical System Error]: Cannot parse notebook file. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        records = cls._load_records()
        return any(nid == check_id for nid, *rest in records)


def main():
    print("=== Personal Secure Notes Engine ===")
    
    while True:
        print("\n" + "="*35)
        print("          NOTEBOOK MENU")
        print("="*35)
        print("1. Create & Save New Note")
        print("2. Display Saved Notes List")
        print("3. View Full Note by ID")
        print("4. Close Notebook Application")
        print("="*35)
        
        choice = input("Select choice (1-4): ").strip()

        try:
            if choice == "1":
                nid = input("Enter Note ID (e.g. N01): ")
                print(f"Valid Categories: {', '.join(NotesManager.VALID_CATEGORIES)}")
                category = input("Enter Note Category: ")
                title = input("Enter Note Title: ")
                content = input("Enter Note Content (Max 500 chars): ")
                NotesManager.add_and_save_note(nid, category, title, content)

            elif choice == "2":
                NotesManager.display_all_notes()

            elif choice == "3":
                search_id = input("Enter Note ID to read: ")
                NotesManager.search_note(search_id)

            elif choice == "4":
                print("\nNotebook closed securely. All notes synced to local storage.")
                break
            else:
                print("\n[Input Error]: Please enter a choice between 1 and 4.")

        except InvalidNoteDataError as e:
            print(f"\n🚨 [Policy Violation]: {e}")
            
        except DuplicateNoteError as e:
            print(f"\n🚨 [ID Conflict]: {e}")
            
        except NoteNotFoundError as e:
            print(f"\n🚨 [Search Failure]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Unexpected System Exception]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()