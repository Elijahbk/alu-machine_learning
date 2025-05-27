#!/usr/bin/env python3
def np_elementwise(mat1, mat2):
    # Function to apply an operation to two elements
    def apply_op(op, a, b):
        return op(a, b)
    
    # Function to handle scalar or matrix
    def process(mat, scalar=False):
        if isinstance(mat, (int, float)):
            return lambda other: [[mat for _ in row] for row in other]
        return lambda other: other
    
    # Ensure mat2 is treated as a matrix if it's a scalar
    mat2_processed = process(mat2)(mat1) if isinstance(mat2, (int, float)) else mat2
    
    # Perform operations using map and zip
    add = list(map(lambda rows: list(map(lambda a, b: a + b, *rows)), zip(mat1, mat2_processed)))
    sub = list(map(lambda rows: list(map(lambda a, b: a - b, *rows)), zip(mat1, mat2_processed)))
    mul = list(map(lambda rows: list(map(lambda a, b: a * b, *rows)), zip(mat1, mat2_processed)))
    div = list(map(lambda rows: list(map(lambda a, b: a / b, *rows)), zip(mat1, mat2_processed)))
    
    return (add, sub, mul, div)
