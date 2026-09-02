import numpy as np
import pandas as pd


class GroupByAnalyticsSystem:
    """Advanced GroupBy & Aggregate Data Analytics Engine using Pandas."""

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def multi_level_aggregation(
        self, group_cols: list, agg_mapping: dict
    ) -> pd.DataFrame:
        """Computes summary metrics (mean, sum, count, std, etc.) grouped by multiple dimensions."""
        grouped_df = self.df.groupby(group_cols).agg(agg_mapping)
        # Flattening MultiIndex columns if generated
        if isinstance(grouped_df.columns, pd.MultiIndex):
            grouped_df.columns = [
                f"{col}_{func}" for col, func in grouped_df.columns
            ]
        return grouped_df.reset_index()

    def calculate_group_percentages(
        self, group_col: str, target_col: str, new_col_name: str
    ) -> pd.DataFrame:
        """Calculates percentage contribution of each row relative to its group total using transform()."""
        group_sums = self.df.groupby(group_col)[target_col].transform("sum")
        self.df[new_col_name] = np.round((self.df[target_col] / group_sums) * 100, 2)
        return self.df

    def compute_group_rankings(
        self, group_col: str, rank_col: str, ascending: bool = False
    ) -> pd.DataFrame:
        """Ranks elements within each group based on a numerical metric."""
        rank_col_name = f"{rank_col}_rank"
        self.df[rank_col_name] = self.df.groupby(group_col)[rank_col].rank(
            method="dense", ascending=ascending
        ).astype(int)
        return self.df

    def pivot_summary_matrix(
        self, index_col: str, columns_col: str, values_col: str, aggfunc: str = "sum"
    ) -> pd.DataFrame:
        """Reshapes tabular data into a two-dimensional Pivot Summary Matrix."""
        pivot_df = pd.pivot_table(
            self.df,
            index=index_col,
            columns=columns_col,
            values=values_col,
            aggfunc=aggfunc,
            fill_value=0,
        )
        return pivot_df


# ==========================================
# Driver Code & Execution
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("      PANDAS GROUPBY ANALYTICS SYSTEM       ")
    print("============================================\n")

    # 1. Sample Enterprise Dataset Initialization
    raw_data = {
        "Region": ["North", "North", "South", "South", "North", "South", "East", "East"],
        "Department": ["IT", "Sales", "IT", "Sales", "IT", "Sales", "IT", "Sales"],
        "Employee": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi"],
        "Salary": [85000, 60000, 92000, 58000, 88000, 64000, 78000, 61000],
        "Sales_Target_Achieved": [95, 110, 88, 125, 102, 115, 90, 105],
    }

    df = pd.DataFrame(raw_data)
    analytics = GroupByAnalyticsSystem(df)

    # 2. Multi-Level GroupBy Aggregation
    print("--- [1] Multi-Level Aggregation (By Region & Department) ---")
    agg_mapping = {
        "Salary": ["mean", "max"],
        "Sales_Target_Achieved": "mean",
        "Employee": "count",
    }
    multi_agg = analytics.multi_level_aggregation(["Region", "Department"], agg_mapping)
    print(multi_agg.to_string(index=False))

    # 3. Transform Window Function (Percentage Share within Department)
    print("\n--- [2] Salary Percentage Share within Department ---")
    df_with_pct = analytics.calculate_group_percentages(
        group_col="Department", target_col="Salary", new_col_name="Dept_Salary_Share_%"
    )
    print(df_with_pct[["Employee", "Department", "Salary", "Dept_Salary_Share_%"]])

    # 4. Group Ranking System
    print("\n--- [3] Salary Rank within Region ---")
    df_ranked = analytics.compute_group_rankings(
        group_col="Region", rank_col="Salary", ascending=False
    )
    print(df_ranked[["Region", "Employee", "Salary", "Salary_rank"]].sort_values(by=["Region", "Salary_rank"]))

    # 5. Pivot Table Summary Matrix
    print("\n--- [4] Pivot Summary Matrix (Total Salary: Region vs Department) ---")
    pivot_matrix = analytics.pivot_summary_matrix(
        index_col="Region", columns_col="Department", values_col="Salary", aggfunc="sum"
    )
    print(pivot_matrix)