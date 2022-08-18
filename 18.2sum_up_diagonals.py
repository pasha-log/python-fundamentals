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
    # TL-BR 
    # import numpy as np
    # a = [[11,2,4],[4,5,6],[10,8,-12]]
    # b = np.asarray(a)
    # print('Diagonal (sum): ', np.trace(b))
    # print('Diagonal (elements): ', np.diagonal(b))

    # BL-TR
    # n = len(matrix)
    # sum(matrix[i][n-i-1] for i in range(n))
    # 19

    import numpy as np
    n = len(matrix)
    b = np.asarray(matrix)
    return np.trace(b) + sum(matrix[i][n-i-1] for i in range(n))

    # Or:
    # total = 0

    # for i in range(len(matrix)):
    #     total += matrix[i][i]
    #     total += matrix[i][-1 - i]

    # return total

    # or, probably too tersely:
    #
    # return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])
    
    