#!/usr/bin/env python3
"""
Matrix Operations Module

This module provides functions for matrix operations including matrix transposition.
The transpose operation flips a matrix over its main diagonal, switching row and column indices.
"""

from typing import List, Any

def matrix_transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    """
    Computes the transpose of a given 2D matrix.

    The transpose of a matrix is obtained by turning rows into columns and vice versa.
    For an m×n matrix, the transpose will be an n×m matrix.

    Args:
        matrix: A 2D matrix (list of lists) to be transposed. 
                All sublists must have equal length (rectangular matrix).

    Returns:
        A new matrix that is the transpose of the input matrix.

    Raises:
        IndexError: If the input matrix is not rectangular (all rows don't have same length).

    Examples:
        >>> matrix_transpose([[1, 2], [3, 4]])
        [[1, 3], [2, 4]]
        >>> matrix_transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]
    """
    # Validate input is a non-empty 2D matrix
    if not matrix or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Input must be a non-empty 2D matrix")

    # Get matrix dimensions
    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0

    # Verify matrix is rectangular
    if any(len(row) != cols for row in matrix):
        raise ValueError("All matrix rows must have the same length")

    # Construct transposed matrix
    transposed = []
    for j in range(cols):
        transposed.append([matrix[i][j] for i in range(rows)])
    
    return transposed
