import argparse


def options():
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
        "-m", "--mode", choices=["sequential", "threaded", "parallel"],
        default="sequential", help="Execution mode."
    )

    return parser.parse_args()
