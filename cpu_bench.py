from typing import Optional
import time

from utils import (
    MatrixSequentially, MatrixThreading, MatrixParallel,
    MatrixOp, MatrixBase, options, setup_logging, get_logger
)


setup_logging()
logger = get_logger(__name__)


def cpu_bound(
    rows: int, cols: int,
    operation: MatrixOp, rand: bool = False,
    matrix: Optional[MatrixBase] = None
) -> float:
    A = matrix.create(rows, cols, rand=rand)
    B = matrix.create(rows, cols, rand=rand)
    
    start_time = time.perf_counter()

    operation(A, B) 

    end_time = time.perf_counter()

    return end_time - start_time

    
def main():
    args = options()

    match args.mode:
        case "sequential":
            matrix = MatrixSequentially()
        case "threaded":
            matrix = MatrixThreading()
        case "parallel":
            matrix = MatrixParallel()
        case _:
            raise ValueError(f"Unknown mode: {args.mode}")

    operations = {
        "add": matrix.addition,
        "mult": matrix.multiplication,
        "transpose": lambda A, B: matrix.transpose(A)
    }

    selected_op = operations[args.op]

    logger.info(
        f"Running '{args.op}' on {args.rows}x{args.cols} matrices..."
    )
    
    elapsed = cpu_bound(
        args.rows, args.cols, selected_op, args.random, matrix
    )

    logger.info(f"Operation completed in {elapsed:.4f} seconds.")


if __name__ == "__main__":
    main()

