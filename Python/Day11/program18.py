#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Diary App
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------
from datetime import datetime
import os

class DuplicateEntryError(Exception):
    """Raised when trying to write an entry for a date that already has a log."""
    pass

class EntryNotFoundError(Exception):
    """Raised when searching for a diary entry date that does not exist."""
    pass

class InvalidDiaryDataError(Exception):
    """Raised when diary input values violate validation or emotional mood structures."""
    pass


class DiaryManager:
    FILE_NAME = "diary.txt"
    # Mood mapping for emotional tagging
    VALID_MOODS = {
        "1": "Happy 😊",
        "2": "Calm 😌",
        "3": "Productive 💪",
        "4": "Anxious 😟",
        "5": "Tired 😴"
    }

    @classmethod
    def add_and_save_entry(cls, date_str, mood_key, theme, content):
        # 1. Date normalization and validation
        date_str = date_str.strip()
        if not date_str:
            # Fall back to today's date if left blank
            date_str = datetime.now().strftime("%Y-%m-%d")
        else:
            try:
                # Ensure the user entered a valid ISO date
                parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
                date_str = parsed_date.strftime("%Y-%m-%d")
            except ValueError:
                raise InvalidDiaryDataError("Date Format Error: Date must use the YYYY-MM-DD template.")

        # 2. Mood & textual validations
        if mood_key not in cls.VALID_MOODS:
            raise InvalidDiaryDataError("Mood Selection Error: Please choose a valid index representing your mood.")
        
        mood_label = cls.VALID_MOODS[mood_key]
        theme = str(theme).strip().title()
        content = str(content).strip()

        if not theme or not content:
            raise InvalidDiaryDataError("All entry components (Theme, Content) are required to commit a log.")

        # Replace pipe delimiters to protect file format parsing alignment
        theme = theme.replace("|", "-")
        content = content.replace("|", "-").replace("\n", " ")

        # 3. Prevent overwriting a previous entry for the same calendar date
        if cls._date_exists(date_str):
            raise DuplicateEntryError(f"Timeline Overwrite Blocked: An entry already exists for {date_str}.")

        # 4. Save to flat file database
        record_line = f"{date_str}|{mood_label}|{theme}|{content}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Journal successfully locked on {date_str} under mood: {mood_label}.")
        except IOError as e:
            print(f"\n[Disk Storage Error]: Unable to record entry. Details: {e}")

    @classmethod
    def display_all_entries(cls):
        records = cls._load_records()
        if not records:
            print("\n[Diary Status]: Your journal history is currently blank.")
            return

        # Sort chronological records by date (descending - newest first)
        records.sort(key=lambda x: x[0], reverse=True)

        print("\n📔 === PERSONAL DIARY INDEX ===")
        print(f"{'Date':<12} | {'Mood State':<12} | {'Core Theme'}")
        print("-" * 55)
        for date, mood, theme, _ in records:
            print(f"{date:<12} | {mood:<12} | {theme}")
        print("=" * 55)

    @classmethod
    def search_entry_by_date(cls, search_date):
        search_date = search_date.strip()
        try:
            # Normalize target search date
            parsed_search = datetime.strptime(search_date, "%Y-%m-%d")
            search_date = parsed_search.strftime("%Y-%m-%d")
        except ValueError:
            raise InvalidDiaryDataError("Search Format Error: Date must follow YYYY-MM-DD formatting.")

        records = cls._load_records()
        for date, mood, theme, content in records:
            if date == search_date:
                print(f"\n📖 [Diary Entry Opened: {search_date}]")
                print(f" -> Mood Reflection : {mood}")
                print(f" -> Core Theme      : {theme}")
                print(f"\n--- Personal Thoughts ---")
                print(content)
                print("-" * 35)
                return

        raise EntryNotFoundError(f"No diary entry exists for the date: {search_date}.")

    # --- Secure Internal Helpers ---
    @classmethod
    def _load_records(cls):
        """Safely loads flat-file pipe-delimited diary logs into memory."""
        if not os.path.exists(cls.FILE_NAME):
            return []

        parsed_records = []
        try:
            with open(cls.FILE_NAME, "r", encoding="utf-8") as file:
                for line in file:
                    cleaned = line.strip()
                    if cleaned:
                        parts = cleaned.split("|")
                        if len(parts) == 4:
                            parsed_records.append(parts)
        except IOError as e:
            print(f"[Critical System Error]: Cannot parse journal files. {e}")
            
        return parsed_records

    @classmethod
    def _date_exists(cls, check_date):
        records = cls._load_records()
        return any(date == check_date for date, *rest in records)


def main():
    print("=== Secure Personal Diary Vault ===")
    
    while True:
        print("\n" + "="*35)
        print("          DIARY PORTAL")
        print("="*35)
        print("1. Write New Diary Entry")
        print("2. Display Chronological History")
        print("3. Read Full Entry by Date")
        print("4. Lock Vault & Exit")
        print("="*35)
        
        choice = input("Select command (1-4): ").strip()

        try:
            if choice == "1":
                print("\nPress [Enter] for today's system date.")
                date_input = input("Enter Date (YYYY-MM-DD): ")
                
                print("\nHow is your emotional headspace today?")
                for key, val in DiaryManager.VALID_MOODS.items():
                    print(f"  {key}. {val}")
                mood_input = input("Select Mood (1-5): ").strip()
                
                theme_input = input("Enter Core Theme of the Day: ")
                content_input = input("Pen down your reflection:\n> ")
                DiaryManager.add_and_save_entry(date_input, mood_input, theme_input, content_input)

            elif choice == "2":
                DiaryManager.display_all_entries()

            elif choice == "3":
                date_search = input("Enter Target Date to Read (YYYY-MM-DD): ")
                DiaryManager.search_entry_by_date(date_search)

            elif choice == "4":
                print("\nDiary Vault locked and encrypted. Sleep well!")
                break
            else:
                print("\n[Input Error]: Select a valid path command (1-4).")

        except InvalidDiaryDataError as e:
            print(f"\n🚨 [Validation Exception]: {e}")
            
        except DuplicateEntryError as e:
            print(f"\n🚨 [Timeline Conflict]: {e}")
            
        except EntryNotFoundError as e:
            print(f"\n🚨 [Search Fault]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [System Error]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()