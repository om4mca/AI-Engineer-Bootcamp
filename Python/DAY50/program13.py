import math
import statistics
from typing import Dict, List, Union


class OutlierDetectionSystem:
    """Statistical Outlier & Anomaly Detection Engine using pure Python."""

    def __init__(self, data: List[Union[int, float]]):
        if not data or len(data) < 3:
            raise ValueError("Dataset must contain at least 3 numerical elements.")
        self.raw_data = data
        self.n = len(data)

    def detect_zscore(self, threshold: float = 3.0) -> Dict[str, Union[int, List]]:
        """Identifies outliers using Z-Score (|Z| > threshold).
        Best suited for Normally Distributed data.
        """
        mean_val = statistics.mean(self.raw_data)
        std_val = statistics.stdev(self.raw_data)

        if std_val == 0:
            return {"method": "Z-Score", "outlier_count": 0, "outliers": []}

        outliers = []
        detailed_flags = []

        for idx, val in enumerate(self.raw_data):
            z_score = (val - mean_val) / std_val
            is_outlier = abs(z_score) > threshold
            if is_outlier:
                outliers.append(val)

            detailed_flags.append(
                {
                    "index": idx,
                    "value": val,
                    "z_score": round(z_score, 3),
                    "is_outlier": is_outlier,
                }
            )

        return {
            "method": f"Z-Score (|Z| > {threshold})",
            "threshold": threshold,
            "outlier_count": len(outliers),
            "outliers": outliers,
            "detailed_records": detailed_flags,
        }

    def detect_iqr(self, multiplier: float = 1.5) -> Dict[str, Union[float, List]]:
        """Identifies outliers using IQR Rule [Q1 - (m * IQR), Q3 + (m * IQR)].
        Best suited for Skewed or Non-Normal distributions.
        """
        sorted_data = sorted(self.raw_data)
        quantiles = statistics.quantiles(sorted_data, n=4)
        q1, q3 = quantiles[0], quantiles[2]
        iqr = q3 - q1

        lower_bound = q1 - (multiplier * iqr)
        upper_bound = q3 + (multiplier * iqr)

        outliers = [x for x in self.raw_data if x < lower_bound or x > upper_bound]

        return {
            "method": f"IQR Rule (multiplier = {multiplier})",
            "q1": round(q1, 3),
            "q3": round(q3, 3),
            "iqr": round(iqr, 3),
            "lower_bound": round(lower_bound, 3),
            "upper_bound": round(upper_bound, 3),
            "outlier_count": len(outliers),
            "outliers": outliers,
        }

    def filter_clean_data(self, method: str = "iqr") -> List[Union[int, float]]:
        """Returns dataset with outliers removed based on the selected method."""
        if method.lower() == "iqr":
            result = self.detect_iqr()
            lower, upper = result["lower_bound"], result["upper_bound"]
            return [x for x in self.raw_data if lower <= x <= upper]
        elif method.lower() == "zscore":
            result = self.detect_zscore()
            outliers_set = set(result["outliers"])
            return [x for x in self.raw_data if x not in outliers_set]
        else:
            raise ValueError("Method must be either 'iqr' or 'zscore'")


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("     STATISTICAL OUTLIER DETECTION SYSTEM   ")
    print("============================================\n")

    # Sample Dataset: Sensor readings with normal values + extreme anomalies
    sensor_readings = [
        24.2, 25.1, 24.8, 25.0, 24.9, 25.3, 24.7, 25.2,
        -12.5,  # Anomaly 1: Sensor Malfunction (Negative drop)
        24.9, 25.1, 25.4, 24.6,
        148.0,  # Anomaly 2: Sudden Power Surge
        25.0, 24.8, 25.2, 25.1
    ]

    detector = OutlierDetectionSystem(sensor_readings)

    # 1. Z-Score Anomaly Detection
    print("--- [1] Z-Score Method Audit ---")
    z_res = detector.detect_zscore(threshold=2.5)
    print(f"Method          : {z_res['method']}")
    print(f"Outliers Count  : {z_res['outlier_count']}")
    print(f"Detected Values : {z_res['outliers']}\n")

    # 2. IQR Anomaly Detection
    print("--- [2] IQR Method Audit ---")
    iqr_res = detector.detect_iqr(multiplier=1.5)
    print(f"Method          : {iqr_res['method']}")
    print(f"Lower Bound     : {iqr_res['lower_bound']}")
    print(f"Upper Bound     : {iqr_res['upper_bound']}")
    print(f"Outliers Count  : {iqr_res['outlier_count']}")
    print(f"Detected Values : {iqr_res['outliers']}\n")

    # 3. Clean Dataset Export
    print("--- [3] Data Cleaning & Filtering ---")
    clean_data = detector.filter_clean_data(method="iqr")
    print(f"Original Count  : {len(sensor_readings)}")
    print(f"Cleaned Count   : {len(clean_data)}")
    print(f"Cleaned Data    : {clean_data}")