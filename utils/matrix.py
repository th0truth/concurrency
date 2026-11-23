from concurrent.futures import ThreadPoolExecutor
from typing import List

from utils.base import MatrixBase
from utils.constants import Matrix2D


class MatrixSequentially(MatrixBase):
    def addition(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        self._validate_addition(A, B)

        return [self._add_rows(a, b) for a, b in zip(A, B)]

    def multiplication(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        self._validate_multiplication(A, B)

        rows = len(A)
        cols = len(B[0])
        inner = len(B)

        result = self.create(rows, cols)

        for i in range(rows):
            for j in range(cols):
                for k in range(inner):
                    result[i][j] += A[i][k] * B[k][j]

        return result


class MatrixThreading(MatrixBase):
    def addition(
        self, A: Matrix2D, B: Matrix2D, workers: int = 4
    ) -> List[Matrix2D]:
        self._validate_addition(A, B)

        with ThreadPoolExecutor(workers) as executor:
            return list(
                executor.map(self._add_rows, A, B)
            )

    def multiplication(
        self, A: Matrix2D, B: Matrix2D, workers: int = 4
    ) -> Matrix2D:
        self._validate_multiplication(A, B)

        rows = len(A)
        B_cols = self.transpose(B)    

        chunk_size = (rows + workers - 1) // workers
        ranges = [
            (i, min(i + chunk_size, rows))
            for i in range(0, rows, chunk_size)
        ]

        with ThreadPoolExecutor(workers) as executor:
            futures = [
                executor.submit(self._compute_rows, A, B_cols, start, end)
                for start, end in ranges
            ]

            result = []

            for f in futures:
                result.extend(f.result())

        return result

    def _compute_rows(
        self, A: Matrix2D, cols_B: Matrix2D, start: int, end: int
    ) -> Matrix2D:
        k = len(A[0])
        n = len(cols_B)
        rrange = end - start

        out = [[0] * n for _ in range(rrange)]

        for i, row in enumerate(range(start, end)):
            row_a = A[row]
            out_row = out[i]

            for c in range(n):
                col_b = cols_B[c]
                result = 0

                for kk in range(k):
                    result += row_a[kk] * col_b[kk]

                out_row[c] = result

        return out