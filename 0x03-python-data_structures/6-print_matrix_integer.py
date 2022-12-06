#!/usr/bin/python3

# Prints a matrix of integers.

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        print(" ".join("{:d}".format(i) for i in row))
