from typing import TypeAlias, List, Callable, Union


Matrix1D: TypeAlias = List[Union[float, int]]
Matrix2D: TypeAlias = List[List[Union[float, int]]]
MatrixOp: TypeAlias = Callable[[Matrix2D, Matrix2D], Matrix2D]
