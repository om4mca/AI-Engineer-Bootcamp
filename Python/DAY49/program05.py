import concurrent.futures
import time
import numpy as np


class MatrixMultiplicationSystem:
    """A multi-engine Matrix Multiplication System implementing Naive, Blocked,

    and Parallel execution strategies using NumPy arrays.
    """

    def __init__(self, A, B):
        self.A = np.array(A, dtype=float)
        self.B = np.array(B, dtype=float)

        self.r1, self.c1 = self.A.shape
        self.r2, self.c2 = self.B.shape

        # Validate inner matrix dimension compatibility
        if self.c1 != self.r2:
            raise ValueError(
                f"Dimension mismatch: Cannot multiply ({self.r1}x{self.c1}) and ({self.r2}x{self.c2}). "
                f"Inner dimensions must match ({self.c1} != {self.r2})."
            )

    # --- 1. Naive Engine O(n^3) ---
    def multiply_naive(self):
        """Standard 3-loop matrix multiplication without cache optimization."""
        C = np.zeros((self.r1, self.c2))
        for i in range(self.r1):
            for j in range(self.c2):
                for k in range(self.c1):
                    C[i, j] += self.A[i, k] * self.B[k, j]
        return C

    # --- 2. Cache-Aware Blocked Engine (Tiled Multiplication) ---
    def multiply_blocked(self, block_size=32):
        """Tiled block-matrix multiplication optimized for CPU L1/L2 cache locality."""
        C = np.zeros((self.r1, self.c2))

        for ii in range(0, self.r1, block_size):
            for jj in range(0, self.c2, block_size):
                for kk in range(0, self.c1, block_size):
                    # Define sub-matrix block boundaries
                    i_end = min(ii + block_size, self.r1)
                    j_end = min(jj + block_size, self.c2)
                    k_end = min(kk + block_size, self.c1)

                    # Compute sub-matrix multiplication
                    C[ii:i_end, jj:j_end] += (
                        self.A[ii:i_end, kk:k_end] @ self.B[kk:k_end, jj:j_end]
                    )
        return C

    # --- 3. Parallel Multi-Core Engine ---
    def _compute_row_block(self, row_start, row_end):
        """Helper for computing a slice of output matrix rows."""
        return self.A[row_start:row_end, :] @ self.B

    def multiply_parallel(self, max_workers=4):
        """Multi-threaded parallel matrix multiplication across row chunks."""
        C = np.zeros((self.r1, self.c2))
        chunk_size = int(np.ceil(self.r1 / max_workers))

        futures = []
        with concurrent.futures.ThreadPoolExecutor(
            max_workers=max_workers
        ) as executor:
            for i in range(0, self.r1, chunk_size):
                row_end = min(i + chunk_size, self.r1)
                future = executor.submit(self._compute_row_block, i, row_end)
                futures.append((i, row_end, future))

            for i, row_end, future in futures:
                C[i:row_end, :] = future.result()

        return C

    # --- Benchmark & System Comparison ---
    def benchmark(self):
        print("=" * 60)
        print("         MATRIX MULTIPLICATION SYSTEM BENCHMARK")
        print("=" * 60)
        print(f"Matrix A Dimensions : {self.r1} x {self.c1}")
        print(f"Matrix B Dimensions : {self.r2} x {self.c2}")
        print(
            f"Total FLOPs         : {2 * self.r1 * self.c1 * self.c2:,} operations\n"
        )

        results = {}

        # Run Naive (Skip if size > 300 due to latency)
        if self.r1 <= 300:
            start = time.perf_counter()
            _ = self.multiply_naive()
            results["Naive O(n^3)"] = time.perf_counter() - start
        else:
            results["Naive O(n^3)"] = "Skipped (Too Slow)"

        # Run Blocked
        start = time.perf_counter()
        _ = self.multiply_blocked(block_size=64)
        results["Cache-Blocked (Tiled)"] = time.perf_counter() - start

        # Run Parallel
        start = time.perf_counter()
        _ = self.multiply_parallel(max_workers=4)
        results["Parallel (4-Workers)"] = time.perf_counter() - start

        # Run Native NumPy BLAS (OpenBLAS / MKL)
        start = time.perf_counter()
        _ = self.A @ self.B
        results["NumPy BLAS (Optimized C/Fortran)"] = (
            time.perf_counter() - start
        )

        for engine, duration in results.items():
            if isinstance(duration, float):
                print(f"{engine:<35}: {duration:.6f} seconds")
            else:
                print(f"{engine:<35}: {duration}")
        print("=" * 60)


# --- Execution Example ---
if __name__ == "__main__":
    # Generate two random 250x250 matrices
    N = 250
    A_mat = np.random.rand(N, N)
    B_mat = np.random.rand(N, N)

    system = MatrixMultiplicationSystem(A_mat, B_mat)
    system.benchmark()