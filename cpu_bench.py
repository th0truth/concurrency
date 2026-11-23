from typing import Optional
import argparse
import time

from utils import (
    MatrixSequentially, MatrixThreading,
    Matrix2D, MatrixOp, MatrixBase
)

def cpu_bound(
    rows: int, cols: int,
    operation: MatrixOp, rand: bool = False,
    matrix: Optional[MatrixBase] = None
) -> Matrix2D:
    matrix = matrix or MatrixSequentially()

    A = matrix.create(rows, cols, rand=rand)
    B = matrix.create(rows, cols, rand=rand)
    
    start_time = time.perf_counter()

    operation(A, B) 

    end_time = time.perf_counter()

    elapsed = end_time - start_time

    print(f"Operation completed in {elapsed:.4f} seconds.")
    
    
def main():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-r", "--rows", required=True, type=int,
        help="Number of rows of matrix."
    )

    parser.add_argument(
        "-c", "--cols", required=True, type=int,
        help="Number of cols of matrix."
    )

    parser.add_argument(
        "-o", "--op", choices=["add", "mult", "transpose"], default="add",
        help="Operation to perform: 'add', 'mult', 'transpose', etc.",
    )

    parser.add_argument(
        "--random", action="store_true", default=False,
        help="Generate random numbers instead of zeros."
    )

    parser.add_argument(
        "-m", "--mode", choices=["sequential", "threaded"], default="sequential",
        help="Execution mode."
    )

    args = parser.parse_args()

    match args.mode:
        case "sequential":
            matrix = MatrixSequentially()
        case "threaded":
            matrix = MatrixThreading()

    operations = {
        "add": matrix.addition,
        "mult": matrix.multiplication,
        "transpose": lambda A, B: matrix.transpose(A)
    }

    selected_op = operations[args.op]

    print(f"Running '{args.op}' on {args.rows}x{args.cols} matrices...")
    
    cpu_bound(
        args.rows, args.cols, selected_op, args.random, matrix
    )
    

if __name__ == "__main__":
    main()

