#!/usr/bin/env python3
"""
Matrix Operations Module

Provides functions for matrix operations including matrix transposition.
The transpose operation flips a matrix over its main diagonal.
"""


def matrix_transpose(matrix):
    """
    Compute the transpose of a 2D matrix.

    Args:
        matrix: A 2D list representing a matrix to be transposed.
               Must be rectangular (all rows same length).

    Returns:
        list: A new matrix that is the transpose of the input matrix.

    Example:
        >>> matrix_transpose([[1, 2], [3, 4]])
        [[1, 3], [2, 4]]
        >>> matrix_transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    # Determine the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0
    
    # Initialize the transposed matrix with dimensions cols x rows
    transposed = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transposed.append(new_row)
    
    return transposed
