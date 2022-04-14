#!/usr/bin/env python3

def matrix_shape(matrix):
    shape = []
    while type(matrix) is list and len(matrix) > 0:
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
