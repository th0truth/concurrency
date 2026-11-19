from typing import TypeAlias, List, Callable


Matrix2D: TypeAlias = List[List[float | int]]
MatrixOp: TypeAlias = Callable[[Matrix2D, Matrix2D], Matrix2D]

MIN_RANDINT = 1_000
MAX_RANDINT = 1_000_000

