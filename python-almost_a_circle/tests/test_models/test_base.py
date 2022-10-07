#!/usr/bin/python3
"""Contains tests for Base class"""

import pycodestyle
import inspect
import unittest
from models import base
Base = base.Base


class TestDocsBase(unittest.TestCase):
    """Tests for presence of Base class documentation"""

    @classmethod
    def setUpClass(cls):
        """Easy access to all functions"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring(self):
        """Tests for the presence of module documentation"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstring(self):
        """Tests for the presence of Base class documentation"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstrings(self):
        """Tests for the presence of docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)

    def test_pycode_class(self):
        """ Checks pycodestyle for base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pycode_test(self):
        """ Checks pycodestyle for test_base """
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_models/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")


class TestBase(unittest.TestCase):
    """Tests class functionality"""

    def test_no_id(self):
        """Tests for handling id as None"""
        b = Base()
        b1 = Base()
        self.assertEqual(b.id, 1)
        self.assertEqual(b1.id, 2)

    def test_id_set(self):
        """Tests setting id when not None"""
        self.assertEqual(Base(89).id, 89)

    def test_no_id_following_set(self):
        """Tests id as None following not None"""
        self.assertEqual(Base().id, 3)

    def test_too_many_arguments(self):
        """Tests for handling of too many args"""
        with self.assertRaises(TypeError):
            Base(8, 8)

    def test_None_to_json(self):
        """Tests for handling of None by to_json_string"""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_to_json(self):
        """
        Tests for handling of an empty string
        by to_json_string
        """
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_particular_id_to_json(self):
        """"Tests that to_json_string works normally"""
        d1 = {'id': 12}
        json_string = Base.to_json_string([d1])
        self.assertTrue(type(json_string) is str)
        self.assertEqual(json_string, '[{"id": 12}]')

    def test_None_from_json(self):
        """Tests for handling of None by from_json_string"""
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_from_json(self):
        """
        Tests for handling of an empty string
        by from_json_string
        """
        self.assertEqual(Base.from_json_string(""), [])

    def test_particular_id_from_json(self):
        """"Tests that from_json_string works normally"""
        d1 = '[{"id": 89}]'
        json_string = Base.from_json_string(d1)
        self.assertTrue(type(json_string) is list)
        self.assertEqual(json_string, [{'id': 89}])
