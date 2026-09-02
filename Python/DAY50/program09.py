import io
import pandas as pd


class CSVDataAnalysisSystem:
    """Out-of-Memory CSV Streaming & Analytics Processing Engine using Pandas."""

    def __init__(self, csv_source, chunksize: int = 1000):
        """Source can be a file path or buffer object."""
        self.csv_source = csv_source
        self.chunksize = chunksize

    def analyze_in_chunks(self, target_column: str) -> dict:
        """Reads CSV incrementally to compute global statistics with low memory footprint."""
        total_sum = 0.0
        total_count = 0
        min_val = float("inf")
        max_val = float("-inf")

        # Stream reading via pandas Chunked Iterator
        for chunk in pd.read_csv(self.csv_source, chunksize=self.chunksize):
            if target_column in chunk.columns:
                clean_series = chunk[target_column].dropna()
                total_sum += clean_series.sum()
                total_count += len(clean_series)
                min_val = min(min_val, clean_series.min())
                max_val = max(max_val, clean_series.max())

        mean_val = total_sum / total_count if total_count > 0 else 0.0
        return {
            "Total Records Processed": total_count,
            "Sum": total_sum,
            "Mean": mean_val,
            "Min": min_val,
            "Max": max_val,
        }

    def inspect_schema_and_nulls(self) -> pd.DataFrame:
        """Reads first batch chunk to inspect schema, data types, and missing count."""
        first_chunk = next(
            pd.read_csv(self.csv_source, chunksize=self.chunksize)
        )
        audit_df = pd.DataFrame(
            {
                "Data Type": first_chunk.dtypes,
                "Null Count (First Batch)": first_chunk.isnull().sum(),
                "Sample Value": first_chunk.iloc[0],
            }
        )
        return audit_df

    def stream_filter_and_export(
        self,
        output_filepath: str,
        filter_col: str,
        condition_func,
    ):
        """Filters large CSV data stream chunk-by-chunk and writes directly to output CSV."""
        first_chunk = True
        total_exported = 0

        for chunk in pd.read_csv(self.csv_source, chunksize=self.chunksize):
            if filter_col in chunk.columns:
                filtered_chunk = chunk[condition_func(chunk[filter_col])]
                total_exported += len(filtered_chunk)

                # Write mode append ('a') for streaming output
                mode = "w" if first_chunk else "a"
                header = first_chunk
                filtered_chunk.to_csv(
                    output_filepath, mode=mode, header=header, index=False
                )
                first_chunk = False

        print(
            f"[EXPORT] Successfully streamed {total_exported} rows matching criteria to '{output_filepath}'."
        )


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      PANDAS CSV DATA ANALYSIS SYSTEM       ")
    print("============================================\n")

    # 1. Simulating a Large CSV File in Memory Buffer
    mock_csv_data = """transaction_id,user_id,amount,category,status
1001,USR_A,150.50,Electronics,COMPLETED
1002,USR_B,45.00,Grocery,COMPLETED
1003,USR_C,1200.00,Electronics,PENDING
1004,USR_A,300.25,Fashion,COMPLETED
1005,USR_D,89.90,Grocery,CANCELLED
1006,USR_E,450.00,Electronics,COMPLETED
1007,USR_B,65.80,Fashion,COMPLETED
1008,USR_C,210.00,Grocery,COMPLETED
"""

    # Using StringIO to treat mock text data like an actual CSV file path
    csv_buffer = io.StringIO(mock_csv_data)

    # Initialize CSV Engine with chunksize=3 (Simulating chunked stream processing)
    csv_engine = CSVDataAnalysisSystem(csv_source=csv_buffer, chunksize=3)

    # 2. Schema and Missing Value Audit
    print("--- [1] Initial Schema & Null Value Audit ---")
    schema_info = csv_engine.inspect_schema_and_nulls()
    print(schema_info)

    # Reset buffer position for next read operation
    csv_buffer.seek(0)

    # 3. Incremental Chunked Stream Metrics Calculation
    print("\n--- [2] Out-of-Memory Chunked Aggregations (Column: 'amount') ---")
    metrics = csv_engine.analyze_in_chunks(target_column="amount")
    for metric, val in metrics.items():
        print(f"  {metric:<25}: {val:.2f}" if isinstance(val, float) else f"  {metric:<25}: {val}")

    # Reset buffer position
    csv_buffer.seek(0)

    # 4. Stream Filter & Export Simulation
    print("\n--- [3] Stream Filtering (COMPLETED Electronics Transactions) ---")

    # Temp target path simulation
    csv_engine.stream_filter_and_export(
        output_filepath="filtered_output.csv",
        filter_col="category",
        condition_func=lambda col: col == "Electronics",
    )