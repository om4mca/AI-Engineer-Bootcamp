import sys
import numpy as np


class NumPyArrayAnalyzer:
    """Advanced NumPy Structural Array & Memory Analysis System."""

    def __init__(self, data):
        if not isinstance(data, np.ndarray):
            data = np.array(data)
        self.array = data

    def profile_memory_layout(self):
        """Memory footprint, striding, aur internal array alignment profile karta hai."""
        return {
            "Shape": self.array.shape,
            "Dimensions (ndim)": self.array.ndim,
            "Data Type (dtype)": self.array.dtype,
            "Item Size (bytes)": self.array.itemsize,
            "Total Bytes": self.array.nbytes,
            "Strides (byte steps)": self.array.strides,
            "Is C-Contiguous": self.array.flags["C_CONTIGUOUS"],
            "Is Fortran-Contiguous": self.array.flags["F_CONTIGUOUS"],
            "OWNS_DATA": self.array.flags["OWNSDATA"],
        }

    def extract_boolean_mask(self, condition_func):
        """Memory copy kiye bina vectorized condition apply karke values extract karta hai."""
        mask = condition_func(self.array)
        return self.array[mask]

    def demonstrate_strided_views(self, step=2):
        """Memory view (zero copy) create karta hai striding use karke."""
        return self.array[::step, ::step]


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("        NUMPY ARRAY ANALYSIS SYSTEM         ")
    print("============================================\n")

    # 1. Multi-dimensional Matrix Initialization (3x4 float64 array)
    raw_data = [
        [10.5, 25.0, 30.2, 45.8],
        [50.1, 12.4, 88.9, 60.3],
        [70.0, 95.2, 14.1, 33.6],
    ]
    analyzer = NumPyArrayAnalyzer(raw_data)

    # 2. Structural & Memory Profiling
    print("--- [1] Memory Layout & Structural Profiling ---")
    profile = analyzer.profile_memory_layout()
    for key, val in profile.items():
        print(f"  {key:<22}: {val}")

    # 3. Vectorized Boolean Indexing & Masking
    print("\n--- [2] Advanced Boolean Masking (Values > 40) ---")
    filtered_values = analyzer.extract_boolean_mask(lambda arr: arr > 40.0)
    print("Filtered Array Elements:", filtered_values)

    # 4. Zero-Copy View vs Deep Copy Analysis
    print("\n--- [3] Memory View vs Deep Copy Proof ---")
    base_arr = analyzer.array
    sliced_view = base_arr[:2, :2]  # View (Shares memory)
    copied_arr = base_arr[:2, :2].copy()  # Deep Copy (New memory allocation)

    print(
        "View shares memory with Base Array? ",
        np.shares_memory(base_arr, sliced_view),
    )
    print(
        "Copy shares memory with Base Array?",
        np.shares_memory(base_arr, copied_arr),
    )

    # View Modify karke original array par reflect hone ka proof
    sliced_view[0, 0] = 999.99
    print("\nModified View[0,0] -> 999.99")
    print("Original Base Array updated automatically (Zero-Copy):")
    print(base_arr)