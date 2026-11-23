from abc import ABC, abstractmethod
import random

from utils.constants import Matrix2D


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
   
    @abstractmethod
    def addition(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        pass

    @abstractmethod
    def multiplication(self, A: Matrix2D, B: Matrix2D) -> Matrix2D:
        pass

    @abstractmethod
    def transpose(self, A: Matrix2D) -> Matrix2D:
        return [list(_) for _ in zip(*A)]
