import functools
import time
from typing import Any, Callable, Generator, List


# ==========================================
# 1. Custom Decorators for Stream Pipelines
# ==========================================
def stream_performance_logger(func: Callable) -> Callable:
    """Decorator jo stream processing start/stop tracking aur total time measure karta hai."""

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[PIPELINE START] Executing stream layer: '{func.__name__}'")
        start_time = time.perf_counter()

        # Call the generator function
        gen = func(*args, **kwargs)

        items_processed = 0
        for item in gen:
            items_processed += 1
            yield item

        elapsed = (time.perf_counter() - start_time) * 1000
        print(
            f"[PIPELINE END] Layer '{func.__name__}' completed. Processed {items_processed} items in {elapsed:.4f} ms."
        )

    return wrapper


def stream_filter(condition: Callable[[Any], bool]) -> Callable:
    """Parameterized Decorator jo stream item-by-item yield hote waqt memory consume kiye bina filter karta hai."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for item in func(*args, **kwargs):
                if condition(item):
                    yield item

        return wrapper

    return decorator


def stream_chunker(chunk_size: int) -> Callable:
    """Decorator jo continuous single item stream ko memory-friendly fixed-size chunks/batches mein group karta hai."""

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            buffer = []
            for item in func(*args, **kwargs):
                buffer.append(item)
                if len(buffer) == chunk_size:
                    yield buffer
                    buffer = []
            if buffer:
                yield buffer

        return wrapper

    return decorator


# ==========================================
# 2. Generator Stream Components
# ==========================================
class DataStreamProcessor:

    @staticmethod
    def raw_log_producer(count: int) -> Generator[dict, None, None]:
        """Generator 1: Raw telemetry log stream produce karta hai (Memory O(1))."""
        levels = ["INFO", "ERROR", "WARNING", "DEBUG", "ERROR"]
        for i in range(1, count + 1):
            yield {
                "event_id": 1000 + i,
                "level": levels[i % len(levels)],
                "payload_size_kb": i * 2.5,
                "timestamp": time.time(),
            }

    @staticmethod
    @stream_performance_logger
    @stream_filter(lambda log: log["level"] == "ERROR")
    def filter_critical_logs(
        log_stream: Generator[dict, None, None]
    ) -> Generator[dict, None, None]:
        """Generator 2 Layer: Standard logging aur Filtering apply karta hai using Decorators.

        Sirf 'ERROR' logs aage pass honge.
        """
        # Delegating stream using yield from
        yield from log_stream

    @staticmethod
    @stream_performance_logger
    @stream_chunker(chunk_size=3)
    def batch_transformation_pipeline(
        filtered_stream: Generator[dict, None, None]
    ) -> Generator[List[dict], None, None]:
        """Generator 3 Layer: Cleaned stream ko batches me chunk karta hai for bulk downstream DB ingestion."""
        for log in filtered_stream:
            # Enriched payload item-by-item
            log["status"] = "PROCESSED"
            yield log


# ==========================================
# 3. Execution Driver / Test Suite
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("   GENERATOR + DECORATOR INTEGRATION PIPELINE")
    print("============================================")

    TOTAL_RECORDS_TO_SIMULATE = 15

    # Step 1: Initialize Producer Generator
    raw_stream = DataStreamProcessor.raw_log_producer(TOTAL_RECORDS_TO_SIMULATE)

    # Step 2: Pass through Layer 1 (Filtering)
    filtered_stream = DataStreamProcessor.filter_critical_logs(raw_stream)

    # Step 3: Pass through Layer 2 (Batching/Chunking)
    batched_pipeline = DataStreamProcessor.batch_transformation_pipeline(
        filtered_stream
    )

    # Step 4: Consume Pipeline Lazily
    print("\n--- Consuming Batched Stream Output Lazily ---")
    batch_counter = 1
    for batch in batched_pipeline:
        print(f"\n[Consumer Received Batch {batch_counter}] (Size: {len(batch)})")
        for item in batch:
            print(
                f"  -> ID: {item['event_id']} | Level: {item['level']} | Status: {item['status']}"
            )
        batch_counter += 1

    print("\n[SUCCESS] Pipeline execution finished with zero memory footprint overload.")