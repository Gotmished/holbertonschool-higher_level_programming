#!/usr/bin/python3
"""
Contains tests for Rectangle subclass of Base class
"""

import os
import json
import pycodestyle
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
            self.assertTrue(len(func[1].__doc__) >= 1)
#            if not func[1].__doc__:
#                print(f"{func[0]} lacks documentation")
#            else:

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """ Checks pycodestyle for test_base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


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
        with self.assertRaises(ValueError):
            Rectangle(0, 1)

    def test_height_non_positive(self):
        """Test handling ints <= 0 for height"""
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 0)

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

    def test___str___exists(self):
        """Testing normal functioning of __str__"""
        self.assertEqual(self.r5.__str__(), '[Rectangle] (14) 12/13 - 10/11')

    def test_display(self):
        """Testing normal functioning of display"""
        self.assertTrue(isinstance(self.r2.display(), str))

    def test_display_too_many_args(self):
        """Test handling display with too many args"""
        with self.assertRaises(TypeError):
            self.r2.display(1)

    def test_to_dictionary(self):
        """Testing normal functioning of to_dictionary"""
        self.assertTrue(isinstance(self.r5.to_dictionary(), dict))

    def test_update_args(self):
        """Testing normal functioning of update with *args"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(89)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 1/1")
        r.update(89, 2)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/1")
        r.update(89, 2, 3)
        self.assertEqual(str(r), "[Rectangle] (89) 0/0 - 2/3")
        r.update(89, 2, 3, 4)
        self.assertEqual(str(r), "[Rectangle] (89) 4/0 - 2/3")
        r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_kwargs(self):
        """Testing normal functioning of update with **kwargs"""
        r = Rectangle(1, 1, 0, 0, 1)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/1")
        r.update(height=10)
        self.assertEqual(str(r), "[Rectangle] (1) 0/0 - 1/10")
        r.update(width=11, x=2)
        self.assertEqual(str(r), "[Rectangle] (1) 2/0 - 11/10")
        r.update(y=3, width=4, x=5, id=89)
        self.assertEqual(str(r), "[Rectangle] (89) 5/3 - 4/10")
        r.update(x=6, height=7, y=8, width=9)
        self.assertEqual(str(r), "[Rectangle] (89) 6/8 - 9/7")

    def test_create(self):
        """Testing normal functioning of create"""
        r = {"id": 89, "width": 1, "height": 2, "x": 3, "y": 4}
        rc = Rectangle.create(**r)
        self.assertEqual("[Rectangle] (89) 3/4 - 1/2", str(rc))

    def test_None_save_to_file(self):
        """Testing None with save_to_file"""
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_empty_save_to_file(self):
        """Testing empty list with save_to_file"""
        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_normal_save_to_file(self):
        """Testing normal functioning of save_to_file with two instances"""
        r1 = Rectangle(1, 1, 1, 1, 1)
        r2 = Rectangle(2, 2, 2, 2, 2)
        l_insts = [r1, r2]
        Rectangle.save_to_file(l_insts)
        with open("Rectangle.json", "r") as f:
            l_dicts = [r1.to_dictionary(), r2.to_dictionary()]
            self.assertEqual(json.dumps(l_dicts), f.read())

    def test_load_from_file(self):
        """Testing load_from_file"""
        l_insts = [self.r2, self.r3]
        Rectangle.save_to_file(l_insts)
        l_from = Rectangle.load_from_file()
        self.assertEqual(str(l_from[1]), str(self.r3))

    def test_load_from_file_no_file(self):
        """Testing load_from_file when file doesn't exist"""
        filename = "Rectangle.json"
        if os.path.exists(filename):
            os.remove(filename)
        self.assertEqual(Rectangle.load_from_file(), [])
