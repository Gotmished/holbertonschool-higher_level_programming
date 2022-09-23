#!/usr/bin/pyhton3
"""
The "0-add_integer" module, with one function:

add_integer(a, b)
"""


def add_integer(a, b=98):
    """
    Adds two numbers and returns the result
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
