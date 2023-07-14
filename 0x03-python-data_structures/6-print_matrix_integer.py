#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return
    for row in matrix:
        for b in row:
            print("{:3d}".format(b), end="")
        print()
