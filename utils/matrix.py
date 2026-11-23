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

        cols_B = self.transpose(B)

        return self._compute_rows(A, cols_B, 0, len(cols_B))


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
