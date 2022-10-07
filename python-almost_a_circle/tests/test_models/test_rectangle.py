#!/usr/bin/python3
"""
Contains tests for Rectangle subclass of Base class
"""

import inspect
import unittest
from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle


class TestDocsRectangle(unittest.TestCase):
    """Tests for presence of Rectangle subclass documentation"""

    @classmethod
    def setUpClass(cls):
        """Easy access to all functions"""
        cls.rectangle_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the presence of module documentation"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of Rectangle subclass documentation"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of documentation in all functions"""
        for func in self.rectangle_funcs:
            if not func[1].__doc__:
                print(f"{func[0]} lacks documentation")
            else:
                self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """Tests class functionality"""

    @classmethod
    def setUpClass(cls):
        """Creating attributes for testing"""
        Base._Base__nb_objects = 0
        cls.r2 = Rectangle(1, 2)
        cls.r3 = Rectangle(3, 4, 5)
        cls.r4 = Rectangle(6, 7, 8, 9)
        cls.r5 = Rectangle(10, 11, 12, 13, 14)

    def test_id(self):
        """Tests for handling id"""
        self.assertEqual(self.r2.id, 1)
        self.assertEqual(self.r3.id, 2)
        self.assertEqual(self.r5.id, 14)
        self.assertEqual(self.r4.id, 3)

    def test_width(self):
        """Tests setting of width"""
        self.assertEqual(self.r2.width, 1)
        self.assertEqual(self.r5.width, 10)

    def test_height(self):
        """Tests setting of height"""
        self.assertEqual(self.r2.height, 2)
        self.assertEqual(self.r4.height, 7)

    def test_x(self):
        """Test for setting x-coordinate"""
        self.assertEqual(self.r2.x, 0)
        self.assertEqual(self.r3.x, 5)

    def test_y(self):
        """Test for setting y-coordinate"""
        self.assertEqual(self.r2.y, 0)
        self.assertEqual(self.r5.y, 13)

    def test_width_non_int(self):
        """Test handling non-ints for width"""
        with self.assertRaises(TypeError):
            Rectangle("hello", 1)

    def test_height_non_int(self):
        """Test handling non-ints for height"""
        with self.assertRaises(TypeError):
            Rectangle(1, "hello")

    def test_width_non_positive(self):
        """Test handling ints <= 0 for width"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)

    def test_height_non_positive(self):
        """Test handling ints <= 0 for height"""
        with self.assertRaises(ValueError):
            Rectangle(1, -1)

    def test_non_coordinate_x(self):
        """Tests for handling of non-coordinate"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, "Hamish")

    def test_non_coordinate_y(self):
        """Tests for handling of non-coordinate"""
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 4, "Hamish")

    def test_x_below_zero(self):
        """Test handling ints < 0 for x"""
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)

    def test_y_below_zero(self):
        """Test handling ints < 0 for y"""
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)

    def test_area(self):
        """Testing area output"""
        self.assertEqual(self.r2.area(), 2)

    def test_area_too_many_args(self):
        """Testing handling of too many args"""
        with self.assertRaises(TypeError):
            self.r2.area(1)

    def test_display_too_many_args(self):
        """Test handling display with too many args"""
        with self.assertRaises(TypeError):
            self.r2.display(1)
