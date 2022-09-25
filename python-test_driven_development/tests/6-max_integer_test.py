#!/usr/bin/python3
"""
The 6-max_integer_test module
"""


import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMaxInteger(unittest.TestCase):

    def test_no_args(self):
        self.assertIsNone(max_integer())

    def test_max_end(self):
        self.assertEqual(max_integer([1, 2]), 2)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_middle(self):
        self.assertEqual(max_integer([1, 3, 2]), 3)

    def test_max_beginning(self):
        self.assertEqual(max_integer([98, 2]), 98)

    def test_one_negative(self):
        self.assertEqual(max_integer([-87, 3, 5]), 5)

    def test_all_negative(self):
        self.assertEqual(max_integer([-4, -7, -1]), -1)

    def test_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_non_int_arg(self):
        with self.assertRaises(TypeError):
            max_integer([8, 52, "Chevy Chase"])

if __name__ == "__main__":
    unittest.main()
