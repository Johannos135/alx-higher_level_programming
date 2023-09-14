#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_copy = matrix.copy()
    return ([[x**2 for x in matrix_copy[i]] for i in range(len(matrix))])
