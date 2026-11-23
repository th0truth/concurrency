from abc import ABC, abstractmethod
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

       
