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

    def transpose(self, A: Matrix2D) -> Matrix2D:
        return [list(_) for _ in zip(*A)]


class MatrixThreading(MatrixBase):
    pass