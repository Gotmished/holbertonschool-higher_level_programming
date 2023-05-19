#!/usr/bin/python3
"""
This is the "4-print_square" module with one function:

print_square(size)
"""


def print_square(size):
    """
    Returns a size * size matrix
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
