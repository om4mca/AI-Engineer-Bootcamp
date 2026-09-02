import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class EmployeeVisualizationSystem:
    """Pure Matplotlib Dashboard Builder for HR and Employee Visual Analytics."""

    def __init__(self, data: pd.DataFrame):
        self.df = data
        # Clean background grid setup
        plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    def generate_dashboard(self, save_path: str = None):
        """Creates a 2x2 Multi-Panel Visual Dashboard without Seaborn."""
        fig, axes = plt.subplots(2, 2, figsize=(14, 10))
        fig.suptitle(
            "Employee Demographics & Performance Analytics",
            fontsize=16,
            fontweight="bold",
        )

        # ---------------------------------------------------------------------
        # Panel 1: Histogram + Kernel-like Frequency Line (Salary Distribution)
        # ---------------------------------------------------------------------
        counts, bins, patches = axes[0, 0].hist(
            self.df["Salary"], bins=8, color="#4c72b0", edgecolor="black", alpha=0.7
        )
        # Dynamic trend overlay over midpoints
        bin_centers = 0.5 * (bins[:-1] + bins[1:])
        axes[0, 0].plot(bin_centers, counts, color="#c44e52", linewidth=2, marker="o")
        axes[0, 0].set_title("1. Salary Distribution", fontweight="bold")
        axes[0, 0].set_xlabel("Salary ($)")
        axes[0, 0].set_ylabel("Employee Count")

        # ---------------------------------------------------------------------
        # Panel 2: Tenure vs Salary (Scatter Plot + Linear Fit Trend Line)
        # ---------------------------------------------------------------------
        x = self.df["Tenure_Years"]
        y = self.df["Salary"]
        axes[0, 1].scatter(x, y, color="#55a868", edgecolors="black", s=60, alpha=0.8)

        # Calculating Best Fit Line (Polyfit)
        m, c = np.polyfit(x, y, 1)
        axes[0, 1].plot(x, m * x + c, color="#c44e52", linewidth=2, linestyle="--", label=f"Fit: y={m:.0f}x+{c:.0f}")
        axes[0, 1].set_title("2. Tenure vs. Salary Growth Trend", fontweight="bold")
        axes[0, 1].set_xlabel("Tenure (Years)")
        axes[0, 1].set_ylabel("Salary ($)")
        axes[0, 1].legend()

        # ---------------------------------------------------------------------
        # Panel 3: Department-wise Average Salary Bar Chart with Value Annotations
        # ---------------------------------------------------------------------
        dept_summary = self.df.groupby("Department")["Salary"].mean().reset_index()
        bars = axes[1, 0].bar(
            dept_summary["Department"], dept_summary["Salary"], color="#8172b0", edgecolor="black", alpha=0.85
        )
        axes[1, 0].set_title("3. Average Salary by Department", fontweight="bold")
        axes[1, 0].set_xlabel("Department")
        axes[1, 0].set_ylabel("Mean Salary ($)")
        
        # Text Annotations on top of bars
        for bar in bars:
            height = bar.get_height()
            axes[1, 0].annotate(
                f"${height:,.0f}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 4),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=9,
                fontweight="bold"
            )

        # ---------------------------------------------------------------------
        # Panel 4: Pure Matplotlib Correlation Heatmap Matrix
        # ---------------------------------------------------------------------
        numeric_df = self.df.select_dtypes(include=[np.number])
        corr_matrix = numeric_df.corr().values
        cols = numeric_df.columns

        cax = axes[1, 1].matshow(corr_matrix, cmap="Blues", vmin=-1, vmax=1)
        fig.colorbar(cax, ax=axes[1, 1], fraction=0.046, pad=0.04)

        axes[1, 1].set_xticks(range(len(cols)))
        axes[1, 1].set_yticks(range(len(cols)))
        axes[1, 1].set_xticklabels(cols, rotation=35, ha="left", fontsize=8)
        axes[1, 1].set_yticklabels(cols, fontsize=8)
        axes[1, 1].set_title("4. Numeric Metric Correlation Matrix", fontweight="bold", pad=20)

        # Annotating cell values inside matrix
        for i in range(len(cols)):
            for j in range(len(cols)):
                val = corr_matrix[i, j]
                color = "white" if abs(val) > 0.5 else "black"
                axes[1, 1].text(j, i, f"{val:.2f}", ha="center", va="center", color=color, fontsize=9)

        plt.tight_layout(rect=[0, 0, 1, 0.96])

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"[SUCCESS] Dashboard exported successfully to '{save_path}'.")

        plt.show()


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("  EMPLOYEE VISUALIZATION SYSTEM (MATPLOTLIB)")
    print("============================================\n")

    # 1. Synthetic HR Dataset Generation
    np.random.seed(42)
    sample_size = 50

    hr_data = {
        "Emp_ID": [f"EMP_{100+i}" for i in range(sample_size)],
        "Department": np.random.choice(
            ["IT", "Sales", "HR", "Finance", "Engineering"], size=sample_size
        ),
        "Tenure_Years": np.random.uniform(0.5, 10.0, size=sample_size).round(1),
        "Performance_Score": np.random.randint(1, 6, size=sample_size),
        "Projects_Completed": np.random.randint(3, 25, size=sample_size),
    }

    df_emp = pd.DataFrame(hr_data)
    df_emp["Salary"] = (
        40000
        + (df_emp["Tenure_Years"] * 4500)
        + (df_emp["Projects_Completed"] * 1200)
        + np.random.normal(0, 3000, size=sample_size)
    ).round(2)

    print("--- [1] Dataset Preview ---")
    print(df_emp.head())

    # 2. Render Dashboard Window
    print("\n--- [2] Generating Pure Matplotlib Dashboard Window ---")
    viz_system = EmployeeVisualizationSystem(df_emp)
    viz_system.generate_dashboard(save_path="employee_analytics_matplotlib.png")