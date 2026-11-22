from typing import Optional, Union, List
import random

from utils.constants import MAX_RANDINT, MIN_RANDINT


class Matrix:
    def __init__(
        self,
        min_randint: Optional[int] = None,
        max_randint: Optional[int] = None
    ):
        self.min_randint = min_randint or MIN_RANDINT
        self.max_randint = max_randint or MAX_RANDINT

    def create(
        self, rows: int, cols: int, *, randint: bool = False
    ) -> List[List[float]]:
        return [
            [
                (
                    random.randint(self.min_randint, self.max_randint)
                    if randint else 0
                ) for _ in range(cols)
            ]
            for _ in range(rows)
        ]

    def addition(
        self,
        A: List[List[Union[int, float]]],
        B: List[List[Union[int, float]]]
    ):
        if not A or not B or len(A) != len(B) or len(A[0]) != len(B[0]):
            raise ValueError("Matricies must have the same dimensions.")

        rows = len(A)
        cols = len(A[0])

        result = self.create(rows, cols)

        for i in range(rows):
            for j in range(cols):
                result[i][j] = A[i][j] + B[i][j]

        return result

    def multiplication(
        self,
        A: List[List[Union[int, float]]],
        B: List[List[Union[int, float]]]
    ):
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
        self,
        A: List[List[Union[int, float]]],
        B_cols: List[List[Union[int, float]]],
        row_start: int,
        row_end: int
    ) -> List[List[Union[int, float]]]:
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


