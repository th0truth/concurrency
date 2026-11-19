from pprint import pp

from matrix import Matrix


def main():
    matrix = Matrix()

    A = matrix.create(5, 5, randint=True)
    B = matrix.create(5, 5, randint=True)

    result_add = matrix.addition(A, B)
    
    result_mult = matrix.multiplication(A, B)

    pp(result_add)
    pp(result_mult)


if __name__ == "__main__":
    main()



