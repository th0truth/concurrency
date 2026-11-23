from typing import TypeAlias, List, Callable, Union


Matrix2D: TypeAlias = List[List[Union[float, int]]]
MatrixOp: TypeAlias = Callable[[Matrix2D, Matrix2D], Matrix2D]
