#!/usr/bin/env python3
def matrix_shape(matrix):
    shape = []
    currentMatrix = matrix
    while isinstance(currentMatrix, list):
        shape.append(len(currentMatrix))
        currentMatrix = currentMatrix[0] if currentMatrix else None
    return shape
