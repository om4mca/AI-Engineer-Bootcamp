class PipelineError(Exception):
    """Base exception for all errors in this pipeline package."""
    pass

class DataValidationError(PipelineError):
    """Raised when record validation fails."""
    def __init__(self, record, reason):
        self.record = record
        self.reason = reason
        super().__init__(f"Invalid record {record}: {reason}")

class FileProcessingError(PipelineError):
    """Raised when file I/O operations fail."""
    pass