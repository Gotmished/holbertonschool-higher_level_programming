#!/usr/bin/python3
"""
Contains tests for Square subclass of
Rectangle subclass of Base class
"""

import os
import json
import pycodestyle
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
        for func in self.square_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """ Checks pycodestyle for test_base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


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
        with self.assertRaises(ValueError):
            Square(0)

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

    def test___str___exists(self):
        """Testing normal functioning of __str__"""
        self.assertEqual(self.s1.__str__(), '[Square] (1) 0/0 - 1')

    def test_to_dictionary(self):
        """Testing normal functioning of to_dictionary"""
        self.assertTrue(isinstance(self.s3.to_dictionary(), dict))

    def test_update_args(self):
        """Testing normal functioning of update with *args"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(89)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 1")
        s.update(89, 2)
        self.assertEqual(str(s), "[Square] (89) 0/0 - 2")
        s.update(89, 2, 3)
        self.assertEqual(str(s), "[Square] (89) 3/0 - 2")
        s.update(89, 2, 3, 4)
        self.assertEqual(str(s), "[Square] (89) 3/4 - 2")

    def test_update_kwargs(self):
        """Testing normal functioning of update with **kwargs"""
        s = Square(1, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 1")
        s.update(size=10)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 10")
        s.update(size=11, x=2)
        self.assertEqual(str(s), "[Square] (1) 2/0 - 11")
        s.update(y=3, size=4, x=5, id=89)
        self.assertEqual(str(s), "[Square] (89) 5/3 - 4")

    def test_create(self):
        """Testing normal functioning of create"""
        s = {"id": 89, "size": 1, "x": 3, "y": 4}
        sc = Square.create(**s)
        self.assertEqual("[Square] (89) 3/4 - 1", str(sc))

    def test_None_save_to_file(self):
        """Testing None with save_to_file"""
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_empty_save_to_file(self):
        """Testing empty list with save_to_file"""
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_normal_save_to_file(self):
        """Testing normal functioning of save_to_file with two instances"""
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        l_insts = [s1, s2]
        Square.save_to_file(l_insts)
        with open("Square.json", "r") as f:
            l_dicts = [s1.to_dictionary(), s2.to_dictionary()]
            self.assertEqual(Square.to_json_string(l_dicts), f.read())

    def test_load_from_file(self):
        """Testing load_from_file"""
        l_insts = [self.s2, self.s3]
        Square.save_to_file(l_insts)
        l_from = Square.load_from_file()
        self.assertEqual(str(l_from[1]), str(self.s3))

    def test_load_from_file_no_file(self):
        """Testing load_from_file when file doesn't exist"""
        filename = "Square.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Square.load_from_file(), [])
