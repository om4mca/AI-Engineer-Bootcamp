import numpy as np
import pandas as pd


class DataFrameCleaningSystem:
    """Robust Tabular Data Sanitization & Cleaning Engine using Pandas."""

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def clean_column_names(self) -> "DataFrameCleaningSystem":
        """Column names ke spaces trim karta hai aur lower_snake_case format me convert karta hai."""
        self.df.columns = (
            self.df.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace(r"[^\w\s]", "", regex=True)
        )
        return self

    def remove_duplicates(
        self, subset: list = None
    ) -> "DataFrameCleaningSystem":
        """Duplicate rows remove karta hai."""
        initial_count = len(self.df)
        self.df.drop_duplicates(subset=subset, inplace=True)
        print(f"[LOG] Removed {initial_count - len(self.df)} duplicate rows.")
        return self

    def sanitize_strings(self, columns: list) -> "DataFrameCleaningSystem":
        """String columns se extra spaces trim karta hai aur null placeholders clean karta hai."""
        for col in columns:
            if col in self.df.columns:
                self.df[col] = (
                    self.df[col]
                    .astype(str)
                    .str.strip()
                    .replace(["nan", "None", "null", "N/A", ""], np.nan)
                )
        return self

    def parse_currency_to_float(
        self, columns: list
    ) -> "DataFrameCleaningSystem":
        """Currency symbols ($, ₹, commas) remove karke numeric float me convert karta hai."""
        for col in columns:
            if col in self.df.columns:
                self.df[col] = (
                    self.df[col]
                    .astype(str)
                    .str.replace(r"[^\d.]", "", regex=True)
                )
                self.df[col] = pd.to_numeric(self.df[col], errors="coerce")
        return self

    def handle_missing_values(
        self, numeric_strategy: str = "median", categorical_fill: str = "Unknown"
    ) -> "DataFrameCleaningSystem":
        """Numeric missing values ko median/mean se aur categorical ko placeholder se fill karta hai."""
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                if numeric_strategy == "median":
                    fill_val = self.df[col].median()
                elif numeric_strategy == "mean":
                    fill_val = self.df[col].mean()
                self.df[col] = self.df[col].fillna(fill_val)
            else:
                self.df[col] = self.df[col].fillna(categorical_fill)
        return self

    def parse_dates(
        self, columns: list, date_format: str = "%Y-%m-%d"
    ) -> "DataFrameCleaningSystem":
        """String date columns ko standard datetime object me parse karta hai."""
        for col in columns:
            if col in self.df.columns:
                self.df[col] = pd.to_datetime(self.df[col], errors="coerce")
        return self

    def execute_pipeline(self) -> pd.DataFrame:
        """Cleaned DataFrame return karta hai."""
        return self.df


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      PANDAS DATAFRAME CLEANING SYSTEM      ")
    print("============================================\n")

    # 1. Messy Raw Data Simulation
    raw_data = {
        " Employee Name ": [
            "  Alice Smith ",
            "Bob Jones ",
            "Charlie Brown",
            "  Alice Smith ",
            "David Miller",
        ],
        " Join Date ": [
            "2021-01-15",
            "15/02/2022",
            "2023-03-20",
            "2021-01-15",
            "N/A",
        ],
        " Age ": ["28", "34", "N/A", "28", "45"],
        " Salary ($) ": ["$55,000.00", "$62,500.50", " ₹75000 ", "$55,000.00", None],
        " Department ": [" HR ", "IT", " null ", " HR ", "Finance"],
    }

    raw_df = pd.DataFrame(raw_data)

    print("--- RAW MESSY DATAFRAME ---")
    print(raw_df)
    print("\n" + "=" * 50 + "\n")

    # 2. Pipeline Execution
    cleaner = DataFrameCleaningSystem(raw_df)

    cleaned_df = (
        cleaner.clean_column_names()
        .remove_duplicates()
        .sanitize_strings(["employee_name", "department"])
        .parse_currency_to_float(["salary"])
        .parse_dates(["join_date"])
        .handle_missing_values(
            numeric_strategy="median", categorical_fill="Unassigned"
        )
        .execute_pipeline()
    )

    print("--- SANITIZED CLEANED DATAFRAME ---")
    print(cleaned_df)

    print("\n--- DATAFRAME DATA TYPES & INFO ---")
    print(cleaned_df.dtypes)