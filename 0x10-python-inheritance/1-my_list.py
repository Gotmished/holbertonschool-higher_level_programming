#!/usr/bin/python3
"""
Module "1-my_list" includes "MyList" class,
taking parameter "list" and sorting it
"""


class MyList(list):
    """
    MyList is a subclass of list
    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
