from typing import Optional
import argparse

from utils.constants import Matrix2D, MatrixOp
from utils.matrix import Matrix


def cpu_bound(
    rows: int, cols: int,
    operation: MatrixOp,
    matrix: Optional[Matrix] = None
) -> Matrix2D:
    matrix = matrix or Matrix()

    A = matrix.create(rows, cols, randint=True)
    B = matrix.create(rows, cols, randint=True)
    
    operation(A, B) 
    
    
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
        "-o", "--op", choices=["add", "mult"], default="add",
        help="Operation to perform: 'add' or 'mult' (default: add).",
    )

    args = parser.parse_args()

    matrix = Matrix()

    operations = {
        "add": matrix.addition,
        "mult": matrix.multiplication
    }

    selected_op = operations[args.op]

    print(f"Running '{args.op}' on {args.rows}x{args.cols} matrices...")
    
    cpu_bound(args.rows, args.cols, selected_op, matrix)
    

if __name__ == "__main__":
    main()

