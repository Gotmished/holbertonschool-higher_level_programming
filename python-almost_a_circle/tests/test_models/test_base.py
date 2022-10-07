#!/usr/bin/python3
"""Contains tests for Base class"""

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


class TestBase(unittest.TestCase):
    """Tests class functionality"""

    def test_no_id(self):
        """Tests for handling id as None"""
        b = Base()
        self.assertEqual(b.id, 1)

    def test_id_set(self):
        """Tests setting id when not None"""
        self.assertEqual(Base(45).id, 45)

    def test_no_id_following_set(self):
        """Tests id as None following not None"""
        self.assertEqual(Base().id, 2)

    def test_too_many_arguments(self):
        """Tests for handling of too many args"""
        with self.assertRaises(TypeError):
            Base(8, 8)
