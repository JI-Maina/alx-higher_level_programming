#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):

    def setUp(self):
        self.b1 = Base()
        self.b2 = Base(None)
        self.b3 = Base(89)
        self.b4 = Base()

    def tearDown(self):
        del self.b1
        del self.b2
        del self.b3
        del self.b4

    def test_id(self):
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b3.id, 89)
        self.assertEqual(self.b4.id, 3)


if __name__ == "__main__":
    unittest.main()
