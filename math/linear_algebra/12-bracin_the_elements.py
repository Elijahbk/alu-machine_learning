#!/usr/bin/env python3
"""
Element-wise Matrix Operations using NumPy

This module provides functions for performing element-wise operations
on matrices using NumPy's vectorized operations.
"""


import numpy as np

def np_elementwise(mat1, mat2):
    add = mat1 + mat2
    sub = mat1 - mat2
    mul = mat1 * mat2
    div = mat1 / mat2
    return (add, sub, mul, div)
