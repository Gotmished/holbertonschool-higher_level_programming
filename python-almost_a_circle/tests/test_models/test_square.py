#!/usr/bin/python3
"""
Contains tests for Square subclass of
Rectangle subclass of Base class
"""

import inspect
import unittest
from models import square
from models.base import Base
Square = square.Square


class TestDocsSquare(unittest.TestCase):
    """Tests for presence of Square subclass documentation"""

    @classmethod
    def setUpClass(cls):
        """Easy access to all functions"""
        cls.square_funcs = inspect.getmembers(Square, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the presence of module documentation"""
        self.assertTrue(len(square.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of Square subclass documentation"""
        self.assertTrue(len(Square.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of documentation in all functions"""
        self.assertTrue(len(func[1].__doc__) >= 1)
#        for func in self.square_funcs:
#            if not func[1].__doc__:
#                print(f"{func[0]} lacks documentation")
#            else:



class TestSquare(unittest.TestCase):
    """Tests class functionality"""

    @classmethod
    def setUpClass(cls):
        """Creating attributes for testing"""
        Base._Base__nb_objects = 0
        cls.s1 = Square(1)
        cls.s2 = Square(2, 3)
        cls.s3 = Square(4, 5, 6)
        cls.s4 = Square(7, 8, 9, 10)

    def test_id(self):
        """Tests for handling id"""
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s4.id, 10)
        self.assertEqual(self.s3.id, 3)

    def test_size(self):
        """Tests setting of size"""
        self.assertEqual(self.s2. size, 2)
        self.assertEqual(self.s4.size, 7)

    def test_x(self):
        """Test for setting x-coordinate"""
        self.assertEqual(self.s2.x, 3)
        self.assertEqual(self.s3.x, 5)

    def test_y(self):
        """Test for setting y-coordinate"""
        self.assertEqual(self.s3.y, 6)
        self.assertEqual(self.s4.y, 9)

    def test_size_non_int(self):
        """Test handling non-ints for size"""
        with self.assertRaises(TypeError):
            Square("hello", 1)

    def test_size_non_positive(self):
        """Test handling ints <= 0 for size"""
        with self.assertRaises(ValueError):
            Square(-8, 1, 4, 6)

    def test_non_coordinate_x(self):
        """Tests for handling of non-coordinate"""
        with self.assertRaises(TypeError):
            Square(10, "Hamish", 3)

    def test_non_coordinate_y(self):
        """Tests for handling of non-coordinate"""
        with self.assertRaises(TypeError):
            Square(10, 3, "Hamish")

    def test_x_below_zero(self):
        """Test handling ints < 0 for x"""
        with self.assertRaises(ValueError):
            Square(1, -1, 4)

    def test_y_below_zero(self):
        """Test handling ints < 0 for y"""
        with self.assertRaises(ValueError):
            Square(1, 4, -1)

    def test_area(self):
        """Testing area output"""
        self.assertEqual(self.s3.area(), 16)

    def test_area_too_many_args(self):
        """Testing handling of too many args"""
        with self.assertRaises(TypeError):
            self.s3.area(1)

    def test_display_too_many_args(self):
        """Test handling display with too many args"""
        with self.assertRaises(TypeError):
            self.s3.display(1)
