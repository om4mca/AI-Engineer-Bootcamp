import logging
from contextlib import contextmanager

# Base logger setup
logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
logger = logging.getLogger("AppLogger")

@contextmanager
def temporary_log_level(new_level: int, target_logger: logging.Logger = logger):
    """Temporarily overrides the logging level for a target logger."""
    original_level = target_logger.level
    target_logger.setLevel(new_level)
    try:
        yield target_logger
    finally:
        # Guarantee original log level is restored
        target_logger.setLevel(original_level)


# --- Usage ---
logger.debug("This DEBUG log won't print initially.")

# Lower level to DEBUG inside the block
with temporary_log_level(logging.DEBUG):
    logger.debug("This DEBUG log IS visible inside the context manager!")

logger.debug("This DEBUG log won't print again because level reset to INFO.")