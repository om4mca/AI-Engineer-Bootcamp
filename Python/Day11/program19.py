#--------------------------------------------
# AI Engineer Bootcamp
# Day 11
# Program: Feedback Collector
# Author: Om Roy
# Date: 14-07-2026
#--------------------------------------------
from datetime import datetime
import os

class DuplicateFeedbackError(Exception):
    """Raised when a user attempts to log multiple feedbacks for the same ID."""
    pass

class FeedbackNotFoundError(Exception):
    """Raised when looking up feedback statistics for a non-existent customer ID."""
    pass

class InvalidFeedbackDataError(Exception):
    """Raised when entry parameters fail validation checks (e.g., ratings outside range 1-5)."""
    pass


class FeedbackCollector:
    FILE_NAME = "feedback.txt"
    VALID_DOMAINS = ["Performance", "UI/UX", "Billing", "Customer Support", "Features"]

    @classmethod
    def add_and_save_feedback(cls, customer_id, rating_input, domain, review_text):
        # 1. Input Sanitization
        customer_id = str(customer_id).strip().lower()
        domain = str(domain).strip().title()
        review_text = str(review_text).strip()

        # 2. Assert Boundary Validations
        if not customer_id or not domain or not review_text or not rating_input:
            raise InvalidFeedbackDataError("Validation Error: All inputs (ID, Rating, Category, Review) are mandatory.")

        # Customer ID Check (Simple alphanumeric user handle or email validation format)
        if len(customer_id) < 3 or "@" not in customer_id:
            raise InvalidFeedbackDataError("Customer ID Error: Please enter a valid identifier (e.g., your email user@domain.com).")

        # Rating Check
        try:
            rating = int(rating_input)
            if rating < 1 or rating > 5:
                raise ValueError()
        except ValueError:
            raise InvalidFeedbackDataError("Rating Range Error: Score must be an integer between 1 and 5.")

        # Domain/Category Check
        if domain not in cls.VALID_DOMAINS:
            allowed = ", ".join(cls.VALID_DOMAINS)
            raise InvalidFeedbackDataError(f"Domain Error: Domain must match one of: [{allowed}].")

        # Protect file structure integrity by escaping parsing delimiter pipes and newlines
        review_text = review_text.replace("|", "-").replace("\n", " ")

        # 3. Check for Duplicate Submission
        if cls._id_exists(customer_id):
            raise DuplicateFeedbackError(f"Submission Limit: Customer '{customer_id}' has already registered their feedback.")

        # 4. Generate timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

        # 5. Commit record to storage
        record_line = f"{customer_id}|{rating}|{domain}|{timestamp}|{review_text}\n"
        try:
            with open(cls.FILE_NAME, "a", encoding="utf-8") as file:
                file.write(record_line)
            print(f"\n[Success]: Feedback recorded for '{customer_id}' under {domain}.")
        except IOError as e:
            print(f"\n[Disk Sync Error]: Unable to append feedback to storage database. Details: {e}")

    @classmethod
    def generate_metrics_summary(cls):
        """Processes logs in real-time to compute analytical operational metrics."""
        records = cls._load_records()
        if not records:
            print("\n[Metrics Summary]: No customer feedback logs registered in the database yet.")
            return

        total_records = len(records)
        rating_sum = 0
        domain_counts = {}
        rating_distribution = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

        for _, rating_str, domain, _, _ in records:
            rating = int(rating_str)
            rating_sum += rating
            rating_distribution[rating] += 1
            domain_counts[domain] = domain_counts.get(domain, 0) + 1

        avg_rating = rating_sum / total_records

        print("\n📈 ====== CUSTOMER METRICS SUMMARY ======")
        print(f" Total Feedback Submissions : {total_records}")
        print(f" Net Average Product Score  : {avg_rating:.2f} / 5.0")
        print("\n--- Rating Breakdown ---")
        for stars in sorted(rating_distribution.keys(), reverse=True):
            bar = "★" * stars + "☆" * (5 - stars)
            percentage = (rating_distribution[stars] / total_records) * 100
            print(f" {bar} ({stars} Stars) : {rating_distribution[stars]} review(s) ({percentage:.1f}%)")
            
        print("\n--- Domain Distribution ---")
        for dom, count in domain_counts.items():
            percentage = (count / total_records) * 100
            print(f" -> {dom:<18} : {count:<3} record(s) ({percentage:.1f}%)")
        print("=" * 40)

    @classmethod
    def find_user_review(cls, target_id):
        target_id = target_id.strip().lower()
        records = cls._load_records()

        for customer_id, rating, domain, timestamp, review in records:
            if customer_id == target_id:
                print(f"\n🔍 [Feedback Entry Found for: {target_id}]")
                print(f" -> Date Logged     : {timestamp}")
                print(f" -> Feature Domain  : {domain}")
                print(f" -> Assigned Rating : {'★' * int(rating)}")
                print(f"\n--- Customer Review Text ---")
                print(review)
                print("-" * 40)
                return

        raise FeedbackNotFoundError(f"Lookup Failed: No recorded feedback located for customer ID '{target_id}'.")

    # --- Safe Storage Core Intersections ---
    @classmethod
    def _load_records(cls):
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
            print(f"[Critical System Error]: Cannot parse database storage system. {e}")
            
        return parsed_records

    @classmethod
    def _id_exists(cls, check_id):
        records = cls._load_records()
        return any(cid == check_id for cid, *rest in records)


def main():
    print("=== Quality Assurance Feedback Engine ===")
    
    while True:
        print("\n" + "="*35)
        print("         FEEDBACK TERMINAL")
        print("="*35)
        print("1. Submit Customer Feedback")
        print("2. Compile Sentiment & Score Metrics")
        print("3. Query Customer Review by Email ID")
        print("4. Exit Terminal Session")
        print("="*35)
        
        choice = input("Enter choice (1-4): ").strip()

        try:
            if choice == "1":
                cid = input("Enter Customer Email ID: ")
                print(f"Eligible Product Domains: {', '.join(FeedbackCollector.VALID_DOMAINS)}")
                domain = input("Select Target Product Domain: ")
                rating_score = input("Input Customer Rating Score (1-5): ")
                review = input("Input Written Feedback Text:\n> ")
                FeedbackCollector.add_and_save_feedback(cid, rating_score, domain, review)

            elif choice == "2":
                FeedbackCollector.generate_metrics_summary()

            elif choice == "3":
                target_email = input("Enter Target Customer Email to Query: ")
                FeedbackCollector.find_user_review(target_email)

            elif choice == "4":
                print("\nFeedback collector safely shut down. Metrics metrics synced.")
                break
            else:
                print("\n[Input Error]: Please supply an active digit path (1-4).")

        except InvalidFeedbackDataError as e:
            print(f"\n🚨 [Data Validation Failed]: {e}")
            
        except DuplicateFeedbackError as e:
            print(f"\n🚨 [User Limit Restriction]: {e}")
            
        except FeedbackNotFoundError as e:
            print(f"\n🚨 [Search Miss]: {e}")
            
        except Exception as e:
            print(f"\n🚨 [Platform System Interruption]: {e}")
            
        finally:
            print("\n" + "-"*40)


if __name__ == "__main__":
    main()