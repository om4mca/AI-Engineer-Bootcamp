import csv
import json
import os
from contextlib import contextmanager

from exceptions import DataValidationError, FileProcessingError
from decorators import log_execution_time, retry

# --- 1. OOP: Domain Data Model ---
class Record:
    def __init__(self, record_id, user, status, amount):
        self.id = record_id
        self.user = user
        self.status = status.lower()
        self.amount = float(amount)

    def validate(self):
        """Raises DataValidationError if record is invalid."""
        if self.amount < 0:
            raise DataValidationError(self.to_dict(), "Amount cannot be negative")
        if not self.user:
            raise DataValidationError(self.to_dict(), "User cannot be empty")

    def to_dict(self):
        return {
            "id": self.id,
            "user": self.user,
            "status": self.status,
            "amount": self.amount
        }

# --- 2. Context Manager + File Handling ---
@contextmanager
def safe_file_writer(filepath):
    """Guarantees file output cleanup and exception isolation."""
    try:
        file = open(filepath, "w")
        yield file
    except OSError as e:
        raise FileProcessingError(f"Could not open file {filepath}: {e}")
    finally:
        file.close()

# --- 3. OOP + Package Management: Data Processor Class ---
class BatchDataProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.stats = {"processed": 0, "failed": 0, "total_amount": 0.0}

    # --- 4. Generator + Line-by-Line File Processing ---
    def stream_raw_records(self):
        """Streams lines from CSV lazily without loading the entire file to RAM."""
        try:
            with open(self.input_file, "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    yield row
        except FileNotFoundError:
            raise FileProcessingError(f"Source file '{self.input_file}' not found.")

    # --- 5. Decorator Integration & Data Transformation ---
    @retry(times=2, delay=0.05, exceptions=(ValueError,))
    def parse_record(self, raw_data):
        """Transforms raw dictionary into a validated Record object."""
        record = Record(
            record_id=raw_data["id"],
            user=raw_data["user"],
            status=raw_data["status"],
            amount=raw_data["amount"]
        )
        record.validate()
        return record

    @log_execution_time
    def run_pipeline(self):
        """Main execution loop chaining all integrated concepts."""
        print(f"🚀 Starting pipeline for '{self.input_file}'...\n")
        
        valid_records = []

        # Consume the generator stream
        for raw_row in self.stream_raw_records():
            try:
                # Function + Class + Exception Validation
                record = self.parse_record(raw_row)
                valid_records.append(record.to_dict())  # List + Dictionary integration
                
                # Update aggregated stats
                self.stats["processed"] += 1
                self.stats["total_amount"] += record.amount

            except DataValidationError as e:
                print(f"❌ Skipped Record: {e}")
                self.stats["failed"] += 1
            except Exception as e:
                print(f"⚠️ Unexpected Error on row {raw_row}: {e}")
                self.stats["failed"] += 1

        # Save processed results safely using Custom Context Manager
        with safe_file_writer(self.output_file) as out_file:
            output_payload = {
                "summary": self.stats,
                "data": valid_records
            }
            json.dump(output_payload, out_file, indent=4)

        print(f"\n✅ Pipeline Complete! Output saved to '{self.output_file}'")
        print(f"📊 Stats: {self.stats}")


# --- Demonstration Run ---
if __name__ == "__main__":
    # Setup dummy CSV input file for demonstration
    sample_csv = "transactions.csv"
    output_json = "processed_summary.json"

    with open(sample_csv, "w") as f:
        f.write("id,user,status,amount\n")
        f.write("101,Om,completed,150.50\n")
        f.write("102,Sudhir,pending,-20.00\n")       # Invalid amount -> raises DataValidationError
        f.write("103,,completed,99.99\n")           # Missing user   -> raises DataValidationError
        f.write("104,Subodh,completed,450.00\n")

    # Run the application
    processor = BatchDataProcessor(sample_csv, output_json)
    processor.run_pipeline()

    # Cleanup demo input file
    if os.path.exists(sample_csv):
        os.remove(sample_csv)