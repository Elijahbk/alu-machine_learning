#!/usr/bin/env python3
"""
Element-wise Matrix Operations using NumPy

This module provides functions for performing element-wise operations
on matrices using NumPy's vectorized operations.
"""


import numpy as np


def np_elementwise(mat1, mat2):
    """
    Perform element-wise operations on two matrices using NumPy.

    Args:
        mat1: First matrix (numpy.ndarray)
        mat2: Second matrix (numpy.ndarray or scalar)

    Returns:
        tuple: Contains four numpy.ndarrays resulting from:
              (addition, subtraction, multiplication, division)

    Note:
        Uses NumPy's broadcasting rules for operations between
        arrays of different shapes or between arrays and scalars.

    Example:
        >>> mat1 = np.array([[11, 22], [33, 44]])
        >>> mat2 = np.array([[1, 2], [3, 4]])
        >>> np_elementwise(mat1, mat2)
        (array([[12, 24], [36, 48]]),
         array([[10, 20], [30, 40]]),
         array([[ 11,  44], [ 99, 176]]),
         array([[11. , 11. ], [11. , 11. ]]))
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
