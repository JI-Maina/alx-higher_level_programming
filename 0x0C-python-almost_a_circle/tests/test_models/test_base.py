#!/usr/bin/python3
"""Defines unittests for Base.py"""

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Unittests for testing insantiation of base class"""

#    @classmethod
#    def setUpClass(cls):
#        cls.b1 = Base()

    def test_id(self):
        b1 = Base()
        b2 = Base(None)
        b3 = Base(89)
        b4 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b4.id, 3)

    def test_unique_id(self):
        b1 = Base(89)
        self.assertEqual(b1.id, 89)

    def test_none_id(self):
        b1 = Base()
        b2 = Base(None)
        self.assertEqual(b2.id, 2)

    def test_non_int_id(self):
        b6 = Base([])
        b7 = Base((1,))
        self.assertEqual(b6.id, [])
        self.assertEqual(b7.id, (1,))

    def test_bool_id(self):
        b8 = Base(True)
        self.assertEqual(b8.id, True)

    def test_more_than_one_args(self):
        with self.assertRaises(TypeError):
            b5 = Base(1, 2)

if __name__ == "__main__":
    unittest.main()
