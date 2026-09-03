import numpy as np
import pandas as pd


class MLDatasetAnalyzer:

    def __init__(
        self,
        df: pd.DataFrame,
        target_col: str,
        id_cols: list = None,
        date_cols: list = None,
    ):
        """Initializes the analyzer with dataset context and metadata."""
        self.df = df.copy()
        self.target_col = target_col
        self.id_cols = id_cols or []
        self.date_cols = date_cols or []

        # Feature matrix (X) and target vector (y)
        self.X = self.df.drop(columns=[self.target_col])
        self.y = self.df[self.target_col]

    def inspect_dataset_properties(self):
        """Analyzes matrix shape, variable dtypes, and separates features."""
        print("=" * 65)
        print(" 1. DATASET PROPERTIES & METADATA")
        print("=" * 65)

        total_rows, total_cols = self.df.shape
        print(f"Total Observations (Rows): {total_rows}")
        print(f"Total Columns            : {total_cols}")
        print(f"Feature Matrix (X) Shape : {self.X.shape}")
        print(f"Target Vector (y) Shape  : {self.y.shape}")

        num_cols = self.X.select_dtypes(
            include=["int64", "float64", "number"]
        ).columns.tolist()
        cat_cols = self.X.select_dtypes(
            include=["object", "category", "bool"]
        ).columns.tolist()

        # Remove explicit ID and Date columns from general features
        num_cols = [c for c in num_cols if c not in self.id_cols + self.date_cols]
        cat_cols = [c for c in cat_cols if c not in self.id_cols + self.date_cols]

        print(f"\n[Numerical Features] ({len(num_cols)}): {num_cols}")
        print(f"[Categorical Features] ({len(cat_cols)}): {cat_cols}")
        if self.id_cols:
            print(f"[ID Columns]           ({len(self.id_cols)}): {self.id_cols}")
        if self.date_cols:
            print(
                f"[Date/Time Columns]    ({len(self.date_cols)}): {self.date_cols}"
            )

        return num_cols, cat_cols

    def classify_problem_type(self):
        """Determines if target represents Regression vs Classification."""
        print("\n" + "=" * 65)
        print(" 2. PROBLEM TYPE DIAGNOSTIC")
        print("=" * 65)

        target_dtype = self.y.dtype
        unique_targets = self.y.nunique()

        print(
            f"Target Column: '{self.target_col}' | DataType: {target_dtype} | Unique Values: {unique_targets}"
        )

        if pd.api.types.is_numeric_dtype(self.y) and unique_targets > 20:
            problem_type = "Regression"
            task_desc = "Continuous Numeric Prediction"
        elif unique_targets == 2:
            problem_type = "Binary Classification"
            task_desc = f"Discrete Classes -> {list(self.y.unique())}"
        elif 2 < unique_targets <= 20:
            problem_type = "Multi-Class Classification"
            task_desc = f"Discrete Classes -> {list(self.y.unique())}"
        else:
            problem_type = "Unspecified / High-Cardinality Categorical"
            task_desc = "Requires manual review or encoding"

        print(f"Diagnosed Task : {problem_type}")
        print(f"Target Nature  : {task_desc}")

        # Class balance check for classification
        if "Classification" in problem_type:
            class_dist = self.y.value_counts(normalize=True) * 100
            print("\nClass Distribution (%):")
            for cls_val, pct in class_dist.items():
                print(f" - Class {cls_val}: {pct:.2f}%")

        return problem_type

    def evaluate_split_proportions(
        self, test_ratio=0.2, val_ratio=0.0, seed=42
    ):
        """Calculates expected sample proportions for Train/Val/Test splits."""
        print("\n" + "=" * 65)
        print(" 3. SPLIT PROPORTION DIAGNOSTIC")
        print("=" * 65)

        n_samples = len(self.df)
        test_cnt = int(n_samples * test_ratio)
        val_cnt = int(n_samples * val_ratio)
        train_cnt = n_samples - test_cnt - val_cnt

        print(f"Total Dataset Size : {n_samples}")
        print(
            f"Training Subset    : {train_cnt} samples ({(train_cnt/n_samples)*100:.1f}%)"
        )
        if val_ratio > 0:
            print(
                f"Validation Subset  : {val_cnt} samples ({(val_cnt/n_samples)*100:.1f}%)"
            )
        print(
            f"Testing Subset     : {test_cnt} samples ({(test_cnt/n_samples)*100:.1f}%)"
        )

    def detect_data_leakage(
        self, correlation_threshold=0.85, test_indices=None
    ):
        """Audits features for target leakage, high correlations, and missing values."""
        print("\n" + "=" * 65)
        print(" 4. DATA LEAKAGE & QUALITY AUDIT")
        print("=" * 65)

        leakage_warnings = []

        # 1. High Target Correlation Check (Target Leakage)
        if pd.api.types.is_numeric_dtype(self.y):
            for col in self.X.select_dtypes(include=["number"]).columns:
                corr = abs(self.X[col].corr(self.y))
                if corr >= correlation_threshold:
                    leakage_warnings.append(
                        f"⚠️ TARGET LEAKAGE RISK: Feature '{col}' has high correlation ({corr:.4f}) with target."
                    )

        # 2. Unique ID Leakage Check
        for col in self.X.columns:
            if self.X[col].nunique() == len(self.X) and col not in self.id_cols:
                leakage_warnings.append(
                    f"⚠️ ID LEAKAGE RISK: Feature '{col}' has 100% unique values (unhandled row identifier)."
                )

        # 3. Missing Value Audit (Preprocessing Leakage Risk)
        missing_counts = self.X.isnull().sum()
        missing_cols = missing_counts[missing_counts > 0]
        if not missing_cols.empty:
            print("Missing Values Detected (Impute AFTER train/test split):")
            for col, count in missing_cols.items():
                print(
                    f" - {col}: {count} missing values ({count/len(self.X)*100:.1f}%)"
                )

        # 4. Train-Test Contamination Check (if indices supplied)
        if test_indices is not None:
            train_mask = ~self.df.index.isin(test_indices)
            train_df = self.df[train_mask].drop(columns=[self.target_col])
            test_df = self.df.loc[test_indices].drop(columns=[self.target_col])

            dups = pd.merge(train_df, test_df, how="inner").shape[0]
            if dups > 0:
                leakage_warnings.append(
                    f"⚠️ TRAIN-TEST CONTAMINATION: Found {dups} identical feature rows across train and test sets."
                )

        if leakage_warnings:
            for w in leakage_warnings:
                print(w)
        else:
            print("✅ No explicit target leakage or ID warnings detected.")

    def run_full_analysis(self, test_ratio=0.2):
        """Executes the complete dataset analysis pipeline."""
        self.inspect_dataset_properties()
        self.classify_problem_type()
        self.evaluate_split_proportions(test_ratio=test_ratio)
        self.detect_data_leakage()
        print("\n" + "=" * 65 + "\n")


# =====================================================================
# EXAMPLE RUNTIME VERIFICATION (Synthetic Hospital Dataset)
# =====================================================================
if __name__ == "__main__":
    np.random.seed(42)
    n = 150

    # Build synthetic hospital risk dataset
    data = {
        "Patient_ID": np.arange(1000, 1000 + n),
        "Age": np.random.randint(20, 85, size=n),
        "BloodPressure": np.random.normal(120, 15, size=n),
        "Department": np.random.choice(
            ["Cardiology", "Neurology", "General"], size=n
        ),
        "Readmitted": np.random.choice([0, 1], size=n, p=[0.7, 0.3]),
    }

    df_hospital = pd.DataFrame(data)

    # Inject missing values
    df_hospital.loc[10:15, "BloodPressure"] = np.nan

    # Inject post-outcome feature (Leakage)
    df_hospital["Post_Op_Score"] = df_hospital[
        "Readmitted"
    ] * 4.5 + np.random.normal(0, 0.1, size=n)

    # Initialize and execute Analyzer
    analyzer = MLDatasetAnalyzer(
        df=df_hospital, target_col="Readmitted", id_cols=["Patient_ID"]
    )

    analyzer.run_full_analysis(test_ratio=0.2)