def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for number in row:
            print("{}".format(number), end="")
            if row.index(number) != len(row) - 1:
                print(" ", end="")
        print()
