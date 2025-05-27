#!/usr/bin/env python3
def np_elementwise(mat1, mat2):
    # Determine if mat2 is a scalar (int or float)
    if isinstance(mat2, (int, float)):
        # Perform operations with scalar
        add = [[elem + mat2 for elem in row] for row in mat1]
        sub = [[elem - mat2 for elem in row] for row in mat1]
        mul = [[elem * mat2 for elem in row] for row in mat1]
        div = [[elem / mat2 for elem in row] for row in mat1]
    else:
        # Perform element-wise operations between two matrices
        add = [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
        sub = [[mat1[i][j] - mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
        mul = [[mat1[i][j] * mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
        div = [[mat1[i][j] / mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]
    return (add, sub, mul, div)
