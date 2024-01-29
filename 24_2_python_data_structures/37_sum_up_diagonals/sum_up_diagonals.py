def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    matrix_size = len(matrix)

    TL_to_BR = 0
    BL_to_TR = 0

    for i in range(matrix_size):
        TL_to_BR += matrix[i][i]
        BL_to_TR += matrix[i][matrix_size - i - 1]

    return TL_to_BR + BL_to_TR