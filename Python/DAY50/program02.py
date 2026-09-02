import abc
import logging
from typing import Any, Dict, List, Optional

# Logging setup for production tracking
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


# ==========================================
# 1. Custom Exception Hierarchy
# ==========================================
class BasePipelineException(Exception):
    """System ki sabhi exceptions ki Base Exception class."""

    pass


class ValidationError(BasePipelineException):
    """Jab input data validation rules pass na kare."""

    def __init__(self, message: str, invalid_value: Any):
        super().__init__(f"{message} (Received: {invalid_value})")
        self.invalid_value = invalid_value


class ProcessingError(BasePipelineException):
    """Data processing runtime exceptions ke liye."""

    pass


class RollbackException(BasePipelineException):
    """Jab state rollback trigger hota hai."""

    pass


# ==========================================
# 2. Context Manager for Safe State Rollback
# ==========================================
class TransactionalState:
    """Context Manager jo state changes ko monitor karta hai.

    Failure ke case me state rollback guarantee karta hai.
    """

    def __init__(self, target_object: "BaseDataRepository"):
        self.target = target_object
        self._backup_data: List[Dict[str, Any]] = []

    def __enter__(self):
        # Create a deep copy backup of current state
        self._backup_data = [item.copy() for item in self.target.data_store]
        logging.info("Transaction Started: State backup created.")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            # Exception occurred -> Restore previous state
            self.target.data_store = self._backup_data
            logging.error(
                f"Transaction Failed ({exc_type.__name__}: {exc_val}). Rolling back state..."
            )
            # Suppress exception after logging/handling if needed, or re-raise custom error
            raise RollbackException(
                f"State restored due to internal failure: {exc_val}"
            ) from exc_val
        logging.info("Transaction Committed Successfully.")
        return True


# ==========================================
# 3. Abstract Base Classes (OOP Architecture)
# ==========================================
class BaseDataRepository(abc.ABC):

    def __init__(self):
        self.data_store: List[Dict[str, Any]] = []

    @abc.abstractmethod
    def add_record(self, record: Dict[str, Any]) -> None:
        """Abstract method for record ingestion."""
        pass

    @abc.abstractmethod
    def validate_record(self, record: Dict[str, Any]) -> bool:
        """Abstract method for business rule validation."""
        pass


class DataProcessorPipeline(BaseDataRepository):

    def validate_record(self, record: Dict[str, Any]) -> bool:
        """Validation rules:

        1. Record must be a dictionary. 2. Must contain 'id' (int) and
        'score' (float/int). 3. Score must be between 0 and 100.
        """
        if not isinstance(record, dict):
            raise ValidationError("Record must be a dictionary", record)

        if "id" not in record or "score" not in record:
            raise ValidationError("Missing required keys ('id', 'score')", record)

        score = record["score"]
        if not isinstance(score, (int, float)):
            raise ValidationError("Score must be numeric", score)

        if not (0 <= score <= 100):
            raise ValidationError("Score out of boundary [0-100]", score)

        return True

    def add_record(self, record: Dict[str, Any]) -> None:
        """Validates and adds a single record."""
        self.validate_record(record)
        self.data_store.append(record)

    def batch_process(self, batch: List[Dict[str, Any]]) -> None:
        """Atomic batch insertion using Transactional Context Manager."""
        with TransactionalState(self):
            for record in batch:
                # Simulating dynamic failure rule
                if record.get("trigger_crash"):
                    raise ProcessingError(
                        "Simulated critical database connection drop!"
                    )
                self.add_record(record)


# ==========================================
# 4. Driver / Demonstration Code
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("     OOP + EXCEPTION INTEGRATION SYSTEM     ")
    print("============================================\n")

    pipeline = DataProcessorPipeline()

    # --- Test 1: Successful Batch Ingestion ---
    print("--- [Test 1] Executing Valid Batch Ingestion ---")
    valid_batch = [
        {"id": 101, "score": 88.5},
        {"id": 102, "score": 92.0},
        {"id": 103, "score": 75.0},
    ]

    try:
        pipeline.batch_process(valid_batch)
        print(f"Current Store Records Count: {len(pipeline.data_store)}")
        print(f"Data: {pipeline.data_store}\n")
    except BasePipelineException as e:
        print(f"Pipeline Error: {e}\n")

    # --- Test 2: Validation Exception Catching ---
    print("--- [Test 2] Testing Validation Exception Handling ---")
    invalid_record = {"id": 104, "score": 150.0}  # Out of range score

    try:
        pipeline.add_record(invalid_record)
    except ValidationError as ve:
        print(f"Caught Specific Error: {ve}")
        print(f"Offending Value: {ve.invalid_value}\n")

    # --- Test 3: Batch Atomic Rollback Verification ---
    print("--- [Test 3] Testing Transactional Rollback ---")
    bad_batch = [
        {"id": 105, "score": 80.0},
        {"id": 106, "score": 95.0, "trigger_crash": True},  # Forces runtime crash
    ]

    print(
        f"Store Count BEFORE failed batch: {len(pipeline.data_store)}"
    )

    try:
        pipeline.batch_process(bad_batch)
    except RollbackException as re:
        print(f"Handled Expected Rollback: {re}")

    print(
        f"Store Count AFTER failed batch: {len(pipeline.data_store)}"
    )
    print(f"Data Store Integrity Retained: {pipeline.data_store}")