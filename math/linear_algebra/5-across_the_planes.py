#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    """Add two 2D matrices element-wise. Returns None if shapes don't match."""
    if [len(r) for r in mat1] != [len(r) for r in mat2]:
        return None
    return [[a+b for a, b in zip(r1, r2)] for r1, r2 in zip(mat1, mat2)]
