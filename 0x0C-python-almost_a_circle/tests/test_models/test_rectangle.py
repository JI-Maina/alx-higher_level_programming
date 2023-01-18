#!/usr/bin/python3
"""Defines unittests for rectangle module."""
import unittest
from models.rectangle import Rectangle


class TestRectangleConstructor(unittest.TestCase):
    """Tests insantialization of a rectangle."""

    def test_id(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        self.assertEqual(r1.id, r2.id -1)

    def test_unique_id(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)

class TestRectangleWidth(unittest.TestCase):
    """Tests right assignment of the width of rec."""

    def test_int_width(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)

    def test_negative_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_zero_width(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_str_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
        
    def test_tuple_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle((1,), 2)

    def test_list_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 2)

    def test_bool_width(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 2)

    def test_set_width(self):
        r1 = Rectangle(10, 2)
        r1.width = 15
        self.assertEqual(r1.width, 15)

        with self.assertRaises(TypeError):
            r1.width = '15'

class TestRectangleHeight(unittest.TestCase):
    """Tests right assignment of the width of rec."""

    def test_int_height(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)

    def test_negative_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_zero_height(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_str_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
        
    def test_tuple_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle((1,), 2)

    def test_list_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 2)

    def test_bool_height(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 2)

    def test_set_height(self):
        r1 = Rectangle(10, 2)
        r1.height = 15
        self.assertEqual(r1.height, 15)

        with self.assertRaises(TypeError):
            r1.height = '15'

class TestRectangleX(unittest.TestCase):
    """Tests right assignment of the width of rec."""

    def test_int_x(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)

    def test_negative_x(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_zero_x(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_str_x(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
        
    def test_tuple_x(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle((1,), 2)

    def test_list_x(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 2)

    def test_bool_x(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 2)

    def test_set_x(self):
        r1 = Rectangle(10, 2)
        r1.x = 15
        self.assertEqual(r1.x, 15)

        with self.assertRaises(TypeError):
            r1.x = '15'

class TestRectangleY(unittest.TestCase):
    """Tests right assignment of the width of rec."""

    def test_int_y(self):
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.width, 10)

    def test_negative_y(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(-10, 2)

    def test_zero_y(self):
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 2)

    def test_str_y(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
        
    def test_tuple_y(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle((1,), 2)

    def test_list_y(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle([1], 2)

    def test_bool_y(self):
        with self.assertRaises(TypeError):
            r1 = Rectangle(True, 2)

    def test_set_y(self):
        r1 = Rectangle(10, 2)
        r1.y = 15
        self.assertEqual(r1.y, 15)

        with self.assertRaises(TypeError):
            r1.y = '15'

class TestRectangleArea(unittest.TestCase):
    """Tests right calculation of rectangle area."""

    def test_area(self):
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_large_area(self):
        r1 = Rectangle(9999999999, 9999999999)
        self.assertEqual(r1.area(), 9999999999 * 9999999999)

    def test_area_side_changes(self):
        r1 = Rectangle(3, 2)
        r1.width = 5
        r1.height = 4
        self.assertEqual(r1.area(), 20)

if __name__ == "__main__":
    unittest.main()
