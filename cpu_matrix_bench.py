from matrix import Matrix
from pprint import pp


def main():
    matrix = Matrix()

    A = matrix.create(3, 3, randint=True)
    B = matrix.create(3, 3, randint=True)

    result = matrix.addition(A, B)

    pp(result)


if __name__ == "__main__":
    main()



