import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class HospitalVisualizationSystem:
    """Production Clinical Analytics Dashboard Builder using Matplotlib."""

    def __init__(self, data_dict: dict):
        self.dept_df = data_dict.get("departments")
        self.time_df = data_dict.get("timeseries")
        self.triage_df = data_dict.get("triage")
        plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    def generate_dashboard(self, save_path: str = None):
        """Creates a 2x2 Multi-Panel Clinical Visualization Dashboard."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 11))
        fig.suptitle(
            "Hospital Resource Utilization & Patient Flow Analytics",
            fontsize=16,
            fontweight="bold",
        )

        # ---------------------------------------------------------------------
        # Panel 1: Dual-Axis Chart (Bar: Wait Time, Line: Occupancy Rate)
        # ---------------------------------------------------------------------
        ax1 = axes[0, 0]
        ax2 = ax1.twinx()

        bars = ax1.bar(
            self.dept_df["Department"],
            self.dept_df["Avg_Wait_Mins"],
            color="#2b5c8f",
            alpha=0.75,
            width=0.4,
            label="Avg Wait Time (mins)",
        )
        line = ax2.plot(
            self.dept_df["Department"],
            self.dept_df["Bed_Occupancy_%"],
            color="#d95f02",
            marker="o",
            linewidth=2.5,
            label="Bed Occupancy (%)",
        )

        ax1.set_title("1. Department Wait Time vs. Bed Occupancy", fontweight="bold")
        ax1.set_ylabel("Avg Wait Time (Minutes)", color="#2b5c8f", fontweight="bold")
        ax2.set_ylabel("Bed Occupancy Rate (%)", color="#d95f02", fontweight="bold")
        ax2.grid(False)  # Remove grid overlap from second axis

        # Annotate Bar values
        for bar in bars:
            height = bar.get_height()
            ax1.annotate(
                f"{height}m",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha="center",
                va="bottom",
                fontsize=8,
            )

        # ---------------------------------------------------------------------
        # Panel 2: Daily Emergency Flow (Time-Series Line Chart)
        # ---------------------------------------------------------------------
        axes[0, 1].plot(
            self.time_df["Hour"],
            self.time_df["ER_Admissions"],
            color="#7570b3",
            linewidth=2,
            marker="s",
            markersize=4,
        )
        axes[0, 1].set_title("2. 24-Hour ER Patient Inflow Trend", fontweight="bold")
        axes[0, 1].set_xlabel("Hour of Day (24H Format)")
        axes[0, 1].set_ylabel("Patient Admissions")
        axes[0, 1].set_xticks(range(0, 24, 2))

        # Highlight Peak Hours Threshold
        peak_threshold = 30
        axes[0, 1].axhline(
            y=peak_threshold,
            color="red",
            linestyle="--",
            alpha=0.7,
            label="Surge Capacity Alert Threshold",
        )
        axes[0, 1].legend(loc="upper left", fontsize=8)

        # ---------------------------------------------------------------------
        # Panel 3: Triage Severity Distribution (Donut Chart)
        # ---------------------------------------------------------------------
        colors = ["#d95f02", "#e6ab02", "#7570b3", "#1b9e77"]
        wedges, texts, autotexts = axes[1, 0].pie(
            self.triage_df["Count"],
            labels=self.triage_df["Category"],
            autopct="%1.1f%%",
            startangle=140,
            colors=colors,
            wedgeprops=dict(width=0.4, edgecolor="w"),
        )
        plt.setp(autotexts, size=9, weight="bold", color="white")
        axes[1, 0].set_title("3. Triage Severity Category Distribution", fontweight="bold")

        # ---------------------------------------------------------------------
        # Panel 4: Staff-to-Patient Ratio (Horizontal Bar Chart)
        # ---------------------------------------------------------------------
        y_pos = np.arange(len(self.dept_df))
        axes[1, 1].barh(
            y_pos,
            self.dept_df["Patients_Per_Doctor"],
            color="#1b9e77",
            alpha=0.8,
            height=0.5,
        )
        axes[1, 1].set_yticks(y_pos)
        axes[1, 1].set_yticklabels(self.dept_df["Department"])
        axes[1, 1].invert_yaxis()  # Top-down order
        axes[1, 1].set_xlabel("Patients Assigned per Active Doctor")
        axes[1, 1].set_title("4. Workload Density (Patient-to-Doctor Ratio)", fontweight="bold")

        # Add target line
        axes[1, 1].axvline(x=5, color="black", linestyle=":", label="Optimal Target (1:5)")
        axes[1, 1].legend(loc="lower right", fontsize=8)

        plt.tight_layout(rect=[0, 0, 1, 0.96])

        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
            print(f"[SUCCESS] Hospital Dashboard saved to '{save_path}'.")

        plt.show()


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("   HOSPITAL DATA VISUALIZATION SYSTEM       ")
    print("============================================\n")

    # 1. Mock Hospital Operational Datasets
    department_data = pd.DataFrame(
        {
            "Department": ["ER", "ICU", "Pediatrics", "Cardiology", "Orthopedics", "General"],
            "Avg_Wait_Mins": [48, 5, 22, 35, 40, 55],
            "Bed_Occupancy_%": [92, 88, 65, 78, 70, 82],
            "Patients_Per_Doctor": [8.2, 2.1, 4.5, 6.0, 5.2, 7.8],
        }
    )

    timeseries_data = pd.DataFrame(
        {
            "Hour": list(range(24)),
            "ER_Admissions": [12, 8, 5, 3, 4, 7, 15, 22, 31, 35, 28, 25, 22, 26, 30, 38, 42, 36, 29, 24, 19, 16, 14, 11],
        }
    )

    triage_data = pd.DataFrame(
        {
            "Category": ["Resuscitation (Level 1)", "Emergent (Level 2)", "Urgent (Level 3)", "Non-Urgent (Level 4/5)"],
            "Count": [15, 45, 120, 80],
        }
    )

    clinical_datasets = {
        "departments": department_data,
        "timeseries": timeseries_data,
        "triage": triage_data,
    }

    # 2. Render Visualization Dashboard
    print("--- Generating Hospital Analytics Dashboard ---")
    hosp_system = HospitalVisualizationSystem(clinical_datasets)
    hosp_system.generate_dashboard(save_path="hospital_clinical_dashboard.png")