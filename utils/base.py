from abc import ABC, abstractmethod
from typing import List, Tuple
import random

from utils.constants import Matrix1D, Matrix2D


class MatrixBase(ABC):
    def create(
        self, rows: int, cols: int, *, rand: bool = False
    ) -> Matrix2D:
        return [
            [
                (
                    random.random()
                    if rand else 0
                ) for _ in range(cols)
            ]
            for _ in range(rows)
        ]
    
    def transpose(self, A: Matrix2D) -> Matrix2D:
        return [list(_) for _ in zip(*A)]

    @abstractmethod
    def addition(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        pass

    @abstractmethod
    def multiplication(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        pass

    def _add_rows(self, row_A: Matrix1D, row_B: Matrix1D) -> Matrix2D:
        return [x + y for x, y in zip(row_A, row_B)]

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

    def _get_mult_ranges(
        self, rows: int, workers: int
    ) -> List[Tuple[int, int]]:
        chunk_size = (rows + workers - 1) // workers
        ranges = [
            (i, min(i + chunk_size, rows))
            for i in range(0, rows, chunk_size)
        ]

        return ranges

    @staticmethod
    def _validate_addition(A: Matrix2D, B: Matrix2D):
        if not A or not B or len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Matricies must have the same dimensions.")

    @staticmethod
    def _validate_multiplication(A: Matrix2D, B: Matrix2D):
        if not A or not B or len(A[0]) != len(B):
            raise ValueError(
                "Number of columns in A must equal number of rows in B."
            )

       
