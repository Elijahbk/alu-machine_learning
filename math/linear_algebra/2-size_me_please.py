#!/usr/bin/env python3
"""
This module provides a function to calculate the shape of a matrix.
"""

def matrix_shape(matrix):
    """
    Calculate the shape of a matrix.

    Args:
        matrix: A nested list representing a matrix.

    Returns:
        list: A list of integers representing the dimensions of the matrix.
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        if len(matrix) > 0:
            matrix = matrix[0]
        else:
            break
    return shape
