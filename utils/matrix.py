from concurrent.futures import ThreadPoolExecutor

from utils.base import MatrixBase
from utils.constants import Matrix2D


class MatrixSequentially(MatrixBase):
    def addition(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        if not A or not B or len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Matricies must have the same dimensions.")

        rows = len(A)
        cols = len(A[0])

        result = self.create(rows, cols)

        for i in range(rows):
            for j in range(cols):
                result[i][j] = A[i][j] + B[i][j]

        return result

    def multiplication(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        if not A or not B or len(A[0]) != len(B):
            raise ValueError(
                "Number of columns in A must equal number of rows in B."
            )

        rows = len(A)
        cols = len(B[0])
        inner = len(B)

        result = self.create(rows, cols)

        for i in range(rows):
            for j in range(cols):
                for k in range(inner):
                    result[i][j] += A[i][k] * B[k][j]

        return result

    def compute_rows(
        self, A: Matrix2D, B_cols: Matrix2D,
        row_start: int, row_end: int
    ) -> Matrix2D:
        k = len(A[0])
        n = len(B_cols)
        rrange = row_end - row_start

        out = [[0] * n for _ in range(rrange)]

        for i, row in enumerate(range(row_start, row_end)):
            row_a = A[row]
            out_row = out[i]

            for c in range(n):
                col_b = B_cols[c]
                result = 0

                for kk in range(k):
                    result += row_a[kk] * col_b[kk]
                out_row[c] = result

        return out


class MatrixThreading(MatrixBase):
    def addition(self, A: Matrix2D, B: Matrix2D, workers: int = 4):
        with ThreadPoolExecutor(workers) as thread:
            return list(
                thread.map(self._add_rows, A, B)
            )

    def multiplication(self, A, B):
        raise NotImplementedError("Multiplication not implemented.")

    def _add_rows(self, row_A: Matrix2D, row_B: Matrix2D) -> Matrix2D:
        return [x + y for x, y in zip(row_A, row_B)]
